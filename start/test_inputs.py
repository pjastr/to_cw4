"""The <input type=number> field – send_keys, clear, keys."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/inputs"
FIELD = (By.CSS_SELECTOR, "input[type='number']")


# TODO: add cases: a negative number, letters (empty field)
@pytest.mark.parametrize("typed, expected", [
    ("10", "10"),
])
def test_typing(driver, typed, expected):
    pytest.skip("TODO: type the text, compare get_property('value')")


def test_arrows_and_clear(driver):
    # TODO: "5" + 2 × Keys.ARROW_UP -> "7"; clear() -> ""
    pytest.skip("TODO")
