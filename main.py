import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

user_prompt = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Usage: python main.py '<your prompt>'")
second_arg = sys.argv[2] if len(sys.argv) > 2 else ""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
)

print(response.text)
if second_arg.lstrip("-") == "verbose":
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")