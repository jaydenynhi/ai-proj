# to read different types of files 
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from PyPDF2 import PdfReader
from docx import Document
import io, tempfile

router = APIRouter()

@router.post("/upload")
async def upload_file(f: UploadFile = File(...)):
    content = await f.read()

    if f.content_type == "application/pdf" or f.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        pages = [p.extract_text() for p in reader.pages]
        full_text = "\n\n".join(filter(None, pages))
