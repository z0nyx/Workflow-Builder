from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def create_user(self, data: UserCreate):
        existing_user = await self.repository.get_by_email_or_username(
            data.email,
            data.username,
        )

        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email or username already exists",
            )

        return await self.repository.create(
            email=data.email,
            username=data.username,
            password_hash=hash_password(data.password),
        )