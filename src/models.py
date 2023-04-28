from playwright._impl._api_structures import SetCookieParam, PdfMargins, FloatRect

from typing import Literal, Optional, TypedDict, Union, List
import pathlib


class PDFParams(TypedDict, total=False):
    scale: Optional[float] = 1.0
    display_header_footer: Optional[bool] = None
    header_template: Optional[str] = None
    footer_template: Optional[str] = None
    print_background: Optional[bool] = None
    landscape: Optional[bool] = None
    page_ranges: Optional[str] = None
    format: Optional[str] = None
    width: Optional[Union[str, float]] = None
    height: Optional[Union[str, float]] = None
    prefer_css_page_size: Optional[bool] = None
    margin: Optional[PdfMargins] = None
    path: Optional[Union[str, pathlib.Path]] = None


class ImgParams(TypedDict, total=False):
    timeout: Optional[float] = None
    type: Optional[Literal["jpeg", "png"]] = None
    path: Optional[Union[str, pathlib.Path]] = None
    quality: Optional[int] = None
    omit_background: Optional[bool] = None
    full_page: Optional[bool] = True
    clip: Optional[FloatRect] = None
    animations: Optional[Literal["allow", "disabled"]] = None
    caret: Optional[Literal["hide", "initial"]] = None
    scale: Optional[Literal["css", "device"]] = None
    mask: Optional[List["Locator"]] = None


class RequestParams(TypedDict, total=False):
    url: str = ''
    cookies: list[SetCookieParam]
    pdf: Optional[PDFParams] = None
    img: Optional[ImgParams] = None
    output: Literal['pdf', 'png', 'load', 'jpeg'] = None
    timeout: Optional[float] = None
    wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None
