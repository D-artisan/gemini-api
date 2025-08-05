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

# Get all available models and write to a Markdown file
models = list(genai.list_models())

with open("available_models.md", "w", encoding="utf-8") as f:
    f.write("# Available Gemini Models\n\n")
    f.write("| Model Name | Supported Generation Methods |\n")
    f.write("|------------|----------------------------|\n")
    for m in models:
        methods = ", ".join(m.supported_generation_methods)
        f.write(f"| `{m.name}` | {methods} |\n")

print("Model list written to available_models.md")
