from fastapi import APIRouter
from . import users

api_router = APIRouter(
    prefix='/api',
)

api_router.include_router(users.router)
