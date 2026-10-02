from database import get_schema, run_sql
from rag import rag_tool as retrieve_policy_answer


def schema_tool():
    """
    Returns a clean description of the database schema.
    """

    schema = get_schema()

    output = []

    for table_name, table_df in schema.groupby("TABLE_NAME"):

        output.append(f"\n{table_name}:")

        for _, row in table_df.iterrows():
            output.append(
                f"- {row['COLUMN_NAME']} ({row['DATA_TYPE']})"
            )

    return "\n".join(output)


def sql_tool(query):
    try:
        result = run_sql(query)

        return {
            "success": True,
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "query": query
        }


def rag_tool(question):
    return retrieve_policy_answer(question)
