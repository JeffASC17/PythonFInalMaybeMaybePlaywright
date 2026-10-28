from collections.abc import Callable

from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(
        self,
        page: Page,
        base_url: str,
        write_log: Callable[[str], None],
    ) -> None:
        super().__init__(page, base_url, write_log)
        self.automobile_link = page.get_by_role("link", name="Automobile", exact=True)

    def open_automobile_quote(self) -> None:
        self.browser_actions.click(self.automobile_link, "Automobile Link")
        self.page.wait_for_load_state("load")
