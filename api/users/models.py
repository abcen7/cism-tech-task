import ormar
from database import database, metadata
import datetime

class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=100, nullable=False)
    hashed_password: str = ormar.String(max_length=100, nullable=False)
    created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    