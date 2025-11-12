from playwright.sync_api import expect


class BasePage:
    __BASE_URL = "https://m.twitch.tv"

    def __init__(self, page):
        self.page = page
        self._endpoint = ""
        self.page.on("dialog", lambda d: d.accept())

    def get_full_url(self):
        return f"{self.__BASE_URL}/{self._endpoint}"

    def navigate_to(self):
        full_url = self.get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state("load")
        self.accept_popup()
        expect(self.page).to_have_url(full_url)

    def wait_and_click(self, selector: str, timeout: int = 5000):
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        locator.click()

    def wait_and_press_enter(self, selector: str, timeout: int = 5000):
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        locator.press("Enter")

    def wait_and_fill(self, selector: str, value: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        self.page.fill(selector, value)

    def assert_element_is_visible(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        expect(self.page.locator(selector)).to_be_visible()

    def accept_popup(self, timeout=5000):
        try:
            self.page.locator("button:has-text('Accept')").click(timeout=timeout)
            self.page.locator("button:has-text('Start Watching')").click(timeout=timeout)
            self.page.on("dialog", lambda d: d.accept())
        except:
            pass

    def scroll_down(self, times: int, timeout=5000):
        for s in range(times):
            self.page.evaluate("window.scrollBy(0, window.innerHeight)")
            self.page.wait_for_timeout(timeout=timeout)

    def take_screenshot(self, screenshot_name, timeout=10000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        self.page.wait_for_selector("[data-a-target='video-player'], h2, h1", state="visible", timeout=timeout)
        self.page.screenshot(path=f"artifacts/screenshots/{screenshot_name}.png", timeout=timeout)
