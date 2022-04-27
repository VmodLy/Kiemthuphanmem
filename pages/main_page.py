from selenium.webdriver.common.keys import Keys
from pages.home_page import BasePage
from utils.locators import *

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver) 

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text