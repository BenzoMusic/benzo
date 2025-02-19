const express = require('express');
const app = express();

// Указываем папку со статическими файлами (index.html)
app.use(express.static('public'));

// Запуск сервера
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Сайт запущен на http://localhost:${port}`);
});
