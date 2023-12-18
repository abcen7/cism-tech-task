from utils import get_hashed_password
from .exceptions import UserAlreadyExists
from .schemas import UserCreate
from .models import User
from .repositories import UsersRepository
from typing import List

class UsersService:

    def __init__(self) -> None:
        self.repository = UsersRepository()
    
    async def get_all(self) -> List[User]:
        return await self.repository.get_all()
    
    async def create(self, user: UserCreate) -> User | None:
        encrypted_password = get_hashed_password(user.password)
        if not await self.is_user_exists(user.email):
            return await self.repository.create(user.email, encrypted_password)
        else:
            raise UserAlreadyExists()
    
    async def get_one(self, user_id: int) -> User:
        return await self.repository.get_one(user_id)
    
    async def is_user_exists(self, email: str) -> bool:
        return await self.repository.is_user_exists(email)