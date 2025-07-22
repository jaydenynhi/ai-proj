from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
import os

def load_doc(folder_path: str):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") or filename.endswith(".md"):
            loader = TextLoader(os.path.join(folder_path, filename), encodings="utf-8")
            docs.extend(loader.load())
    return docs

def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

documents = load_doc("/doc")
chunks = split_documents(documents)

embedding_model = SentenceTransformerEmbeddings(model_name="gemini-1.5-flash")
