import asyncio

from aiogram import Dispatcher
from src.config import bot, logger
from src.handlers import (
    start_router,
    admin_panel_router,

)

async def main():
    dp = Dispatcher()
    dp.include_routers(
        start_router,
        admin_panel_router,
    )
    r = await bot.get_me()
    logger.info(f"Бот запущен: https://t/me/{r.username}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())