from .utils.crud import UsersInterface, UsersRepository
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router


users = Router()
users_interface = UsersInterface(UsersRepository)


@users.message(CommandStart())
async def start_cmd(message: Message):
    await users_interface.check_user(
        user_id=message.from_user.id,
        data={"username": message.from_user.username, "user_id": message.from_user.id},
    )
    await message.answer(text=f"Здравствуйте {message.from_user.full_name}")
