from fastapi import FastAPI
import requests, okta_jwt_verifier, os
from .routers import loupe, projects
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
  app.request_session = requests.Session()

app.include_router(loupe.router)
app.include_router(projects.router)
