from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from src.config import logger

from src.utils.filter import AdminRoleFilter
from src.utils.keyboard.user import master_panel_inline_kb

router = Router()


@router.message(Command('user'))
@router.message(F.text == 'Назад')
async def admin_panel(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в меню пользователя!',
                        reply_markup=master_panel_inline_kb)
    await state.clear()
    await message.delete()
