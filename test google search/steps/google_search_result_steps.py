from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.google_search_result_page import GoogleSearchResultPage


def open_text(driver, text):
    driver.find_element(By.XPATH, GoogleSearchResultPage.first_found_title).send_keys(text)
    driver.find_element(By.XPATH, GoogleSearchResultPage.first_found_title).send_keys(Keys.DOWN)