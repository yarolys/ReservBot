from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from datetime import datetime, timedelta

import locale

from src.utils.keyboard.user import schedule_management_kb


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
router = Router()
selected_dates = {}


def generate_calendar(selected_date: datetime, user_dates: dict):
    year_month = selected_date.strftime("%Y-%m")
    selected_days = user_dates.get(year_month, set())
    start_date = selected_date.replace(day=1)
    end_date = (start_date + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    inline_keyboard = [[InlineKeyboardButton(text=day, callback_data="ignore") for day in days_of_week]]
    day_buttons = []
    for day in range(1, end_date.day + 1):
        current_date = start_date.replace(day=day)
        day_text = f"{day}✔️" if day in selected_days else str(day)
        if current_date < datetime.now():
            day_buttons.append(InlineKeyboardButton(text=" ", callback_data="ignore"))
        else:
            day_buttons.append(InlineKeyboardButton(text=day_text, callback_data=f"toggle_day:{year_month}:{day}"))
    for i in range(0, len(day_buttons), 7):
        inline_keyboard.append(day_buttons[i:i + 7])
    current_month_year = selected_date.strftime("%B %Y").capitalize()
    inline_keyboard.insert(0, [
        InlineKeyboardButton(text="◀️", callback_data=f"change_month:{(selected_date - timedelta(days=1)).strftime('%Y-%m')}"),
        InlineKeyboardButton(text=current_month_year, callback_data="ignore"),
        InlineKeyboardButton(text="▶️", callback_data=f"change_month:{(selected_date + timedelta(days=31)).strftime('%Y-%m')}")
    ])

    inline_keyboard.append([
        InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel"),
        InlineKeyboardButton(text="👍 Готово", callback_data="confirm")
    ])

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard


@router.callback_query(lambda c: c.data == "create")
async def handle_create(callback_query: CallbackQuery):
    today = datetime.now()
    user_id = callback_query.from_user.id
    selected_dates[user_id] = {}  #
    keyboard = generate_calendar(today, selected_dates[user_id])
    await callback_query.message.edit_text("Выберите даты:", reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("toggle_day:"))
async def handle_day_toggle(callback_query: CallbackQuery):
    _, year_month, day = callback_query.data.split(":")
    selected_day = int(day)
    user_id = callback_query.from_user.id
    if user_id not in selected_dates:
        selected_dates[user_id] = {}
    if year_month not in selected_dates[user_id]:
        selected_dates[user_id][year_month] = set()
    if selected_day in selected_dates[user_id][year_month]:
        selected_dates[user_id][year_month].remove(selected_day)
    else:
        selected_dates[user_id][year_month].add(selected_day)
    selected_date = datetime.strptime(year_month, "%Y-%m")
    keyboard = generate_calendar(selected_date, selected_dates[user_id])
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("change_month:"))
async def handle_month_change(callback_query: CallbackQuery):
    year, month = map(int, callback_query.data.split(":")[1].split("-"))
    new_date = datetime(year, month, 1)
    user_id = callback_query.from_user.id

    if user_id not in selected_dates:
        selected_dates[user_id] = {}
    keyboard = generate_calendar(new_date, selected_dates[user_id])
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "confirm")
async def handle_confirm(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user_dates = selected_dates.get(user_id, {})
    chosen_dates = []
    for year_month, days in user_dates.items():
        for day in sorted(days):
            chosen_dates.append(f"{day} {year_month}")
    if chosen_dates:
        chosen_dates_str = ", ".join(chosen_dates)
        await callback_query.message.answer(f"Вы выбрали следующие даты: {chosen_dates_str}",
                                            reply_markup=schedule_management_kb)
    else:
        await callback_query.message.answer("Вы не выбрали ни одной даты.",
                                            reply_markup=schedule_management_kb)



@router.callback_query(lambda c: c.data == "cancel")
async def handle_cancel(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    selected_dates.pop(user_id, None)
    await callback_query.message.edit_text(
    text="Вы вернулись в главное меню управления расписанием:",
    reply_markup=schedule_management_kb
    )
