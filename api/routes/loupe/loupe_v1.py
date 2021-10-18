
from fastapi import APIRouter
from starlette import responses
from api.controller.loupe_controller import LoupeController


router = APIRouter()

@router.get('/v1/loupe/projects')
async def get_all_projects():
  responses = LoupeController.get_all_projects()
  return responses