from sqlalchemy import create_engine
import pandas as pd
import re

server = r"localhost\SQLEXPRESS"
database = "SalesAI"

connection_string = r"mssql+pyodbc://@localhost\SQLEXPRESS/SalesAI?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"

engine = create_engine(connection_string)


def run_sql(query):

    # Remove leading/trailing whitespace
    query = query.strip()

    # Only allow SELECT statements
    if not query.lower().startswith("select") and not query.lower().startswith("with"):
        raise ValueError("Only SELECT and WITH queries are allowed.")

    # Block potentially dangerous SQL commands
    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "exec",
        "execute"
    ]

    query_lower = query.lower()

    for word in forbidden:
        if re.search(rf"\b{word}\b", query_lower):
            raise ValueError(
                f"SQL command '{word.upper()}' is not allowed."
            )

    # Execute query and return DataFrame
    return pd.read_sql(query, engine)

def get_schema():

    query = """
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'dbo'
    ORDER BY TABLE_NAME, ORDINAL_POSITION;
    """

    return pd.read_sql(query, engine)