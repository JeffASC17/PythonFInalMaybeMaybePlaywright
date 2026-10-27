import tempfile
import unittest
from pathlib import Path

from Utilities.common_utils import read_product_data, read_vehicle_data
from Utilities.csv_utils import read_csv

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class CsvUtilsTests(unittest.TestCase):
    def test_reads_quoted_comma_in_product_value(self) -> None:
        product = read_product_data(PROJECT_ROOT / "Data" / "ProductData.csv")
        self.assertEqual(product.insurance_sum, "3.000.000,00")

    def test_reads_vehicle_record(self) -> None:
        vehicle = read_vehicle_data(PROJECT_ROOT / "Data" / "VehicleData.csv")
        self.assertEqual(vehicle.make, "Audi")
        self.assertEqual(vehicle.annual_mileage, "10000")

    def test_rejects_rows_with_wrong_field_count(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            csv_path = Path(temporary_directory) / "invalid.csv"
            csv_path.write_text("first,second\none\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "expected 2"):
                read_csv(csv_path)

    def test_rejects_duplicate_headers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            csv_path = Path(temporary_directory) / "invalid.csv"
            csv_path.write_text("first,first\none,two\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate header"):
                read_csv(csv_path)


if __name__ == "__main__":
    unittest.main()
