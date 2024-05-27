import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import handlers as hd


TOKEN = '7489342817:AAFJ5tXq6eBpbqlnqH-KYUt5mJ4z-LOnqc8'
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(hd.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
