from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import requests
import os

# Замени на свой API-токен
BOT_TOKEN = '7836922267:AAEh99TfVahcs-Tfoqy8H8IYdfhprCIqWZ8'

# URL сервера (пока локальный)
SERVER_URL = 'https://benzo-7l47.onrender.com'  # Поменяй на Render URL после деплоя

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я бот для синхронизации музыки. Отправь мне аудиофайл или ссылку на SoundCloud."
    )

async def handle_message(update: Update, context: CallbackContext):
    # Обработка аудиофайлов
    if update.message.audio:
        file_id = update.message.audio.file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path

        # Добавляем трек на сервер
        track_data = {
            "id": file_id,
            "title": update.message.audio.title or "Без названия",
            "artist": update.message.audio.performer or "Неизвестный исполнитель",
            "url": file_url
        }
        response = requests.post(f'{SERVER_URL}/add_track', json=track_data)
        if response.status_code == 200:
            await update.message.reply_text(f"Трек добавлен: {track_data['title']}")
        else:
            await update.message.reply_text("Ошибка при добавлении трека.")

    # Обработка ссылок на SoundCloud (позже)
    elif update.message.text and 'soundcloud.com' in update.message.text:
        await update.message.reply_text("Ссылка на SoundCloud будет обработана позже.")
    else:
        await update.message.reply_text("Отправь мне аудиофайл или ссылку на SoundCloud.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.run_polling()
