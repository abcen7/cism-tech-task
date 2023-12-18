from pydantic import EmailStr, BaseModel, validator
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    created: datetime.datetime

    @validator('created')
    @classmethod
    def validate_datetime(cls, value: datetime.datetime) -> str:
        return value.strftime("%d-%m-%Y, %H:%M:%S")