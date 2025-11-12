from pages.base_page import BasePage


class StreamerPage(BasePage):

    def __init__(self, page, endpoint: str):
        super().__init__(page)
        self._endpoint = endpoint

    def take_screenshot_of_streamer(self, text: str):
        self.page.wait_for_load_state("networkidle")
        self.take_screenshot(text)
