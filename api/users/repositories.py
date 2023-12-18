from pydantic import EmailStr
from .models import User
from .schemas import UserCreate
from typing import List

class UsersRepository:

    @staticmethod
    async def get_all() -> List[User]:
        return await User.objects.all()
    
    @staticmethod
    async def create(email: EmailStr, encrypted_password: str) -> User:
        return await User.objects.create(
            email=email,
            hashed_password=encrypted_password
        )
    
    @staticmethod
    async def get_one(id: int) -> User:
        return await User.objects.get(id)

    @staticmethod
    async def is_user_exists(email: str) -> bool:
        is_user_in_db = await User.objects.get_or_none(email=email)
        return not is_user_in_db is None