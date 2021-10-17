from fastapi import APIRouter
from unlimiter.data.api import BenchlingV2APIConnection


router = APIRouter()

@router.get('/projects')
async def get_all_projects():
  with BenchlingV2APIConnection() as benchling:
    projects = benchling.projects.list_projects()
  return projects