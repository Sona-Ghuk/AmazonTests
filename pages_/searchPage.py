from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def set_price_range(self, min_price, max_price):
        min_price_input = self.driver.find_element(By.ID, 'min-price-input')
        max_price_input = self.driver.find_element(By.ID, 'max-price-input')

        min_price_input.clear()
        min_price_input.send_keys(str(min_price))

        max_price_input.clear()
        max_price_input.send_keys(str(max_price))

    def apply_price_filter(self):
        apply_button = self.driver.find_element(By.ID, 'apply-filter-button')
        apply_button.click()