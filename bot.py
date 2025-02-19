import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# URL сервера
SERVER_URL = 'https://benzo-7l47.onrender.com'

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь мне ссылку на SoundCloud, и я добавлю её в список."
    )

# Обработчик для SoundCloud ссылок
async def handle_soundcloud_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    link = update.message.text

    # Проверяем, является ли ссылка на SoundCloud
    if "soundcloud.com" in link:
        # Отправляем ссылку на сервер
        response = requests.post(f'{SERVER_URL}/add_link', json={"user_id": user_id, "link": link})
        if response.status_code == 200:
            await update.message.reply_text(f"Ссылка добавлена: {link}")
        else:
            await update.message.reply_text("Ошибка при добавлении ссылки.")
    else:
        await update.message.reply_text("Это не ссылка на SoundCloud. Пожалуйста, отправь правильную ссылку.")

# Обработчик для удаления ссылок при выходе пользователя
async def clear_links_on_exit(user_id: str):
    response = requests.post(f'{SERVER_URL}/clear_links', json={"user_id": user_id})
    if response.status_code == 200:
        print(f"Ссылки для пользователя {user_id} очищены.")
    else:
        print(f"Ошибка при очистке ссылок для пользователя {user_id}.")

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token("7836922267:AAEh99TfVahcs-Tfoqy8H8IYdfhprCIqWZ8").build()

    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_soundcloud_link))

    # Запускаем бота
    app.run_polling()
