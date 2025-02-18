from fastapi import FastAPI, WebSocket
from youtube_dl import YoutubeDL
import json
import asyncio

app = FastAPI()

# Глобальные переменные для синхронизации
current_track = None
clients = []

# Функция для поиска музыки
def search_music(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "extract_flat": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"]
    return [
        {
            "title": item["title"],
            "url": item["url"],
            "thumbnail": item["thumbnail"]
        }
        for item in results
    ]

# Маршрут для поиска музыки
@app.get("/search")
async def search(q: str):
    results = search_music(q)
    return results

# WebSocket для синхронизации
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message["type"] == "play":
                global current_track
                current_track = message["track"]
                
                # Отправляем текущий трек всем клиентам
                for client in clients:
                    await client.send_text(json.dumps({"type": "play", "track": current_track}))
    except Exception as e:
        clients.remove(websocket)
        print(f"Ошибка: {e}")