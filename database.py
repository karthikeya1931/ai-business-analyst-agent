import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
import pandas as pd
import re

server = r"localhost\SQLEXPRESS"
database = "SalesAI"

load_dotenv()
#connection_string = r"mssql+pyodbc://@localhost\SQLEXPRESS/SalesAI?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
connection_url = URL.create(
    "postgresql+psycopg",
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB")
)
engine = create_engine(connection_url)


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
        table_schema,
        table_name,
        column_name,
        data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position;
    """
    return pd.read_sql(query, engine)

