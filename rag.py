from pathlib import Path
from functools import lru_cache
from database import engine
from sqlalchemy import text
import os
import re
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer, CrossEncoder
#import chromadb(moving from chromadb to pgvector)


# 1. Find the Docs folder
DOCS_DIR = Path(__file__).parent / "Docs"


# 2. Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


@lru_cache(maxsize=1)
def get_reranker():
    """Load the relevance model once, when retrieval first needs it."""
    return CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", max_length=512)


# # 3. Create ChromaDB
# client = chromadb.PersistentClient(path="./chroma_db")

# collection = client.get_or_create_collection(
#     name="policy_docs",
#     embedding_function=None
# )

#loading llm
load_dotenv()

groq_client = Groq( api_key=os.getenv("GROQ_API_KEY")
)

def load_documents():
    documents = []

    for file in DOCS_DIR.glob("*.md"):
        text = file.read_text(encoding="utf-8")

        documents.append({
            "filename": file.name,
            "text": text
        })

    return documents


def chunk_text(text, chunk_size=1500):
    """Split by headings, then paragraphs; repeat heading context in each chunk."""
    import re

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    lines = text.splitlines()
    title = next((line[2:].strip() for line in lines if line.startswith("# ")), "Untitled document")
    headings = {}
    sections = []
    content = []
    fence = ""

    # Collect each section together with its parent headings.
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            if not fence:
                fence = stripped[:3]
            elif stripped == fence:
                fence = ""

        heading = re.match(r"^(#{1,6})\s+(.+)$", line) if not fence else None
        if heading:
            if content:
                sections.append((list(headings.values()), "\n".join(content)))
            content = []
            level = len(heading.group(1))
            headings = {key: value for key, value in headings.items() if key < level}
            if level > 1:
                headings[level] = heading.group(2)
        else:
            content.append(line)

    if content:
        sections.append((list(headings.values()), "\n".join(content)))

    chunks = []
    for section_headings, body in sections:
        context = f"Document: {title}\n"
        if section_headings:
            context += "Section: " + " > ".join(section_headings) + "\n"
        current = ""

        # Blank lines separate paragraphs; consecutive table rows stay together.
        for paragraph in re.split(r"\n\s*\n", body.strip()):
            if not paragraph:
                continue
            if current and len(current) + 2 + len(paragraph) > chunk_size:
                chunks.append(context + "\n" + current)
                current = ""

            # Only cut within a paragraph if it alone exceeds the limit.
            # Tables and fenced blocks may exceed this soft body-size limit.
            if not paragraph.startswith(("|", "```", "~~~")):
                while len(paragraph) > chunk_size:
                    chunks.append(context + "\n" + paragraph[:chunk_size])
                    paragraph = paragraph[chunk_size:]

            current = current + "\n\n" + paragraph if current else paragraph

        if current:
            chunks.append(context + "\n" + current)

    return chunks


def build_rag_database():
    ensure_fts_index()
    chunks = []
    sources = []

    for file_path in DOCS_DIR.glob("*.md"):
        text_content = file_path.read_text(encoding="utf-8")

        file_chunks = chunk_text(text_content)

        chunks.extend(file_chunks)
        sources.extend([file_path.name] * len(file_chunks))

    print(f"Total chunks: {len(chunks)}")

    embeddings = embedding_model.encode(chunks).tolist()

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM policy_documents")
        )

        for chunk, source, embedding in zip(
            chunks, sources, embeddings
        ):
            connection.execute(
                text("""
                    INSERT INTO policy_documents
                    (content, source, embedding)
                    VALUES (:content, :source, :embedding)
                """),
                {
                    "content": chunk,
                    "source": source,
                    "embedding": str(embedding)
                }
            )

    print("RAG database built successfully.")

@lru_cache(maxsize=1)
def ensure_fts_index():
    """Upgrade existing policy chunks without rebuilding their embeddings."""
    with engine.begin() as connection:
        # Separate numeric ranges so 11-20% indexes both 11 and 20, not -20.
        # PostgreSQL maintains this column on every insert/update.
        connection.execute(text(r"""
            ALTER TABLE policy_documents
            ADD COLUMN IF NOT EXISTS search_vector TSVECTOR
            GENERATED ALWAYS AS (
                to_tsvector('english', regexp_replace(
                    content, '([0-9])[[:space:]]*[-–—][[:space:]]*([0-9])',
                    '\1 \2', 'g'
                ))
            ) STORED
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_policy_documents_search_vector
            ON policy_documents USING GIN (search_vector)
        """))


