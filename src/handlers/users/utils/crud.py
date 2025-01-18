from typing import Optional

from src.settings import async_session_maker, settings
from src.utils import SQLAlchemyRepository, Interface
from src.database.models import User
from sqlalchemy import select
import logging


class UsersRepository(SQLAlchemyRepository):
    model = User

    async def select_one(self, search: Optional[int]):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(user_id=search)
            result = await session.execute(stmt)
            return result.scalar()


class UsersInterface(Interface):

    async def check_user(self, user_id: int, data: dict):
        user = await self.repository.select_one(search=user_id)
        if data.get("user_id") == settings.ADMIN_ID:
            data.update(is_admin=True)
        if user is None:
            await self.add_one(data=data)
            logging.info(msg=f"user with id={user_id} started work with bot")
