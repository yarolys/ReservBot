from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import BOT_ADMIN_ID
from src.utils.keyboard.user import master_panel_inline_kb

router = Router()

@router.message(Command('start'), F.chat.type == 'private')
async def start(message: Message):
    user_name = message.from_user.full_name
    await message.answer(
        f'👩🏻 Добро пожаловать, {user_name}. Это Ваш кабинет для управления расписанием и записи клиентов\n'
        'Ссылка на кабинет для перехода клиентов: \n\n'
        'Возникли вопросы? Пишите @KandyBobby',
        reply_markup=master_panel_inline_kb
    )
    if message.from_user.id == BOT_ADMIN_ID:
        await message.answer('Для запуска админки нажми /admin')
