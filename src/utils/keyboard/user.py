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


schedule_management_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Создать')],
    ],
    resize_keyboard=True  
)