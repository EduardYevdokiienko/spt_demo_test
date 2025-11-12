from pages.base_page import BasePage


class MainPage(BasePage):
    MAIN_LOGO = "//a[@aria-label='Go to the Twitch home page']"
    SEARCH_BUTTON = "//a[2]"

    def __init__(self, page):
        super().__init__(page)
        self.endpoint = ""

    def open(self):
        return self.navigate_to()

    def expect_page_is_opened(self):
        self.assert_element_is_visible(self.MAIN_LOGO)

    def click_search_icon(self):
        self.wait_and_click(self.SEARCH_BUTTON)
