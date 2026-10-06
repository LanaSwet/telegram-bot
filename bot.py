import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "8749375471:AAEbqlmVC4nnfrCeeBMvO8EcgUVJKmrM4MU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
