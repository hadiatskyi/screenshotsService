from playwright.sync_api import sync_playwright

from models import RequestParams


def get_goto_params(params: RequestParams) -> dict:
    goto_params = {'url': params.get('url'), }
    if params.get('wait_until'):
        goto_params['wait_until'] = params.get('wait_until')
    if params.get('timeout'):
        goto_params['timeout'] = params.get('timeout')
    return goto_params


def get_screenshot(params: RequestParams):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies(params.get('cookies'))
        page = context.new_page()
        page.goto(**get_goto_params(params))
        page.wait_for_load_state(
            state=params.get('wait_until', 'networkidle'),
            timeout=params.get('timeout', 1000)
        )

        path = 'screenshot.{}'.format(params.get('output'))

        match params.get('output'):
            case 'pdf':
                result = page.pdf(path=path, **params.get('pdf'))
            case 'png' | 'jpeg':
                result = page.screenshot(path=path, **params.get('img').dict())
            case _:
                result = path = ''
        # ---------------------
        context.close()
        browser.close()
    return result, path
