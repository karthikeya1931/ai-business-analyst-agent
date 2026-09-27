import pandas as pd
from sqlalchemy import create_engine

server = r"localhost\SQLEXPRESS"
database = "SalesAI"

connection_string = r"mssql+pyodbc://@localhost\SQLEXPRESS/SalesAI?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"

engine = create_engine(connection_string)

query = "SELECT TOP 10 * FROM dbo.Orders"

df = pd.read_sql(query, engine)

print(df)