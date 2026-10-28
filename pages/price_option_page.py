from collections.abc import Callable

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class PriceOptionPage(BasePage):
    def __init__(
        self,
        page: Page,
        base_url: str,
        write_log: Callable[[str], None],
    ) -> None:
        super().__init__(page, base_url, write_log)
        self.price_option_table = page.locator("#priceTable")

    @property
    def price_table(self) -> Locator:
        return self.price_option_table
