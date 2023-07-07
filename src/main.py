import os

import uvicorn

from core import get_screenshot
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, Response
from models import RequestParams


app = FastAPI()
API_TOKENS = ['L5ytMGZD6bvbzj4KfrKcasvy']
DEFAULT_FORMAT = str(os.getenv('DEFAULT_SCREENSHOT_FORMAT')or 'png')


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

    path, title = get_screenshot(params, DEFAULT_FORMAT)
    return FileResponse(path=path)


@app.post('/api/render-pdf/')
def render(
    request: Request,
    params: RequestParams
):
    if not (key := request.headers.get('x-api-key')) or not key in API_TOKENS:
        return Response(status_code=400, content='Bad api key')
    path, title = get_screenshot(params, 'jpeg')
    return FileResponse(path=path)


@app.post('/api/render-png/')
def render(
    request: Request,
    params: RequestParams
):
    if not (key := request.headers.get('x-api-key')) or not key in API_TOKENS:
        return Response(status_code=400, content='Bad api key')
    path, title = get_screenshot(params, 'png')
    return FileResponse(path=path)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
