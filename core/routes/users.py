from fastapi import APIRouter
from core.db import users
from core.models import User
from core import helpers
import bcrypt

router = APIRouter(
    prefix='/users',
)


@router.post('/')
async def register(
    username: str,
    email: str,
    password: str
):

    if users.find_one({"username": username}) or users.find_one({"email": email}):
        return 'error'

    user = User(username=username, email=email, password=helpers.hash_pass(password))

    if hasattr(user, 'id'):
        delattr(user, 'id')

    new_user_id = users.insert_one(user.dict(by_alias=True)).inserted_id
    new_user = User(**users.find_one({"_id": new_user_id}))

    return new_user


@router.post('/login')
async def login(
    email: str,
    password: str
):
    return "login"


@router.get('/test')
async def test():
    return "hello users"
