import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com" "%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" "%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F""%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        login_page = LoginPage(self.driver)
        login_page.fill_username_field("sona.ghukasyan@gmail.com")
        login_page.click_to_continue_button()
        login_page.fill_password_field("hasiko07")
        login_page.click_to_signin_button()

    def test_negative_login_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.fill_username_field("sona.ghukasyan@gmail.com")
        login_page.click_to_continue_button()
        login_page.fill_password_field("fendi")
        login_page.click_to_signin_button()
        time.sleep(5)
        expected_error_message = "password is incorrect"
        actual_error_message = expected_error_message
        self.assertEqual(actual_error_message, expected_error_message)

    def tearDown(self):
        self.driver.close()
