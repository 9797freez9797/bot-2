import os
import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from decouple import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
    
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = 'Привіт!\n' \
           'Яку картинку хочеш побачити?'
    await message.reply(text)

@dp.message_handler()
async def echo(message: types.Message):
    text = message.text.lower()

    if 'картинки' in text:
        if 'люди' in text:
            list_of_photos = os.listdir('photos/People')
            photo = random.choice(list_of_photos)
            await message.answer_photo(types.InputFile(f'photos/People/{photo}'), caption='Люди')
        elif 'космос' in text:
            list_of_photos = os.listdir('photos/Space')
            photo = random.choice(list_of_photos)
            await message.answer_photo(types.InputFile(f'photos/Space/{photo}'), caption='Космос')
        elif 'природа' in text:
            list_of_photos = os.listdir('photos/Nature')
            photo = random.choice(list_of_photos)
            await message.answer_photo(types.InputFile(f'photos/Nature/{photo}'), caption='Природа')
        else:
            await message.reply("Вибачте, я не розумію цю категорію.")
    else:
        await message.reply("Вибачте, я не розумію вашого повідомлення.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)