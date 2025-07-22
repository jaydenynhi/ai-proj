from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.core.llm import generate_with_prompt  # Gemini call wrapper

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

def build_system_prompt(question: str) -> str:
    return (
        "You are Jayden’s assistant. Answer clearly and factually. "
        "If you don't know the answer, say so.\n\n"
        f"Question: {question}"
    )

@router.post("/generate")
async def generate_text(request: PromptRequest) -> Dict[str, Any]:
    try:
        question = request.prompt.strip()
        if not question:
            raise HTTPException(status_code=400, detail="Prompt cannot be empty")

        prompt = build_system_prompt(question)

        # Gemini API call (no vector search)
        answer = generate_with_prompt(prompt).strip()

        return {"response": answer}

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
