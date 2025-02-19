from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь мне ссылку на SoundCloud, и я отправлю её тебе."
    )

# Обработчик для SoundCloud ссылок
async def handle_soundcloud_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text

    # Проверяем, является ли ссылка на SoundCloud
    if "soundcloud.com" in link:
        # Отправляем ссылку пользователю
        await update.message.reply_text(f"Вот твоя ссылка: {link}")
    else:
        await update.message.reply_text("Это не ссылка на SoundCloud. Пожалуйста, отправь правильную ссылку.")

# Инициализация приложения
app = ApplicationBuilder().token("7836922267:AAEh99TfVahcs-Tfoqy8H8IYdfhprCIqWZ8").build()

# Регистрируем обработчики
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_soundcloud_link))

# Функция для Vercel (обработка вебхуков)
async def vercel_handler(request):
    await app.initialize()
    await app.process_update(Update.de_json(await request.json(), app.bot))
    return {"status": "ok"}

# Локальный запуск (для тестирования)
if __name__ == '__main__':
    app.run_polling()
