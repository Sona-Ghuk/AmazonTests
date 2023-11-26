from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_.customLogger import logger


class CustomListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        logger.info(f"Before navigating to: {url}")

    def after_navigate_to(self, url, driver):
        logger.info(f"After navigating to: {url}")

    def before_click(self, element, driver):
        logger.info(f"Before clicking on element: {element}")

    def after_click(self, element, driver):
        logger.info(f"After clicking on element: {element}")

    def after_quit(self, driver):
        logger.info("After quitting the driver")

    def on_exception(self, exception, driver):
        logger.error(f"Exception encountered: {exception}")
        logger.info(f"Navigating to {url}")

    def before_find(self, by, value, driver):
        logger.info(f"Trying to find element by: {by} with value: {value}")

    def after_find(self, by, value, driver):
        logger.info(f"Found element by: {by} with value: {value}")