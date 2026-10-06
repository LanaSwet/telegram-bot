import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "8749375471:AAGVr_9jxFvM_DXISPAptX0kmmLO2NJoD8o"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
