"""Checkboxes – is_selected() state and clicks."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/checkboxes"
CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")


def test_initial_state(driver):
    # TODO: 2 boxes; the first unchecked, the second checked
    pytest.skip("TODO")


def test_check_and_uncheck(driver):
    # TODO: click both boxes and check that the state is reversed
    pytest.skip("TODO")
