from database import get_schema, run_sql


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
    """
    Executes a read-only SQL query.
    Returns either the result or the database error.
    """

    try:

        result = run_sql(query)

        return result.to_string(index=False)

    except Exception as e:

        return f"""
SQL execution failed.

Error:
{str(e)}

Query:
{query}

Correct the SQL and try again.
"""