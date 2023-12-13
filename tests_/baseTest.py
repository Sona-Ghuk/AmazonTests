import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from testData_.testData import signInPageUrl, validUser, userWithInvalidUserName


class BaseTestWithoutLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.signInPage = LoginPage(self.driver)

    def test_valid_login(self):
        self.driver.get(signInPageUrl)
        self.signInPage.fill_username_field(validUser.userName)
        self.signInPage.click_to_continue_button()
        self.signInPage.fill_password_field(validUser.password)
        self.signInPage.click_to_signin_button()

    def test_invalid_login(self):
        self.driver.get(signInPageUrl)
        self.signInPage.fill_username_field(userWithInvalidUserName.userName)
        self.signInPage.click_to_continue_button()
        self.signInPage.fill_password_field(userWithInvalidUserName.password)
        self.signInPage.click_to_signin_button()

    def tearDown(self):
        self.driver.quit()


