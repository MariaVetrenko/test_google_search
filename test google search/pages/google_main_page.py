from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage

class GoogleMainPage(CommonPage):
    search_field = "//*[@class='gLFyf']"


