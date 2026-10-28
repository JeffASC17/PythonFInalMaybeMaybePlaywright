from collections.abc import Callable

from playwright.sync_api import Page

from Config.environment import resolve_url
from Utilities.browser_actions import BrowserActions


class BasePage:
    def __init__(
        self,
        page: Page,
        base_url: str,
        write_log: Callable[[str], None],
    ) -> None:
        self.page = page
        self.base_url = base_url
        self.browser_actions = BrowserActions(write_log)

    def navigate(self, path: str) -> None:
        self.page.goto(resolve_url(self.base_url, path), wait_until="domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()
