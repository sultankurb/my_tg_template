from .utils.tasks import tasks
from aiogram import Router


admin = Router()
admin.include_router(tasks)
