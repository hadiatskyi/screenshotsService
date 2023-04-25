
from playwright.sync_api import sync_playwright


def get_screenshot(params: dict):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        if params.get('cookies'):
            context.add_cookies(params.get('cookies'))
        page = context.new_page()
        page.goto(params.get('url'), **params.get('goto'))
        match type := params.get('output', 'pdf'):
            case 'pdf':
                path = 'screenshot.pdf'
                result = page.pdf(path=path, **params.get('pdf'))
            case 'png' | 'jpeg':
                path = f'screenshot.{type}'
                result = page.screenshot(path=path, full_page=True, type=type)
            case _:
                result = path = ''
        # ---------------------
        context.close()
        browser.close()
    return result, path
