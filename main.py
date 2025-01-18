from src.handlers.main_router import router
from aiogram import Dispatcher, Bot
from src.settings import settings
import asyncio
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s:%(message)s",
)
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)
bot.my_admins_list = [settings.ADMIN_ID]


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
