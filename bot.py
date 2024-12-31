from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from datetime import datetime
import asyncio
import os

# Bot token
BOT_TOKEN = "8133212885:AAGyXSXVM5I3tSpBFz5nCnaUXUyHqnDNlmg"

# Special user IDs with associated messages and image filenames
SPECIAL_USERS = {
    137998265: ("Привет, Саша! Поздравляю тебя с Новым годом, всего наилучшего! Категорически рад быть, твоим братом и абсолютно искренне рад твоим прекрасным успехам в прошедшем году! Желаю тебе лишь больших успехов и наилучшего времяпровождения. Бери подарок номер 3, он твой по праву крови! ", "2.jpg"),
    318643868: ("Привет, Мама! Поздравляю тебя с Новым годом, я очень рад быть твоим сыном и быть воспитанным тобой, большое тебе за это спасибо, искренне надеюсь я являюсь хоть немного достойным, этого наследия, сыном. Желаю тебе всего наилучшего и максимально счастливого времяпровождения! Твой подарок номер 1 по праву! Передай, пожалуйста, конверты 4 и без номера их получателям!", "2.jpg"),
    172931785: ("Привет, Папа! Всего тебе наилучшего в этом году! С Новым годом! Категорически рад быть воспитанным тобой. Надеюсь не подвожу ожиданий. Желаю тебе прекрасного и счастливого времяпровождения и максимально доброй атмосферы. Твой подарок номер 2 по праву! Очень надеюсь на твоё хорошее отношение к этому подарку.", "2.jpg"),
    514749621: ("Я это я, или ты это ты?", "2.jpg"),
}

DEFAULT_MESSAGE = ("Ещё ведь старый год.. Куда ты меня зовешь?! посмотри на часы!", "1.jpg")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()

@router.message(Command("start"))
async def send_welcome(message: Message):
    user_id = message.from_user.id
    today = datetime.now()

    # Determine which image and message to send
    if today < datetime(2025, 1, 1):
        response_message, image_file = DEFAULT_MESSAGE
    else:
        response_message, image_file = SPECIAL_USERS.get(user_id, ("Ты кто!?", "1.jpg"))

    # Send the message
    await message.answer(response_message)

    # Send the image if it exists
    image_path = os.path.join(os.path.dirname(__file__), image_file)
    if os.path.exists(image_path):
        photo = FSInputFile(image_path)
        await message.answer_photo(photo)
    else:
        await message.answer("Ты кто!?")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
