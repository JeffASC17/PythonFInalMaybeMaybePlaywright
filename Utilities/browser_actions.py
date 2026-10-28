from collections.abc import Callable

from playwright.sync_api import Locator

LogCallback = Callable[[str], None]


class BrowserActions:
    def __init__(
        self,
        write_log: LogCallback = print,
    ) -> None:
        self.write_log = write_log

    def fill(self, locator: Locator, value: str, object_name: str) -> None:
        try:
            locator.fill(value)
            self.write_log(f"Filled {value} in {object_name}")
        except Exception as error:
            self.write_log(f"FAIL: Filling {object_name}\n{error}")
            raise

    def select(self, locator: Locator, value: str, object_name: str) -> None:
        try:
            locator.select_option(label=value)
            self.write_log(f"Selected {value} in {object_name}")
        except Exception as error:
            self.write_log(f"FAIL: Selecting {object_name}\n{error}")
            raise

    def click(self, locator: Locator, object_name: str) -> None:
        try:
            locator.click()
            self.write_log(f"Clicked on {object_name}")
        except Exception as error:
            self.write_log(f"FAIL: Clicking {object_name}\n{error}")
            raise
