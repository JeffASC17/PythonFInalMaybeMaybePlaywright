from collections.abc import Callable

from playwright.sync_api import Locator, Page

from BusinessMethods.datatypes import InsurantData
from pages.base_page import BasePage


class InsurantPage(BasePage):
    def __init__(
        self,
        page: Page,
        base_url: str,
        write_log: Callable[[str], None],
    ) -> None:
        super().__init__(page, base_url, write_log)
        self.first_name = page.locator("#firstname")
        self.last_name = page.locator("#lastname")
        self.birthdate = page.locator("#birthdate")
        self.street_address = page.locator("#streetaddress")
        self.country = page.locator("#country")
        self.zip_code = page.locator("#zipcode")
        self.city = page.locator("#city")
        self.occupation = page.locator("#occupation")
        self.next_to_product = page.locator("#nextenterproductdata")

    @property
    def first_name_field(self) -> Locator:
        return self.first_name

    def _gender(self, gender: str) -> Locator:
        return self.page.locator(f"label:has(#gender{gender.lower()})")

    def _hobby(self, hobby: str) -> Locator:
        hobby_id = hobby.lower().replace(" ", "")
        return self.page.locator(f"label:has(#{hobby_id})")

    def enter_insurant(self, data: InsurantData) -> None:
        actions = self.browser_actions
        actions.fill(self.first_name, data.first_name, "First Name")
        actions.fill(self.last_name, data.last_name, "Last Name")
        actions.fill(self.birthdate, data.date_of_birth, "Date of Birth")
        actions.click(self._gender(data.gender), "Gender")
        actions.fill(self.street_address, data.street_address, "Street Address")
        actions.select(self.country, data.country, "Country")
        actions.fill(self.zip_code, data.zip_code, "Zip Code")
        actions.fill(self.city, data.city, "City")
        actions.select(self.occupation, data.occupation, "Occupation")
        for hobby in (item.strip() for item in data.hobbies.split("-")):
            actions.click(self._hobby(hobby), f"{hobby} of Hobbies")

    def continue_to_product(self) -> None:
        self.browser_actions.click(self.next_to_product, "Next to Product Data")
