from pathlib import Path
import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import chromadb


# 1. Find the Docs folder
DOCS_DIR = Path(__file__).parent / "Docs"


# 2. Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# 3. Create ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="policy_docs",
    embedding_function=None
)

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

    global collection

    client.delete_collection("policy_docs")

    collection = client.get_or_create_collection(
        name="policy_docs",
        embedding_function=None
    )

    documents = load_documents()

    chunk_id = 0

    for document in documents:
        chunks = chunk_text(document["text"])
        if not chunks:
            continue

        embeddings = embedding_model.encode(chunks).tolist()

        collection.add(
            ids=[str(chunk_id + i) for i in range(len(chunks))],
            documents=chunks,
            embeddings=embeddings,
            metadatas=[{"filename": document["filename"]} for _ in chunks]
        )
        chunk_id += len(chunks)
        
    print(f"Added {chunk_id} chunks to ChromaDB.")

def search(query, top_k=3):

    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results

def generate_answer(question, results):

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are a business policy assistant.

Answer using only the retrieved policy information provided below.

When answering policy questions:
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
    results = search(question)
    return generate_answer(question, results)
