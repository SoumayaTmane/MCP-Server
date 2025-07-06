import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
else:
    print(f"Using API key (first 5 chars): {GEMINI_API_KEY[:5]}*****")
    genai.configure(api_key=GEMINI_API_KEY)

    try:
        print("\nAttempting to list models...")
        for m in genai.list_models():
            print(f"Model Name: {m.name}, Supports generateContent: {'generateContent' in m.supported_generation_methods}")
        print("\nModel listing complete. ")

    except Exception as e:
        print(f"Error connecting to Gemini API: {e}")