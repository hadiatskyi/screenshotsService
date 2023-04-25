from src.core import get_screenshot
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post('/api/render/')
def create_item(params: dict):
    data, path = get_screenshot(params)
    return FileResponse(path=path)
