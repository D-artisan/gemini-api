
import os
import hashlib
import time
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
response = model.generate_content("Teach me System Design in 5 minutes.")

# Print the response
print(response.text)

# Persist the response in response/ directory with unique filename
os.makedirs("response", exist_ok=True)
timestamp = int(time.time())
data_hash = hashlib.sha256(response.text.encode("utf-8")).hexdigest()[:8]
filename = f"response/response_{timestamp}_{data_hash}.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)
print(f"Response saved to {filename}")
