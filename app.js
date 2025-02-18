const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsDiv = document.getElementById('results');
const audioPlayer = document.getElementById('audio-player');

// Функция для поиска музыки
async function searchMusic(query) {
    const response = await fetch(`https://benzo-7l47.onrender.com/search?q=${query}`);
    const data = await response.json();
    return data;
}

// Обработчик кнопки поиска
searchButton.addEventListener('click', async () => {
    const query = searchInput.value;
    const results = await searchMusic(query);

    resultsDiv.innerHTML = ''; // Очищаем предыдущие результаты

    results.forEach(item => {
        // Создаем кнопку с заставкой и названием
        const resultButton = document.createElement('button');
        resultButton.className = 'result-button';
        
        // Устанавливаем заставку как фоновое изображение
        resultButton.style.backgroundImage = `url(${item.thumbnail})`;
        
        // Добавляем название поверх кнопки
        const title = document.createElement('div');
        title.className = 'result-title';
        title.textContent = item.title;
        resultButton.appendChild(title);

        // Обработчик клика по кнопке
        resultButton.addEventListener('click', () => {
            // Воспроизводим звук из видео
            audioPlayer.src = item.url;
            audioPlayer.play();
        });

        // Добавляем кнопку в контейнер результатов
        resultsDiv.appendChild(resultButton);
    });
});

// Инициализация Telegram Web App
Telegram.WebApp.ready();