import ormar
from database import database, metadata
from pydantic import EmailStr
import datetime

class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key=True)
    email: EmailStr = ormar.String(max_length=100, nullable=False, unique=True)
    hashed_password: str = ormar.String(max_length=100, nullable=False)
    created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    