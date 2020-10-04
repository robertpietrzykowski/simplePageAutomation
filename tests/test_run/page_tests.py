import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkbox_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(TestSettings.WEBDRIVER_CHROME_PATH)
        self.url = TestSettings.URL
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkbox_page(self):
        checkbox_page.checkbox_click_tab(self.driver)
        self.assertTrue(checkbox_page.checkbox_content_visible(self.driver))
        checkbox_page.checkbox_click_all_checkboxes(self.driver)
