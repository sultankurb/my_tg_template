from sqlalchemy import select, insert, delete, update
from src.settings import async_session_maker
from abc import ABC, abstractmethod
from typing import Optional


class AbstractRepository(ABC):

    @abstractmethod
    async def select_all(self):
        raise NotImplementedError

    @abstractmethod
    async def select_one(self, search: Optional[int]):
        raise NotImplementedError

    @abstractmethod
    async def insert_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, pk: int, data: dict):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def select_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    async def select_one(self, search: Optional[int]):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(pk=search)
            result = await session.execute(stmt)
            return result.scalar()

    async def insert_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data)
            await session.execute(stmt)
            await session.commit()

    async def delete_one(self, pk: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(pk=pk)
            await session.execute(stmt)
            await session.commit()

    async def update_one(self, pk: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(pk=pk).values(**data)
            await session.execute(stmt)
            await session.commit()
