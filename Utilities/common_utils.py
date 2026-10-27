from pathlib import Path

from BusinessMethods.datatypes import InsurantData, ProductData, VehicleData
from Utilities.csv_utils import CsvRow, read_csv


def required_value(row: CsvRow, key: str) -> str:
    value = row.get(key)
    if value is None or not value.strip():
        raise ValueError(f'Required CSV value "{key}" is missing')
    return value


def _first_record(file_path: str | Path) -> CsvRow:
    records = read_csv(file_path)
    return records[0]


def read_vehicle_data(file_path: str | Path) -> VehicleData:
    row = _first_record(file_path)
    return VehicleData(
        make=required_value(row, "make"),
        engine_performance=required_value(row, "enginePerformance"),
        date_of_manufacture=required_value(row, "dateOfManufacture"),
        number_of_seats=required_value(row, "numberOfSeats"),
        fuel_type=required_value(row, "fuelType"),
        list_price=required_value(row, "listPrice"),
        license_plate_number=required_value(row, "licensePlateNumber"),
        annual_mileage=required_value(row, "annualMileage"),
    )


def read_insurant_data(file_path: str | Path) -> InsurantData:
    row = _first_record(file_path)
    gender = required_value(row, "gender")
    if gender not in {"Male", "Female"}:
        raise ValueError(f"Unsupported insurant gender {gender!r}")
    return InsurantData(
        first_name=required_value(row, "firstName"),
        last_name=required_value(row, "lastName"),
        date_of_birth=required_value(row, "dateOfBirth"),
        gender=gender,
        street_address=required_value(row, "streetAddress"),
        country=required_value(row, "country"),
        zip_code=required_value(row, "zipCode"),
        city=required_value(row, "city"),
        occupation=required_value(row, "occupation"),
        hobbies=required_value(row, "hobbies"),
    )


def read_product_data(file_path: str | Path) -> ProductData:
    row = _first_record(file_path)
    return ProductData(
        start_date=required_value(row, "startDate"),
        insurance_sum=required_value(row, "insuranceSum"),
        merit_rating=required_value(row, "meritRating"),
        damage_insurance=required_value(row, "damageInsurance"),
        courtesy_car=required_value(row, "courtesyCar"),
        optional_products=required_value(row, "optionalProducts"),
    )
