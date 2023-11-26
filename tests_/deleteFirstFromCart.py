import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener


class LogInPage(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_Login(self):
        loginPage = LoginPage(self.driver)
        loginPage.fill_username_field("sona.ghukasyan@gmail.com")
        loginPage.click_to_continue_button()
        loginPage.fill_password_field("hasiko07")
        loginPage.click_to_signin_button()

    def search_product(self):
        navigation_bar = NavigationBar(self.driver)
        search_input = self.driver.find_element(navigation_bar.get_search_locator())
        search_input.send_keys("Laptop")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        navigation_bar.click_to_sign_out_element()
        first_result = self.driver.find_element(navigation_bar.get_first_result_locator())
        first_result.click()
        time.sleep(5)

    def add_to_cart(self):
        navigation_bar = NavigationBar(self.driver)
        add_to_cart_button = self.driver.find_element(navigation_bar.get_add_to_cart_locator())
        add_to_cart_button.click()
        time.sleep(5)

    def remove_from_cart(self):
        navigation_bar = NavigationBar(self.driver)
        remove_button = self.driver.find_element(navigation_bar.get_remove_from_cart_locator())
        remove_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()