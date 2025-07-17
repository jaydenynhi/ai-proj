from fastapi import FastAPI, Request
from app.routes import file

app = FastAPI(
    docs_url="/backend"
)

app.include_router(file.router)


