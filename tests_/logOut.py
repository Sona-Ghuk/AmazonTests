import time
import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener


class LogInPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com")
        time.sleep(2)

    def test_sign_out(self):
        navigation_bar = NavigationBar(self.driver)

    def tearDown(self):
        self.driver.quit()
