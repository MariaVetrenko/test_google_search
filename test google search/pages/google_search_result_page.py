from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class GoogleSearchResultPage(CommonPage):
    first_found_title = "//*[@class='LC20lb MBeuO DKV0Md'][1]"
