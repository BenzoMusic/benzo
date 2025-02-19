const TelegramBot = require('node-telegram-bot-api');

// Токен бота (вставь свой токен)
const token = '7836922267:AAEh99TfVahcs-Tfoqy8H8IYdfhprCIqWZ8';
const bot = new TelegramBot(token, { polling: true });

// URL вашего сайта (вставь свой URL)
const siteUrl = 'https://benzo-eight.vercel.app';

// Обработка сообщений
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    const text = msg.text;

    // Проверяем, является ли сообщение ссылкой
    if (text.match(/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/)) {
        // Отправляем пользователю ссылку на сайт с параметром
        const trackUrl = `${siteUrl}?track=${encodeURIComponent(text)}`;
        bot.sendMessage(chatId, `Слушайте трек: ${trackUrl}`);
    } else {
        bot.sendMessage(chatId, 'Пожалуйста, отправьте ссылку на трек.');
    }
});
