"""Selenium Web Form – form fields, their state and submission."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from config import SELENIUM_WEB_URL
from helpers import open_page, wait_for


@pytest.fixture
def page(driver):
    """Opens the form and returns the driver."""
    url = f"{SELENIUM_WEB_URL}/web-form.html"
    open_page(driver, url, By.TAG_NAME, "form")
    return driver


def test_text_fields(page):
    # TODO: text, password, textarea – send_keys, value, clear()
    pytest.skip("TODO")


def test_attribute_vs_property(page):
    # TODO: get_dom_attribute vs get_property vs get_attribute
    pytest.skip("TODO")


def test_disabled_and_readonly(page):
    # TODO: is_enabled(); readOnly; value of the readonly field
    pytest.skip("TODO")


def test_select_and_datalist(page):
    # TODO: Select "Two" -> value "2"; 5 datalist options
    pytest.skip("TODO")


def test_checkbox_and_radio(page):
    # TODO: state of my-check-1/2, click my-radio-2
    pytest.skip("TODO")


def test_submit_form(page):
    # TODO: Submit -> "Form submitted", #message == "Received!"
    pytest.skip("TODO")
