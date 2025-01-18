from aiogram import Router
from .users.router import users
from .admin.router import admin

router = Router()
router.include_routers(users, admin)
