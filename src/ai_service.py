from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(
        timeout=60000
    )
)


def ask_gemini(question: str) -> str:

    if not question.strip():
        return "Please enter a question."

    prompt = f"""
You are Smart Student Buddy, a helpful AI assistant.

Explain answers in simple language with examples.

Student's question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        if response.text:
            return response.text

        return "No answer was generated."

    except Exception as error:

        return (
            f"Gemini Error: {type(error).__name__}: {error}"
        )