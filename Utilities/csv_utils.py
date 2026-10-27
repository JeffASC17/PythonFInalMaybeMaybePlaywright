import csv
from pathlib import Path
from typing import TypeAlias

CsvRow: TypeAlias = dict[str, str]


def read_csv(path: str | Path) -> list[CsvRow]:
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        rows = [row for row in csv.reader(csv_file) if row]

    if len(rows) < 2:
        raise ValueError(f"CSV must contain a header and at least one data row: {csv_path}")

    headers = [header.strip() for header in rows[0]]
    if any(not header for header in headers) or len(set(headers)) != len(headers):
        raise ValueError(f"CSV contains an empty or duplicate header: {csv_path}")

    records: list[CsvRow] = []
    for row_number, values in enumerate(rows[1:], start=2):
        if len(values) != len(headers):
            raise ValueError(
                f"CSV row {row_number} has {len(values)} fields; "
                f"expected {len(headers)}: {csv_path}"
            )
        records.append(
            {header: value.strip() for header, value in zip(headers, values, strict=True)}
        )

    return records
