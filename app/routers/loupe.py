from fastapi import APIRouter

from ..lib.services import loupe_service

router = APIRouter()

@router.get('/plasmids', tags=["plasmids"])
async def get_all_plasmids():
  print("in loupe router get all plasmids")
  service = loupe_service.LoupeService()
  result = await service.fetch_all()
  return result.json()