"""First tests: open a page and check its title."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page


def test_title_the_internet(driver):
    # TODO: open f"{INTERNET_URL}/login" (marker: By.ID, "login")
    # TODO: check that driver.title == "The Internet"
    pytest.skip("TODO")


def test_title_web_form(driver):
    # TODO: open f"{SELENIUM_WEB_URL}/web-form.html"
    #       (marker: By.TAG_NAME, "form")
    # TODO: check the title "Web form" and the end of current_url
    pytest.skip("TODO")
