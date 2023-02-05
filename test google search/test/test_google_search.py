from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from test_data import *
from steps.common_steps import *
from steps.google_main_steps import *
from steps.google_search_result_steps import *


def test_google_search(getDriver):
    go_to_site(getDriver, LINK)
    title_before_search = getDriver.find_element(By.XPATH,"/html/head/title[1]")
    find_text(getDriver, TEST_SEARCH_TEXT)
    title_after_search = getDriver.find_element(By.XPATH, "/html/head/title[1]")

    assert title_before_search != title_after_search, "Title didn't change after search, expected that change."



