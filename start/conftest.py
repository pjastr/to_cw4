"""Shared fixtures for all tests (conftest.py)."""
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """A new Chrome browser for each test."""
    # TODO 1: drv = webdriver.Chrome()   (Selenium Manager)
    # TODO 2: drv.implicitly_wait(0)     (explicit waits only)
    # TODO 3: yield drv                  (the test runs here)
    # TODO 4: drv.quit()                 (cleanup)
    pytest.skip("TODO: complete the driver fixture in conftest.py")
