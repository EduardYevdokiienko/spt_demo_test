import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage


@pytest.fixture(scope="session")
def page():
    playwright = sync_playwright().start()
    pixel_7 = playwright.devices["Pixel 7"]
    browser = playwright.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context(**pixel_7)
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()

@pytest.fixture()
def main_page(page):
    return MainPage(page)

@pytest.fixture()
def search_page(page):
    return SearchPage(page)

@pytest.fixture()
def streamer_page(page):
    return StreamerPage(page, endpoint="")
