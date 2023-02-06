from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.google_main_page import GoogleMainPage


def find_text(driver, text):
    driver.find_element(By.XPATH, GoogleMainPage.search_field).send_keys(text)
    driver.find_element(By.XPATH, GoogleMainPage.search_field).send_keys(Keys.ENTER)


