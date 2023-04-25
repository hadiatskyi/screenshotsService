from src.core import get_screenshot

REQUEST_BODY = {
    "url": "https://f4.graintrack.com/#/logistics/voyages?show_uncompleted=1&page=1",
    "waitFor": "6000",
    "goto": {"wait_until": "networkidle"},
    "output": "pdf",
    "pdf": {"landscape": True, "scale": 0.50},
    "cookies": [
        {
            "name": "sessionid",
            "value": "6p26atjsfgjd1wwnsahj3izdtoll3cu9",
            "domain": "f4.graintrack.com",
            'path': '/',
        },
        {
            "name": "csrftoken",
            "value": "Mwo9LG2OAMavftwFD2Zg2Jj1KH7y5IZXyd8allxDehISGDMMW4o0ww6HQWbZKaZt",
            "domain": "f4.graintrack.com",
            'path': '/',
}
    ]
}


get_screenshot(REQUEST_BODY)
