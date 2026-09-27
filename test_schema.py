from database import get_schema

schema = get_schema()

print(schema.to_string(index=False))