import re
from datetime import datetime

import allure
from playwright.sync_api import sync_playwright

from BusinessMethods.customer_business import CustomerBusiness
from Config.environment import PROJECT_ROOT, get_base_url
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.insurant_page import InsurantPage
from pages.price_option_page import PriceOptionPage
from pages.product_page import ProductPage
from pages.vehicle_page import VehiclePage


def before_all(context) -> None:
    context.base_url = get_base_url()


def before_scenario(context, scenario) -> None:
    scenario_name = re.sub(r"[^A-Za-z0-9._-]+", "-", scenario.name).strip("-")
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    context.artifact_dir = PROJECT_ROOT / "reports" / run_id / scenario_name
    context.artifact_dir.mkdir(parents=True, exist_ok=True)
    context.execution_logs = []
    context.screenshot_count = 0

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()
    context.page.set_default_timeout(30_000)

    context.capture_screenshot = lambda name: _capture_screenshot(context, name)
    context.write_log = lambda message: _write_log(context, message)
    page_args = (context.base_url, context.capture_screenshot, context.write_log)
    context.base_page = BasePage(context.page, *page_args)
    context.home_page = HomePage(context.page, *page_args)
    context.vehicle_page = VehiclePage(context.page, *page_args)
    context.insurant_page = InsurantPage(context.page, *page_args)
    context.product_page = ProductPage(context.page, *page_args)
    context.price_option_page = PriceOptionPage(context.page, *page_args)
    context.customer_business = CustomerBusiness(
        context.vehicle_page,
        context.insurant_page,
        context.product_page,
    )


def after_scenario(context, scenario) -> None:
    try:
        if context.execution_logs:
            log_path = context.artifact_dir / "execution.log"
            log_path.write_text("\n".join(context.execution_logs), encoding="utf-8")
            allure.attach.file(
                str(log_path),
                name="Execution logs",
                attachment_type=allure.attachment_type.TEXT,
            )
        if scenario.status.name == "failed" and context.page:
            screenshot_path = context.artifact_dir / "failure.png"
            context.page.screenshot(
                path=str(screenshot_path),
                full_page=True,
            )
            allure.attach.file(
                str(screenshot_path),
                name="Failure screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
    finally:
        if getattr(context, "browser", None):
            context.browser.close()
        if getattr(context, "playwright", None):
            context.playwright.stop()


def _capture_screenshot(context, action_name: str) -> None:
    context.screenshot_count += 1
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", action_name).strip("-")
    screenshot_path = context.artifact_dir / f"{context.screenshot_count:03d}-{safe_name}.png"
    context.page.screenshot(path=str(screenshot_path), full_page=True)
    allure.attach.file(
        str(screenshot_path),
        name=action_name,
        attachment_type=allure.attachment_type.PNG,
    )


def _write_log(context, message: str) -> None:
    formatted_message = f"[{datetime.now().astimezone().isoformat()}] {message}"
    print(formatted_message)
    context.execution_logs.append(formatted_message)
