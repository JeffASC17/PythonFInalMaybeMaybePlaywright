# Playwright Python Automation

Python translation of the repository's automobile insurance quote automation,
using Playwright's synchronous API, Behave/Gherkin, and the Page Object Model.
This project is self-contained; the original TypeScript files are not changed.

## Requirements

- Python 3.10 or later
- A supported Playwright browser installation
- Allure Commandline (requires Java) to generate and open the HTML report

## Setup

From this directory, create and activate a virtual environment, then install
the dependencies and Chromium:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Set the target application URL in `.env` or in the process environment. For
example, create `.env` with:

```dotenv
BASE_URL=https://sampleapp.tricentis.com/101/
```

Run the Gherkin scenario and generate an Allure HTML report:

```powershell
python run_tests.py
```

The runner writes raw results to a unique folder under
`reports/allure-results/` and generates the HTML report under
`reports/allure-report/`. It attaches action screenshots, execution logs, and a
failure screenshot to the Allure results. Open the generated report using the
path printed by the runner:

```powershell
allure open reports/allure-report/<run-id>
```

`python -m behave` can still be used to run Behave directly, but use
`python run_tests.py` when you want Allure results and the HTML report.

Run the CSV utility tests:

```powershell
python -m unittest discover -s tests
```

The browser runs headlessly. Screenshots taken after browser actions and
scenario logs are written beneath `reports/` and attached to the Allure report.
A full-page screenshot is also captured and attached when a scenario fails.

## Structure

- `features/` — Gherkin feature and Behave step definitions
- `features/environment.py` — per-scenario browser lifecycle and artifacts
- `pages/` — page objects for the quote flow
- `BusinessMethods/` — customer workflow orchestration
- `Utilities/` — browser actions and validated CSV loading
- `Data/` — the source CSV test records
- `Config/` — environment and base URL configuration
- `tests/` — focused tests for CSV parsing and validation
