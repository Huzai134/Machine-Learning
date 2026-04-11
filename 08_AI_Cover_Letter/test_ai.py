import os
from dotenv import load_dotenv
from google import genai

# 1. Load the secret key from the .env file safely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Initialize the modern Gemini Client
client = genai.Client(api_key=api_key)

# 3. Give the AI a command (Using the newest 2.5 Flash model)
print("Sending request to Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Write a 1-sentence welcome message for a junior Full-Stack Developer.'
)

# 4. Print the result
print("\n--- AI RESPONSE ---")
print(response.text)