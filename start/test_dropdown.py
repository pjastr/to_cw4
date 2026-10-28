"""Dropdown list – the Select class."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/dropdown"


def test_dropdown_options(driver):
    # TODO: Select(...).options – 3 options; the first one disabled
    pytest.skip("TODO")


def test_select_option(driver):
    # TODO: select_by_visible_text, select_by_value, select_by_index
    pytest.skip("TODO")
