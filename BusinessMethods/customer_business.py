from BusinessMethods.datatypes import InsurantData, ProductData, VehicleData
from pages.insurant_page import InsurantPage
from pages.product_page import ProductPage
from pages.vehicle_page import VehiclePage


class CustomerBusiness:
    def __init__(
        self,
        vehicle_page: VehiclePage,
        insurant_page: InsurantPage,
        product_page: ProductPage,
    ) -> None:
        self.vehicle_page = vehicle_page
        self.insurant_page = insurant_page
        self.product_page = product_page

    def enter_vehicle(self, data: VehicleData) -> None:
        self.vehicle_page.enter_vehicle(data)

    def enter_insurant(self, data: InsurantData) -> None:
        self.insurant_page.enter_insurant(data)

    def enter_product(self, data: ProductData) -> None:
        self.product_page.enter_product(data)
