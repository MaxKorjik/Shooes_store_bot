import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hello! The bot is officially running.")

@dp.message()
async def say_something(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    logging.basicConfig(level=logging.INFO)
    
    print("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
        
