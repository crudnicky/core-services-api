from functools import lru_cache
from fastapi import FastAPI
from .routes import loupe
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins= ['http://localhost:3000'],
  allow_credentials=True,
  allow_methods=["GET"],
  allow_headers=["*"],
)

app.include_router(loupe.router)