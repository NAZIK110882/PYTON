import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
import database

async def main():
    await database.init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    
    print("Бот успішно запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())