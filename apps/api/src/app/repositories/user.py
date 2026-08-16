from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def get_by_email_or_username(
        self,
        email: str,
        username: str,
    ) -> User | None:
        result = await self.session.execute(
            select(User).where(
                or_(
                    User.email == email,
                    User.username == username,
                )
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        email: str,
        username: str,
        password_hash: str,
    ) -> User:
        user = User(
            email=email,
            username=username,
            password_hash=password_hash,
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user