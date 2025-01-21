from aiogram import F, Router
from aiogram.types import CallbackQuery

from src.utils.keyboard.user import master_panel_inline_kb, schedule_management_kb, clients_kb, records_kb, settings_kb


router = Router()

#Расписание
@router.callback_query(lambda c: c.data == 'schedule_management')
async def schedule_management_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Управление расписанием:", reply_markup=schedule_management_kb
    )


#Клиенты
@router.callback_query(lambda c: c.data == 'clients')
async def clients_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Управление клиентами:', reply_markup=clients_kb
    )


#Записи
@router.callback_query(lambda c: c.data == 'records')
async def records_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Управлением записями:', reply_markup=records_kb
    )


@router.callback_query(lambda c: c.data == 'settings')
async def settings_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Управление настройками:', reply_markup=settings_kb
    )


#Назад
@router.callback_query(lambda c: c.data == 'back_to_main')
async def back_to_main_handler(callback_query: CallbackQuery):
    user_name = callback_query.from_user.full_name 
    await callback_query.message.edit_text(
        f'👩🏻 Добро пожаловать, {user_name}. Это Ваш кабинет для управления расписанием и записи клиентов\n'
        'Ссылка на кабинет для перехода клиентов: \n\n'
        'Возникли вопросы? Пишите @KandyBobby',
        reply_markup=master_panel_inline_kb
    )