from fastapi import FastAPI

from unlimiter.data.api import BenchlingV2APIConnection

app = FastAPI()

@app.get('/')
async def root():
  with BenchlingV2APIConnection() as benchling:
    projects = benchling.projects.list_projects()
  return projects