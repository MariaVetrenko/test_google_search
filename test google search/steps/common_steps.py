import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.common_page import CommonPage


@pytest.fixture(scope="function")
def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver  # делит функцию на части до тестов и после тестов
    driver.close()


def go_to_site(driver, base_url):
    return driver.get(base_url)
