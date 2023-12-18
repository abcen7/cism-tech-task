from .schemas import UserCreate
from .models import User
from .repositories import UsersRepository
from typing import List

class UsersService:

    def __init__(self) -> None:
        self.repository = UsersRepository()
    
    async def get_all(self) -> List[User]:
        return await self.repository.get_all()
    
    async def create(self, user: UserCreate) -> User:
        return await self.repository.create(user)
    
    async def get_one(self, user_id: int) -> User:
        return await self.repository.get_one(user_id)
    