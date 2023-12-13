from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import logger


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__signOutElementLocator = (By.ID, "nav-item-signout")
        self.__searchProductLocater = (By.ID, "twotabsearchtextbox")
        self.__addToCartLocater = (By.ID, "add-to-cart-button")
        self.__firstResultLocater = (By.ID, ".s-result-item")
        self.__remove_locator = (By.CSS_SELECTOR, "[value='Delete']")
        self.__cartButtonLocator = (By.ID, "nav-cart-text-container")


    def fill_search_field(self, text):
        fillSearchFieldElement = self._find_element(self.__searchProductLocater)
        self._fill_field(fillSearchFieldElement, text)

    def click_to_sign_out_element(self):
        signOutButtonElement = self._find_element(self.__signOutElementLocator)
        self._click(signOutButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def get_add_to_cart_locator(self):
        return self.__addToCartLocater

    def get_first_result_locator(self):
        return self.__firstResultLocater

    def get_remove_locator(self):
        return self.__remove_locator

    def remove_from_cart(self):
        removeButtonElement = self._find_element(self.__remove_locator)
        self._click(removeButtonElement)

    def get_search_locator(self):
        return self.search_locator