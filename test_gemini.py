
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it with your actual API key.")

genai.configure(api_key=api_key)

# Choose a Gemini model
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# Generate content with the model
response = model.generate_content("Tell me a story about a dragon.")

# Print the response
print(response.text)
