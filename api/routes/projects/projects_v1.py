
from fastapi import APIRouter, HTTPException, Depends
from starlette import responses
from api.controller.loupe_controller import LoupeController
from api.lib.auth import AuthVerifier


router = APIRouter()


@router.get('/v1/projects')
async def get_all_projects(auth=Depends(AuthVerifier)):
  if auth.is_authorized():
    responses = LoupeController.get_all_projects()
    return responses
    