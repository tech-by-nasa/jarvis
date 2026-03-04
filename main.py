import os
from dotenv import load_dotenv
from google import genai  # This is the modern 2026 import

load_dotenv()

# Initialize the 2026 client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Test call
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Jarvis, are you there?"
)
print(response.text)
