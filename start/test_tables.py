"""Tables – reading a column and sorting by clicking the header."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page, wait_for_class

URL = f"{INTERNET_URL}/tables"


def column(driver, table_id, index):
    """Cell texts of column `index` (from 1) of the table with this id."""
    # TODO: selector f"#{table_id} tbody td:nth-child({index})"
    return []


def test_read_column(driver):
    # TODO: column 1 of table1 = Smith, Bach, Doe, Conway
    pytest.skip("TODO")


def test_sort_last_names(driver):
    # TODO: click the "Last Name" header, wait for the class
    #       "headerSortDown"; then the list == sorted(list)
    pytest.skip("TODO")


def test_sort_amounts_descending(driver):
    # TODO: click the "Due" header of table 2 twice; after the
    #       second click the class is "headerSortUp" -> descending
    pytest.skip("TODO")
