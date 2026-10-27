from collections.abc import Callable

from playwright.sync_api import Locator, Page

from BusinessMethods.datatypes import ProductData
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(
        self,
        page: Page,
        base_url: str,
        capture_screenshot: Callable[[str], None],
        write_log: Callable[[str], None],
    ) -> None:
        super().__init__(page, base_url, capture_screenshot, write_log)
        self.start_date = page.locator("#startdate")
        self.insurance_sum = page.locator("#insurancesum")
        self.merit_rating = page.locator("#meritrating")
        self.damage_insurance = page.locator("#damageinsurance")
        self.courtesy_car = page.locator("#courtesycar")
        self.next_to_price_option_button = page.locator("#nextselectpriceoption")

    @property
    def start_date_field(self) -> Locator:
        return self.start_date

    def _optional_product(self, product: str) -> Locator:
        product_id = product.replace(" ", "")
        return self.page.locator(f"label:has(#{product_id})")

    def enter_product(self, data: ProductData) -> None:
        actions = self.browser_actions
        actions.fill(self.start_date, data.start_date, "Start Date")
        actions.select(self.insurance_sum, data.insurance_sum, "Insurance Sum")
        actions.select(self.merit_rating, data.merit_rating, "Merit Rating")
        actions.select(self.damage_insurance, data.damage_insurance, "Damage Insurance")
        for product in (item.strip() for item in data.optional_products.split("-")):
            actions.click(self._optional_product(product), f"{product} of Optional Products")
        actions.select(self.courtesy_car, data.courtesy_car, "Courtesy Car")

    def continue_to_price_option(self) -> None:
        self.browser_actions.click(self.next_to_price_option_button, "Next to Price Option")
