from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import (
    KeyboardButton, 
    ReplyKeyboardMarkup, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)


master_panel_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='🗓 Управление расписанием', callback_data='schedule_management')],

        [
        InlineKeyboardButton(text='👥 Клиенты', callback_data='clients'),
        InlineKeyboardButton(text='📝 Записи', callback_data='records'),
        ],

        [
        InlineKeyboardButton(text='📅 Сегодня', callback_data='today'),
        InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings'),
        ],
    ]
)


schedule_management_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='✏️ Создать', callback_data='create'),
        InlineKeyboardButton(text='📖 Просмотреть', callback_data='check'),
        ],
        [
        InlineKeyboardButton(text='🗑 Удалить', callback_data='delete'),
        InlineKeyboardButton(text='📝 Редактировать день', callback_data='redact_day'),
        ],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_main')],
    ]
)

clients_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='✏️Добавить', callback_data='add'),
        InlineKeyboardButton(text='📝 Изменить', callback_data='change'),
        ],
        [
        InlineKeyboardButton(text='✏️Добавить и записать', callback_data='add_and_write'),
        ],
        [
        InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_main'),    
        ]
    ]
)

records_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='📝 Записать', callback_data='recording'),
        InlineKeyboardButton(text='😢 Отменить', callback_data='cancel'),
        ],
        [
        InlineKeyboardButton(text='📖 Просмотреть', callback_data='check_all_recordings'),
        InlineKeyboardButton(text='📚 На неделю', callback_data='check_week_recordings'),
        ],
        [
        InlineKeyboardButton(text='📝 Записать нового клиента', callback_data='record_new_client'),
        ],
        [
        InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_main'),    
        ],
    ]
)

settings_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='⚡️ Информация', callback_data='info'),
        InlineKeyboardButton(text='💼 Кабинет', callback_data='personal_account'),
        ],
        [
        InlineKeyboardButton(text='🗣 Услуги', callback_data='services'),
        InlineKeyboardButton(text='📖 О сервисе', callback_data='about_service'),
        ],
        [
        InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_main'),    
        ],
    ]
)