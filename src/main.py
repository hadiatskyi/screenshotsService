import os

import uvicorn

from core import get_screenshot
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, Response
from models import RequestParams


app = FastAPI()
API_TOKENS = ['L5ytMGZD6bvbzj4KfrKcasvy']
DEFAULT_FORMAT = str(os.getenv('DEFAULT_SCREENSHOT_FORMAT') or 'pdf')


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

    path = get_screenshot(params, DEFAULT_FORMAT)
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
{"timeout": 30000, "wait_until": "networkidle", "output": "pdf", "pdf": {"landscape": true,"scale": 0.5}, "cookies": [{"name": "sessionid", "value": "bszjm6g1h178on96mbtafn07vud64mbe", "domain": "millcorp.tst.graintrack.com", "path": "/"}, {"name": "csrftoken", "value": "lr8iLe59TgUTBSW74cO1V0FHeXWjTUlbYAX2QrNorB2FVwK9f8OPL8Swlw5Qeiit", "domain": "millcorp.tst.graintrack.com", "path": "/"}], "url": "https://millcorp.tst.graintrack.com/#/reports/invoice-risk-report?start_date=01.01.2022&end_date=31.12.2023&predicate=invoice_date&position_use_list=cargo&group_by=vessel_name&has_balance=1&currency_list=1&currency_list=3"}
