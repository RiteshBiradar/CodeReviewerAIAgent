import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def review_code_with_llm(language: str, code: str, debug=False) -> dict:
    try:
        # Load the prompt template
        prompt_path = "prompts/code_review_prompt.txt"
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

        with open(prompt_path, "r", encoding="utf-8") as f:
            template = f.read()

        # Fill prompt
        filled_prompt = template.format(language=language, code=code)

        # Debug mode: print the full prompt being sent
        if debug:
            print("\n🔍 Prompt being sent:\n")
            print(filled_prompt)
            print("\n---\n")

        # Generate content using Gemini
        response = model.generate_content(filled_prompt)

        return {"success": True, "response": response.text}

    except Exception as e:
        return {"success": False, "error": str(e)}
