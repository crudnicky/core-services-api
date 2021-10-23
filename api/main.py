from functools import lru_cache
from fastapi import FastAPI
from .routes.projects import projects_v1
from starlette.middleware.cors import CORSMiddleware
from starlette.config import Config
from dotenv import load_dotenv

load_dotenv('.env.dev')

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins= ['http://localhost:3000'],
  allow_credentials=True,
  allow_methods=["GET"],
  allow_headers=["*"],
)

app.include_router(projects_v1.router)