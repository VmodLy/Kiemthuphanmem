import unittest
from tests.test_home import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases

class TestSignInPage(BaseTest):

    # test 1
    def test_page_load(self):
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    #test 2
    def test_search_item(self):
        page = MainPage(self.driver)
        self.driver.save_screenshot('BeforeSearch.png')
        search_result = page.search_item("lmao")
        self.driver.save_screenshot('AfterSearch.png')
        self.assertIn("lmao", search_result)