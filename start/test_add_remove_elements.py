"""Adding and removing elements – find_elements() and count."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/add_remove_elements/"
ADD = (By.CSS_SELECTOR, "button[onclick='addElement()']")
DELETE = (By.CSS_SELECTOR, "#elements button")


def test_no_buttons_at_start(driver):
    # TODO: find_elements(*DELETE) returns an empty list
    pytest.skip("TODO")


def test_add_three_delete_one(driver):
    # TODO: 3 × Add Element -> 3 Delete buttons; delete 1 -> 2
    pytest.skip("TODO")
