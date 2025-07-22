from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.genai import types
from app.services.file_service import get_full_context


load_dotenv()

def generate_with_prompt(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No API KEY FOUND")
    
    client = genai.Client(api_key=api_key)
    model = "gemini-1.5-flash-002"

    context = get_full_context or ""

    contents = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=context),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

    config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    output = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config,
    ):
        output += chunk.text

    return output

