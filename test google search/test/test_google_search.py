from test_data import *
from steps.common_steps import *
from steps.google_main_steps import *
from steps.google_search_result_steps import *
from selenium.common.exceptions import NoSuchElementException


def test_google_search(getDriver):
    go_to_site(getDriver, LINK)
    title_before_search = getDriver.title
    find_text(getDriver, TEST_SEARCH_TEXT)
    title_after_search = getDriver.title

    assert title_before_search != title_after_search, "Title didn't change after search, expected that change."
    try:
        getDriver.find_element(By.XPATH, "//h3[contains(text(),'Automation QA')]")
    except NoSuchElementException as e:
        raise NoSuchElementException("ERROR: on result page we should have title with our test request:'" + TEST_SEARCH_TEXT + "'. " + str(e))

