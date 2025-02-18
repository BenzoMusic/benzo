from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

# Создаем приложение FastAPI
app = FastAPI()

# Настройка CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы со всех доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Твой YouTube API Key
YOUTUBE_API_KEY = "AIzaSyBMnIF_OLDZ93uAOgUOSzZHPXOcefSzFXY"

# Маршрут для поиска музыки
@app.get("/search")
async def search(q: str):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&key={YOUTUBE_API_KEY}&type=video"
    response = requests.get(url)
    data = response.json()
    
    results = [
        {
            "title": item["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"]  # Добавляем заставку
        }
        for item in data["items"]
    ]
    return results
async def search(q: str):
    # Формируем URL для запроса к YouTube API
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&key={YOUTUBE_API_KEY}&type=video"
    
    # Выполняем запрос к YouTube API
    response = requests.get(url)
    
    # Если запрос успешен, обрабатываем данные
    if response.status_code == 200:
        data = response.json()
        
        # Формируем список результатов
        results = [
            {
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            for item in data["items"]
        ]
        
        return results
    else:
        # Если запрос не удался, возвращаем ошибку
        return {"error": "Не удалось выполнить запрос к YouTube API"}