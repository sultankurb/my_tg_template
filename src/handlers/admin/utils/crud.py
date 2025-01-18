from src.utils import Interface, SQLAlchemyRepository
from src.keyboards.keyboard import get_keyboard
from src.database.models import Event, Task
from aiogram.types import Message


ADMIN_KB = get_keyboard("Получить список задач")


class EventRepository(SQLAlchemyRepository):
    model = Event


class EventInterface(Interface):
    pass


class TasksRepository(SQLAlchemyRepository):
    model = Task


class TasksInterface(Interface):

    async def get_tasks_list_for_handler(self, message: Message):
        tasks_list = await self.find_all()
        if tasks_list:
            for task in tasks_list:
                await message.answer_photo(
                    photo=task.media_url,
                    caption=f"Название: {task.title}\nОписание: {task.description}\nЗакончен ли? {task.is_done}",
                )
        else:
            await message.answer(text="Здесь ничего нету")
