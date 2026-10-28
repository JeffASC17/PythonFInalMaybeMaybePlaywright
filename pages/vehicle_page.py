from collections.abc import Callable

from playwright.sync_api import Locator, Page

from BusinessMethods.datatypes import VehicleData
from pages.base_page import BasePage


class VehiclePage(BasePage):
    def __init__(
        self,
        page: Page,
        base_url: str,
        write_log: Callable[[str], None],
    ) -> None:
        super().__init__(page, base_url, write_log)
        self.make = page.locator("#make")
        self.engine_performance = page.locator("#engineperformance")
        self.date_of_manufacture = page.locator("#dateofmanufacture")
        self.number_of_seats = page.locator("#numberofseats")
        self.fuel_type = page.locator("#fuel")
        self.list_price = page.locator("#listprice")
        self.license_plate_number = page.locator("#licenseplatenumber")
        self.annual_mileage = page.locator("#annualmileage")
        self.next_to_insurant_button = page.locator("#nextenterinsurantdata")

    @property
    def make_field(self) -> Locator:
        return self.make

    def enter_vehicle(self, data: VehicleData) -> None:
        actions = self.browser_actions
        actions.select(self.make, data.make, "Make")
        actions.fill(self.engine_performance, data.engine_performance, "Engine Performance")
        actions.fill(self.date_of_manufacture, data.date_of_manufacture, "Date of Manufacture")
        actions.select(self.number_of_seats, data.number_of_seats, "Number of Seats")
        actions.select(self.fuel_type, data.fuel_type, "Fuel Type")
        actions.fill(self.list_price, data.list_price, "List Price")
        actions.fill(self.license_plate_number, data.license_plate_number, "License Plate Number")
        actions.fill(self.annual_mileage, data.annual_mileage, "Annual Mileage")

    def continue_to_insurant(self) -> None:
        self.browser_actions.click(self.next_to_insurant_button, "Next to Insurant Data")
