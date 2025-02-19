from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# Замени на свой API-токен
BOT_TOKEN = '7836922267:AAEh99TfVahcs-Tfoqy8H8IYdfhprCIqWZ8'

# URL сервера (пока локальный)
SERVER_URL = 'http://localhost:5000'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я бот для синхронизации музыки. Используй /play чтобы начать."
    )

async def play(update: Update, context: CallbackContext):
    # Отправляем состояние плеера
    response = requests.get(f'{SERVER_URL}/get_state')
    state = response.json()
    await update.message.reply_text(
        f"Сейчас играет: {state['current_track']}\n"
        f"Состояние: {'Играет' if state['is_playing'] else 'На паузе'}"
    )

async def handle_message(update: Update, context: CallbackContext):
    # Обработка ссылок или файлов
    if update.message.audio:
        file_id = update.message.audio.file_id
        await update.message.reply_text(f"Аудио получено! ID: {file_id}")
    elif update.message.text and 'soundcloud.com' in update.message.text:
        await update.message.reply_text("Ссылка на SoundCloud получена!")
    else:
        await update.message.reply_text("Я не понимаю эту команду.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Регистрация обработчиков команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    # Запуск бота
    app.run_polling()