from typing import List
from fastapi import APIRouter, Depends
from starlette import status

from .models import User
from .schemas import UserCreate, UserRead
from .services import UsersService

users_router = APIRouter()


@users_router.post(
    "/users",
    status_code=status.HTTP_200_OK
)
async def create_user(user: UserCreate, users_service: UsersService = Depends()) -> User:
    return await users_service.create(user)

@users_router.get(
    "/users",
    status_code=status.HTTP_200_OK
)
async def get_all_users(users_service: UsersService = Depends()) -> List[UserRead]:
    return await users_service.get_all()

