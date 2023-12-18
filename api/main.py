import uvicorn

from fastapi import FastAPI
from database import database
from contextlib import asynccontextmanager


# List of routers
from users import users_router


app = FastAPI()
app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(users_router, tags=['User'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)