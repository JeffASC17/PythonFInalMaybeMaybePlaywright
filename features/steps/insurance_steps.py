from pathlib import Path

from behave import given, then, when
from playwright.sync_api import expect

from Config.environment import PROJECT_ROOT
from Utilities.common_utils import read_insurant_data, read_product_data, read_vehicle_data


def _data_file(file_name: str) -> Path:
    return PROJECT_ROOT / "Data" / file_name


@given('I use test data "{test_case}"')
def select_test_data(context, test_case: str) -> None:
    context.test_case = test_case


@given("I am on the home page")
def go_to_home_page(context) -> None:
    context.base_page.navigate("/")
    expect(context.page).to_have_title("Tricentis Vehicle Insurance")


@when("I open the automobile quote page")
def open_automobile_quote(context) -> None:
    context.home_page.open_automobile_quote()


@then("the vehicle fields should be visible")
def vehicle_fields_are_visible(context) -> None:
    expect(context.vehicle_page.make_field).to_be_visible(timeout=5_000)


@when('I enter the vehicle details from "{file_name}"')
def enter_vehicle_details(context, file_name: str) -> None:
    context.customer_business.enter_vehicle(
        read_vehicle_data(_data_file(file_name), context.test_case)
    )


@when("I go to Insurant Data")
def go_to_insurant_data(context) -> None:
    context.vehicle_page.continue_to_insurant()
    expect(context.insurant_page.first_name_field).to_be_visible(timeout=5_000)


@when('I enter Insurant details from "{file_name}"')
def enter_insurant_details(context, file_name: str) -> None:
    context.customer_business.enter_insurant(
        read_insurant_data(_data_file(file_name), context.test_case)
    )


@when("I go to Product Data")
def go_to_product_data(context) -> None:
    context.insurant_page.continue_to_product()
    expect(context.product_page.start_date_field).to_be_visible(timeout=5_000)


@when('I enter Product details from "{file_name}"')
def enter_product_details(context, file_name: str) -> None:
    context.customer_business.enter_product(
        read_product_data(_data_file(file_name), context.test_case)
    )


@when("I go to Select Price option")
def go_to_price_options(context) -> None:
    context.product_page.continue_to_price_option()


@then("I can see the Price Options Table")
def price_options_table_is_visible(context) -> None:
    expect(context.price_option_page.price_table).to_be_visible(timeout=5_000)
