import asyncio
import logging
import os
from aiogram import Bot, Router, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN
from utils import process_message
from keep_alive import keep_alive
keep_alive()

# Инициализация бота
bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")

# Инициализация роутера
router = Router()

# Инициализация диспетчера
dp = Dispatcher()
dp.bot = bot
dp.include_router(router)

# Путь к файлу с изображением (относительно текущего каталога)
image_path = os.path.join('Default_A_serene_cityscape_at_dawn_the_calm_before_the_storm_0.jpg')

# Создание экземпляра InputFile
photo = types.FSInputFile(image_path)

# Обработчик команды /start
@router.message(Command('start'))
async def send_welcome(message: types.Message):
    try:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption="Привет👋, Я ИИ бот который может помочь тебе улучшить скилы и знания которые помогут выиграть дебаты🚀 Можешь начать разговор со мной и проверить как это работает😇 \n Удачи !",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[
                    types.InlineKeyboardButton(
                        text="Смотреть видео",
                        url="https://youtube.com/shorts/XySzMwLDQjY?feature=share"
                    )
                ]]
            )
        )
    except Exception as e:
        logging.error(f"Ошибка при отправке изображения: {e}")

# Обработчик всех остальных сообщений
@router.message()
async def handle_message(message: types.Message):
    try:
        response = process_message(message)
        await message.answer(response)
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")
        
@router.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f"Произошла ошибка: {exception}")
    return True
    
if __name__ == '__main__':
    from database import create_table
    create_table()

    # Получаем порт из переменной окружения PORT, если она существует, иначе используем 10000
    PORT = int(os.environ.get('PORT', 10000))

    # Запуск бота
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot, host='0.0.0.0', port=PORT))
