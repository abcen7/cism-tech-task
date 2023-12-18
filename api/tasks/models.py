import ormar
import datetime

from enum import Enum
from database import database, metadata


class TaskStatus(Enum):
    CREATED = 'created'
    IN_PROCCESS = 'in proccess'
    RESPONSE = 'response'


class Task(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
    
    id: int = ormar.Integer(primary_key=True)
    status: TaskStatus = ormar.Enum(enum_class=TaskStatus)
    created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    updated: datetime.datetime = ormar.DateTime(default=datetime.datetime.now(), onupdate=datetime.datetime.now())
