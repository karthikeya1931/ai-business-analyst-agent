from agent import run_agent


question = "get the schema of the database and provide a clean description of the tables and columns"

answer = run_agent(question)

print("\n-----------------------------")
print("AI BUSINESS ANALYST")
print("-----------------------------")
print(answer)