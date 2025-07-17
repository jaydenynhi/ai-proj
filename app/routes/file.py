# to read different types of files 
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from PyPDF2 import PdfReader
from docx import Document
import io, tempfile
from typing import Optional
from app.services.file_service import get_context

router = APIRouter()

@router.post("/upload")
async def upload_file(f: UploadFile = File(...)):
    content = await f.read()

    if f.content_type == "application/pdf" or f.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        pages = [p.extract_text() for p in reader.pages]
        full_text = "\n\n".join(filter(None, pages))

    elif f.content_type == "application/docx" or f.filename.endswith(".docx"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        doc = Document(tmp_path)
        full_text = "\n".join(p.text for p in doc.paragraphs)

    else:
        try:
            full_text = content.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(400, "Unsupported file type or binary format")
        
    return {"message": "File uploaded and context stored"}  

@router.get("/context")
async def list_contexts(
    filename: Optional[str] = Query(
        None,
    )
):
    return get_context(filename)


