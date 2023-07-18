import time
from playwright.sync_api import sync_playwright

from models import RequestParams


def get_browser(playwright, screenshot_format: str = 'png'):
    if screenshot_format == 'pdf':
        return playwright.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--exclude-switches=enable-automation',
            ]
        )
    else:
        return playwright.firefox.launch(headless=True)


def get_screenshot(params: RequestParams, screenshot_format: str = 'jpeg') -> tuple[str, str]:
    with sync_playwright() as playwright:
        browser = get_browser(playwright, screenshot_format)
        context = browser.new_context()
        context.add_cookies(params.get('cookies'))
        page = context.new_page()
        page.set_default_timeout(90000)
        page.goto(url=params.get('url'))
        print(len(page.content()))
        page.wait_for_load_state(state='networkidle')
        print(len(page.content()))
        page.locator('.overlay').wait_for(state='hidden')
        print(len(page.content()))
        res = make_screenshot(page=page, params=params, screenshot_format=screenshot_format)
        # ---------------------
        context.close()
        browser.close()
    return res


def make_screenshot(
        page,
        params: RequestParams,
        screenshot_format
) -> tuple[str, str]:
    path = f'screenshot.{screenshot_format}'
    match screenshot_format:
        case 'pdf':
            page.pdf(path=path, **params.get('pdf'))
        case 'png' | 'jpeg':
            page.screenshot(path=path, type=screenshot_format, full_page=True)
    return path
