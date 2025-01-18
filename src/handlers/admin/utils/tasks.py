from .crud import TasksInterface, TasksRepository, ADMIN_KB
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F


tasks = Router()
tasks_interface = TasksInterface(TasksRepository)


@tasks.message(Command("admin"))
async def admin_cmd(message: Message):
    await message.answer(text="Что вы бы хотели сделать?", reply_markup=ADMIN_KB)


@tasks.message(Command("Получить список задач"))
@tasks.message(F.text == "Получить список задач")
async def get_list_tasks(message: Message):
    await tasks_interface.get_tasks_list_for_handler(message=message)


@tasks.message(Command(""))
@tasks.message(F.text == "")
async def start_add_task():
    pass
