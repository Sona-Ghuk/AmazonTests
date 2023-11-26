from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordButtonLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordButtonLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_signin_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click(signInButtonElement)

    def test_negative_login_invalid_password(self):
        actual_error_message = login_page.get_error_message()

        expected_error_message = "password is incorrect"
        self.assertEqual(actual_error_message, expected_error_message, "Error message")






