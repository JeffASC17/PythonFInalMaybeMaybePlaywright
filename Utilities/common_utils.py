from pathlib import Path

from BusinessMethods.datatypes import InsurantData, ProductData, VehicleData
from Utilities.csv_utils import CsvRow, read_csv


def required_value(row: CsvRow, key: str) -> str:
    value = row.get(key)
    if value is None or not value.strip():
        raise ValueError(f'Required CSV value "{key}" is missing')
    return value


def _record_for_test_case(file_path: str | Path, test_case: str) -> CsvRow:
    records = read_csv(file_path)
    matches = [record for record in records if record.get("TestCase") == test_case]
    if not matches:
        raise ValueError(f'Test case "{test_case}" was not found in {file_path}')
    if len(matches) > 1:
        raise ValueError(f'Test case "{test_case}" appears more than once in {file_path}')
    return matches[0]


def read_vehicle_data(file_path: str | Path, test_case: str) -> VehicleData:
    row = _record_for_test_case(file_path, test_case)
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


def read_insurant_data(file_path: str | Path, test_case: str) -> InsurantData:
    row = _record_for_test_case(file_path, test_case)
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


def read_product_data(file_path: str | Path, test_case: str) -> ProductData:
    row = _record_for_test_case(file_path, test_case)
    return ProductData(
        start_date=required_value(row, "startDate"),
        insurance_sum=required_value(row, "insuranceSum"),
        merit_rating=required_value(row, "meritRating"),
        damage_insurance=required_value(row, "damageInsurance"),
        courtesy_car=required_value(row, "courtesyCar"),
        optional_products=required_value(row, "optionalProducts"),
    )
