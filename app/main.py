from fastapi import FastAPI
import requests

from .routers import loupe

app = FastAPI()

@app.on_event("startup")
async def startup_event():
  app.request_session = requests.Session()

app.include_router(loupe.router)