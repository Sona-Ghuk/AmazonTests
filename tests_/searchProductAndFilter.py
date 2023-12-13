import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage
from pages_.searchPage import SearchPage
from pages_.navigationBar import NavigationBar
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener


class AmazonTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_Login(self):
        loginPage = LoginPage(self.driver)
        loginPage.fill_username_field("sona.ghukasyan@gmail.com")
        loginPage.click_to_continue_button()
        loginPage.fill_password_field("hasiko07")
        loginPage.click_to_signin_button()
        time.sleep(5)

    def search_product(self):
        navigation_bar = NavigationBar(self.driver)
        search_input = self.driver.find_element(*navigation_bar.get_search_locator())
        search_input.send_keys("adidas shoes women")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def price_filter(self):
        search_page = SearchPage(self.driver)
        search_page.set_price_range(50, 100)
        search_page.apply_price_filter()
        time.sleep(5)

    def test_select_product(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, ".product_title")
        if results:
            results[0].click()


    def tearDown(self):
        self.driver.quit()