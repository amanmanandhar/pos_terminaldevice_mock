from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="Mock POS terminal system")
app.include_router(api_router, prefix="/terminal")