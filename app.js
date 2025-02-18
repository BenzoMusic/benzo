const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsDiv = document.getElementById('results');
const audioPlayer = document.getElementById('audio-player');

let socket = null;

// Подключаемся к WebSocket
function connectWebSocket() {
    socket = new WebSocket(`wss://ваш-backend-урл/ws`);
    
    socket.onmessage = (event) => {
        const message = JSON.parse(event.data);
        if (message.type === "play") {
            audioPlayer.src = message.track.url;
            audioPlayer.play();
        }
    };
}

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
        const resultButton = document.createElement('button');
        resultButton.className = 'result-button';
        resultButton.style.backgroundImage = `url(${item.thumbnail})`;

        const title = document.createElement('div');
        title.className = 'result-title';
        title.textContent = item.title;
        resultButton.appendChild(title);

        resultButton.addEventListener('click', () => {
            if (socket) {
                socket.send(JSON.stringify({ type: "play", track: item }));
            }
        });

        resultsDiv.appendChild(resultButton);
    });
});

// Подключаемся к WebSocket при загрузке страницы
connectWebSocket();