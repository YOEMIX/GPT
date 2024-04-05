import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Токен Telegram бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Ключ API OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Путь к базе данных SQLite
DB_PATH = 'data/database.db'