from fastapi import HTTPException, status

class UserAlreadyExists(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with such email already exists"
        )