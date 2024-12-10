from fastapi import FastAPI
from app.route import router  # Импортируем router вместо app

app = FastAPI()  # Создаем приложение FastAPI

# Подключаем маршруты из route.py
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в контейнерное приложение FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}