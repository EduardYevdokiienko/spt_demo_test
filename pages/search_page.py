from urllib.parse import urlparse

from pages.base_page import BasePage
from pages.streamer_page import StreamerPage


class SearchPage(BasePage):
    SEARCH_INPUT = "//input[@placeholder='Search']"
    STREAMER_ONE = "(//button)[2]" # fallback


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'directory'

    def open(self):
        return self.navigate_to()

    def expect_page_is_opened(self):
        self.assert_element_is_visible(self.SEARCH_INPUT)

    def input_value_and_search_(self, value: str):
        self.wait_and_fill(self.SEARCH_INPUT, value)
        self.wait_and_press_enter(self.SEARCH_INPUT)

    def scroll_down_times_(self, times: int):
        self.scroll_down(times)

    def choose_streamer_(self, number: str =2) -> StreamerPage:
        self.wait_and_click(f"(//button)[{number}]")
        self.page.wait_for_load_state("networkidle")
        path = urlparse(self.page.url).path
        streamer_endpoint = path.lstrip("/")
        return StreamerPage(self.page, streamer_endpoint)
