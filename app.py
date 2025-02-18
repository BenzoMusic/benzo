from fastapi import FastAPI
import requests

app = FastAPI()

YOUTUBE_API_KEY = "ваш_youtube_api_ключ"

@app.get("/search")
async def search(q: str):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&key={YOUTUBE_API_KEY}&type=video"
    response = requests.get(url)
    data = response.json()
    results = [{"title": item["snippet"]["title"], "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"} for item in data["items"]]
    return results