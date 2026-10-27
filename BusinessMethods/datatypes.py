from dataclasses import dataclass


@dataclass(frozen=True)
class VehicleData:
    make: str
    engine_performance: str
    date_of_manufacture: str
    number_of_seats: str
    fuel_type: str
    list_price: str
    license_plate_number: str
    annual_mileage: str


@dataclass(frozen=True)
class InsurantData:
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    street_address: str
    country: str
    zip_code: str
    city: str
    occupation: str
    hobbies: str


@dataclass(frozen=True)
class ProductData:
    start_date: str
    insurance_sum: str
    merit_rating: str
    damage_insurance: str
    courtesy_car: str
    optional_products: str
