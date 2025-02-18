const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsDiv = document.getElementById('results');
const audioPlayer = document.getElementById('audio-player');

// Функция для поиска музыки
async function searchMusic(query) {
    if (!query) {
        alert("Введите запрос для поиска");
        return;
    }

    try {
        const response = await fetch(`https://benzo-7l47.onrender.com/search?q=${query}`);
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Ошибка при выполнении запроса:", error);
        return [];
    }
}

// Обработчик кнопки поиска
searchButton.addEventListener('click', async () => {
    const query = searchInput.value;
    const results = await searchMusic(query);

    resultsDiv.innerHTML = ''; // Очищаем предыдущие результаты

    results.forEach(item => {
        if (!item.url) {
            console.error("Некорректные данные:", item);
            return;
        }

        // Создаем кнопку с заставкой и названием
        const resultButton = document.createElement('button');
        resultButton.className = 'result-button';

        // Устанавливаем заставку (если есть) или используем заглушку
        const thumbnail = item.thumbnail || "https://via.placeholder.com/150";
        resultButton.style.backgroundImage = `url(${thumbnail})`;

        // Добавляем название поверх кнопки
        const title = document.createElement('div');
        title.className = 'result-title';
        title.textContent = item.title;
        resultButton.appendChild(title);

        // Обработчик клика по кнопке
        resultButton.addEventListener('click', () => {
            if (item.url) {
                audioPlayer.src = item.url;
                audioPlayer.play();
            } else {
                console.error("URL для воспроизведения не найден");
            }
        });

        // Добавляем кнопку в контейнер результатов
        resultsDiv.appendChild(resultButton);
    });
});