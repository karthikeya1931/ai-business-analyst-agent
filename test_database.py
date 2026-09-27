from database import run_sql

query = """
DELETE FROM dbo.Orders;
"""



df = run_sql(query)

print(df)
print("\nDataFrame shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())