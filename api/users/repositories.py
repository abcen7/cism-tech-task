from .models import User
from .schemas import UserCreate
from typing import List

class UsersRepository:

    @staticmethod
    async def get_all() -> List[User]:
        return await User.objects.all()
    
    @staticmethod
    async def create(user: UserCreate) -> User:
        return await User.objects.create(**user.dict())
    
    @staticmethod
    async def get_one(id: int) -> User:
        return await User.objects.get(id)
