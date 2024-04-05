import os
import tempfile
import sqlite3
import json

DB_PATH = os.path.join(tempfile.gettempdir(), 'database.db')

# Создание таблицы для хранения истории диалогов
def create_table():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS dialogs
                     (chat_id INTEGER PRIMARY KEY, history TEXT)""")
        conn.commit()
    finally:
        conn.close()

# Получение истории диалога для указанного chat_id
def get_dialog_history(chat_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT history FROM dialogs WHERE chat_id=?", (chat_id,))
        result = c.fetchone()
        history = json.loads(result[0]) if result else []
    finally:
        conn.close()
    return history

# Сохранение истории диалога для указанного chat_id
def save_dialog_history(chat_id, history):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        history_json = json.dumps(history)
        c.execute("INSERT OR REPLACE INTO dialogs (chat_id, history) VALUES (?, ?)", (chat_id, history_json))
        conn.commit()
    finally:
        conn.close()