def semantic_search(query, top_k=5):
    if top_k <= 0:
        return []

    query_embedding = embedding_model.encode(query).tolist()

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    id,
                    content,
                    source,
                    1 - (embedding <=> CAST(:embedding AS vector)) AS similarity
                FROM policy_documents
                WHERE embedding IS NOT NULL
                ORDER BY embedding <=> CAST(:embedding AS vector), id
                LIMIT :top_k
            """),
            {
                "embedding": str(query_embedding),
                "top_k": top_k
            }
        )

        return [
            {
                "id": row.id,
                "content": row.content,
                "source": row.source,
                "semantic_score": row.similarity,
                "similarity": row.similarity
            }
            for row in result
        ]
def search(query, top_k=5):
    """Keep the original vector-search API for existing callers."""
    return semantic_search(query, top_k)


def keyword_search(query, top_k=5):
    if top_k <= 0:
        return []
    ensure_fts_index()
    normalized = re.sub(r"\b(?:percent(?:age)?|per\s+cent)\b", "%", query, flags=re.I)
    normalized = re.sub(r"(?<=\d)\s*[-–—]\s*(?=\d)", " ", normalized)
    # Prefer full matches. If there are none, relax to the chunks matching
    # the most distinct terms, so repeated generic words cannot dominate.
    terms = re.findall(r"[^\W_]+", normalized, flags=re.UNICODE)
    broad_query = " OR ".join(terms)
    with engine.connect() as connection:
        result = connection.execute(text("""
            WITH queries AS (
                SELECT websearch_to_tsquery('english', :query) AS exact_query,
                       websearch_to_tsquery('english', :broad_query) AS broad_query,
                       tsvector_to_array(to_tsvector('english', :query)) AS terms
            ), matches AS (
                SELECT id, content, source,
                       search_vector @@ exact_query AS full_match,
                       (SELECT COUNT(*) FROM unnest(terms) AS term
                        WHERE term = ANY(tsvector_to_array(search_vector))) AS matched_terms,
                       ts_rank_cd(search_vector, broad_query, 2) AS keyword_score
                FROM policy_documents CROSS JOIN queries
                WHERE search_vector @@ exact_query OR search_vector @@ broad_query
            ), ranked_matches AS (
                SELECT *, MAX(full_match::int) OVER () AS has_full_match,
                          MAX(matched_terms) OVER () AS best_coverage
                FROM matches
            )
            SELECT id, content, source, keyword_score
            FROM ranked_matches
            WHERE full_match OR (has_full_match = 0 AND matched_terms = best_coverage)
            ORDER BY keyword_score DESC, id
            LIMIT :top_k
        """), {"query": normalized, "broad_query": broad_query, "top_k": top_k})
        return [dict(row._mapping) for row in result]


def hybrid_search(query, top_k=5):
    """Fuse 10 candidates per search, rerank all, and return at most 5."""
    if top_k <= 0:
        return []
    top_k = min(top_k, 5)
    candidate_count = 10
    semantic_results = semantic_search(query, candidate_count)
    keyword_results = keyword_search(query, candidate_count)
    merged = {}
    for rank_name, score_name, results in (
        ("semantic_rank", "semantic_score", semantic_results),
        ("keyword_rank", "keyword_score", keyword_results),
    ):
        for rank, result in enumerate(results, start=1):
            chunk = merged.setdefault(result["id"], {
                "id": result["id"],
                "content": result["content"],
                "source": result["source"],
                "hybrid_score": 0.0,
                "semantic_rank": None,
                "keyword_rank": None,
                "semantic_score": None,
                "keyword_score": None,
            })
            chunk[rank_name] = rank
            chunk[score_name] = result[score_name]
            chunk["hybrid_score"] += 1 / (60 + rank)
    candidates = sorted(merged.values(), key=lambda item: (-item["hybrid_score"], item["id"]))
    if not candidates:
        return []

    # Score the entire candidate union before the final cutoff, so evidence
    # outside RRF's top five still has a chance to reach the answer context.
    scores = get_reranker().predict(
        [(query, item["content"]) for item in candidates],
        show_progress_bar=False,
    )
    for item, score in zip(candidates, scores):
        item["rerank_score"] = float(score)
    return sorted(candidates, key=lambda item: (
        -item["rerank_score"], -item["hybrid_score"], item["id"]
    ))[:top_k]


def generate_answer(question, results):

    context = "\n\n".join(
    result["content"]
    for result in results
)

    prompt = f"""
You are a business policy assistant.

Answer using only the retrieved policy information provided below.

When answering policy questions:
- Discount is an absolute monetary discount per unit, not a percentage. Discount Rate is Discount / (Unit_Price + Discount). Policy percentage limits apply to Discount Rate; never compare raw Discount with a policy percentage.
- Distinguish approval authority from category-specific discount caps.
- When the user asks what a sales representative can give "without approval" or "without additional approval", use the approval matrix. Answer with the upper bound of the range explicitly assigned to Sales Rep in the retrieved context.
- Do NOT use a category discount cap to answer an approval-authority question. A category cap limits discounts for that category; it does not establish a sales representative's personal approval authority.
- When the user asks for the maximum discount allowed for a category, use the explicit cap for that category in the retrieved context.
- When both concepts appear in the context, select the rule that directly answers the user's wording.
- Do not combine separate limits or infer a new limit from them.
- Do not invent, infer, or reinterpret policy rules. Do not rely on outside knowledge.
- If the relevant approval matrix or category cap is missing, do not substitute the other concept as the answer.

If the answer is not present in the policy information, say:
"I could not find this information in the provided policies."

Policy information:
{context}

User question:
{question}

Give a concise answer.
"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def rag_tool(question):
    results = hybrid_search(question)
    return generate_answer(question, results)

if __name__ == "__main__":
    build_rag_database()

    results = hybrid_search(
        "What discount can a sales representative give without approval?"
    )

    for result in results:
        print("\nSOURCE:", result["source"])
        print("SEMANTIC RANK:", result["semantic_rank"])
        print("KEYWORD RANK:", result["keyword_rank"])
        print("HYBRID SCORE:", result["hybrid_score"])
        print("RERANK SCORE:", result["rerank_score"])
        print("CONTENT:")
        print(result["content"])
        print("-" * 80)
