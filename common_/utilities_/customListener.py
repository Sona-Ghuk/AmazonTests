from common_.utilities_.customLogger import *
from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_.customLogger import logger


class CustomListener(AbstractEventListener):
    def after_navigate_to(self, url, driver):
        print("After navigating to ", url)
    def after_navigate_back(self, driver):
        print("After navigating back ", driver.current_url)
    def after_navigate_forward(self, driver):
        print("After navigating forward ", driver.current_url)
    def after_find(self, by, value, driver):
        logger("INFO", f"Founded element with locator: By: {by}, Value: {value}")
    def after_click(self, element, driver):
        logger("INFO", f"Clicked to element: {element}")
    def after_change_value_of(self, element, driver):
        logger("INFO", f"Changed value of element: {element}")
    def after_execute_script(self, script, driver):
        print("after_execute_script")
    def after_close(self, driver):
        logger("INFO", "Closing Browser!")
    def after_quit(self, driver):
        logger("INFO", "Quiting browser tab!")
    def on_exception(self, exception, driver):
        print("on_exception")
