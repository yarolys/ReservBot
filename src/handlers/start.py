from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import BOT_ADMIN_ID, logger

router = Router()

@router.message(Command('start'), F.chat.type == 'private')
async def start(message: Message):
    await message.answer(
        'Привет. Этот бот был создан для резервирования слота на определенное время.\n'
        'Этот бот будет рассылать сообщение человеку на подтверждение своей записи, в случае отказа'
        'слот просто сгорает, так же запись в случае ошибки можно изменить.\n'
        'Проще говоря, это просто тестовый бот, который будет полезен для развития себя :P \n'
        'Создатель - @KandyBobby'
    )
    if message.from_user.id == BOT_ADMIN_ID:
        await message.answer('Для запуска админки нажми /admin')
        await message.delete()