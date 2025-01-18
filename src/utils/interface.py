from .repository import AbstractRepository
import logging


class Interface:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def find_all(self):
        answer = await self.repository.select_all()
        logging.info(msg=f"Used function find_all()")
        return answer

    async def find_one_by_pk(self, pk: int):
        answer = await self.repository.select_one(pk=pk)
        logging.info(msg=f"Used function find_one_by_pk()")
        return answer

    async def add_one(self, data: dict):
        await self.repository.insert_one(data=data)
        logging.info(msg=f"Used function add_one()")

    async def edit_one(self, pk: int, data: dict):
        await self.repository.update_one(pk=pk, data=data)
        logging.info(msg=f"Used function edit_one()")

    async def delete_one(self, pk: int):
        await self.repository.delete_one(pk=pk)
        logging.info(msg=f"Used function delete_one()")
