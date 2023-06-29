import os

import uvicorn

from src.core import get_screenshot
from src.models import RequestParams
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, Response


app = FastAPI()
API_TOKENS = ['L5ytMGZD6bvbzj4KfrKcasvy']


@app.get('/')
def say_hello():
    return 'it works!'


@app.post('/api/render/')
def render(
    request: Request,
    params: RequestParams
):
    if not (key := request.headers.get('x-api-key')) or not key in API_TOKENS:
        return Response(status_code=400, content='Bad api key')
    data, path, title = get_screenshot(params)
    return FileResponse(path=path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
