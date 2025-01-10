from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


admin_panel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Посмотреть приветственное сообщение')],
        [KeyboardButton(text='Отредактировать приветственное сообщение')]
    ],
    resize_keyboard=True
)

