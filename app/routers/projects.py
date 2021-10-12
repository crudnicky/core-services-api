from fastapi import APIRouter

from ..lib.services import loupe_service

router = APIRouter()

@router.get('/projects', tags=["projects"])
async def get_all_plasmids():
  service = loupe_service.LoupeService()
  result = await service.fetch_projects()
  return result