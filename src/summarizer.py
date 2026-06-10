import google.generativeai as genai
from .config import GEMINI_API_KEY, GEMINI_MODEL_NAME

def summarize_content(content: str, prompt_template: str) -> str:
    """Gemini APIを使用してコンテンツを要約・SNS案生成する"""
    if not GEMINI_API_KEY:
        return "Error: GEMINI_API_KEY not found."
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    
    prompt = prompt_template.replace("{{CONTENT}}", content)
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {str(e)}"
