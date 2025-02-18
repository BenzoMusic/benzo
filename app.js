const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsDiv = document.getElementById('results');
const audioPlayer = document.getElementById('audio-player');

// Функция для поиска музыки
async function searchMusic(query) {
    const response = await fetch(`https://ваш-backend-урл/search?q=${query}`);
    const data = await response.json();
    return data;
}

// Обработчик кнопки поиска
searchButton.addEventListener('click', async () => {
    const query = searchInput.value;
    const results = await searchMusic(query);

    resultsDiv.innerHTML = ''; // Очищаем предыдущие результаты

    results.forEach(item => {
        const resultItem = document.createElement('div');
        resultItem.textContent = item.title;
        resultItem.addEventListener('click', () => {
            audioPlayer.src = item.url;
        });
        resultsDiv.appendChild(resultItem);
    });
});

// Инициализация Telegram Web App
Telegram.WebApp.ready();