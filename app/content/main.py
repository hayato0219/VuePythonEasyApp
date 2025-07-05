from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str

app = FastAPI()

DICEBEAR_API_URL = "https://api.dicebear.com/7.x"

@app.get("/api")
def api_root():
    return {"Hello": "World"}

@app.post("/api/greetings")
def greetings(user: User):
    return {
        "message": f"こんにちは{user.name}さん"
    }

@app.get("/api/avatar/{name}")
async def get_avatar(name: str):
    avatar_url = f"{DICEBEAR_API_URL}/pixel-art/svg?seed={name}"
    return {"name": name, "avatar_url": avatar_url}