import databases
import sqlalchemy

from enum import Enum
from os import environ
from config import DATABASE_URL


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

from users import User
from tasks import Task

# TODO: Check env before creating metadata
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)