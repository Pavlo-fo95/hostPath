from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()  # Создаем экземпляр APIRouter

@router.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI App</title>
    </head>
    <body>
        <h1>Добро пожаловать в мое приложение!</h1>
    </body>
    </html>
    """

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}