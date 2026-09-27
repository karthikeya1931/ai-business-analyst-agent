import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
print("1. Python started")

api_key = os.getenv("GEMINI_API_KEY")

print("2. API key found:", bool(api_key))

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

print("3. Creating Gemini client...")

client = genai.Client(
    api_key=api_key
)

print("4. Client created")

print("5. Sending request...")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Which category has the highest total profit?"
)

print("6. Response received")

print(response.text)