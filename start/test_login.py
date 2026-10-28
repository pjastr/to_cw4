"""Login on the-internet – equivalence partitioning (EP)."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page, wait_for

USERNAME, PASSWORD = "tomsmith", "SuperSecretPassword!"


def log_in(driver, username, password):
    """Fills in the form; returns the #flash message."""
    open_page(driver, f"{INTERNET_URL}/login", By.ID, "login")
    # TODO: type the username (#username) and the password (#password)
    # TODO: click the "#login button" button
    return wait_for(driver, By.ID, "flash")


# TODO: add 4 equivalence classes: valid data, wrong username,
#       wrong password, empty fields (expected message and path)
@pytest.mark.parametrize("username, password, message, path", [
    (USERNAME, PASSWORD, "You logged into a secure area!", "/secure"),
])
def test_login_ep(driver, username, password, message, path):
    pytest.skip("TODO: log_in(), check the message and the path")


def test_message_css_class(driver):
    # TODO: after a wrong password #flash has the CSS class "error"
    pytest.skip("TODO")
