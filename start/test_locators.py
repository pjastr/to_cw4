"""DevTools exercise: CSS and XPath locators.

Fill in the table: for each element enter a CSS selector
and an XPath expression (checked in DevTools: $$() and $x()).
"""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page

I, W = INTERNET_URL, SELENIUM_WEB_URL + "/web-form.html"
LOCATORS = [
    (I + "/login", "", ""),              # 1 Username field
    (I + "/login", "", ""),              # 2 Login button
    (I + "/login", "", ""),              # 3 Password label
    (I + "/checkboxes", "", ""),         # 4 second checkbox
    (I + "/tables", "", ""),             # 5 J. Doe's e-mail (table 2)
    (I + "/tables", "", ""),             # 6 Due header (table 1)
    (I + "/add_remove_elements/", "", ""),  # 7 Add Element
    (W, "", ""),                         # 8 Text input field
    (W, "", ""),                         # 9 Disabled input field
    (W, "", ""),                         # 10 option "Two"
    (W, "", ""),                         # 11 Submit button
    (W, "", ""),                         # 12 Return to index link
]


@pytest.mark.parametrize("url, css, xpath", LOCATORS)
def test_css_and_xpath(driver, url, css, xpath):
    if not css or not xpath:
        pytest.skip("TODO: fill in the locators")
    open_page(driver, url, By.CSS_SELECTOR, "#content, form")
    by_css = driver.find_elements(By.CSS_SELECTOR, css)
    by_xpath = driver.find_elements(By.XPATH, xpath)
    assert len(by_css) == 1, "CSS: expected exactly 1 element"
    assert len(by_xpath) == 1, "XPath: expected exactly 1 element"
    assert by_css[0] == by_xpath[0]           # the same element
