import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config.test_settings import TestSettings
from tests.page_objects import main_page, checkbox_page, hover_page, users_page, input_page, dropdown_page, \
    add_remove_page, basic_auth_page, form_page, key_press_page, status_codes_page
from tests.helpers import support_functions
from tests.page_objects.add_remove_page import AddRemoveSelectors
from tests.page_objects.basic_auth_page import BasicAuthSelectors
from tests.page_objects.checkbox_page import CheckboxSelectors
from tests.page_objects.date_picker_page import fill_date_picker, DatePickerSelectors
from tests.page_objects.drag_and_drop import DragAndDropSelectors
from tests.page_objects.dropdown_page import DropdownSelectors
from tests.page_objects.form_page import FormSelectors
from tests.page_objects.hover_page import HoverSelectors
from tests.page_objects.input_page import InputPage
from tests.page_objects.key_press_page import KeyPressSelectors
from tests.page_objects.status_codes_page import StatusCodeSelectors


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
        support_functions.click_tab(self.driver, CheckboxSelectors.checkbox_header)
        self.assertTrue(checkbox_page.checkbox_content_visible(self.driver))
        checkbox_page.checkbox_click_all_checkboxes(self.driver)

    def test3_date_picker_page(self):
        support_functions.click_tab(self.driver, DatePickerSelectors.date_picker_header)
        elem = self.driver.find_element_by_id(DatePickerSelectors.date_picker_field)
        fill_date_picker(self.driver, DatePickerSelectors.date_picker_field, DatePickerSelectors.date_picker_date)
        self.assertEqual(elem.get_attribute('value'), DatePickerSelectors.date_picker_date)

    def test4_hover_page(self):
        support_functions.click_tab(self.driver, HoverSelectors.hover_header)
        self.assertTrue(hover_page.hover_content_displayed(self.driver))
        hover_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test5_inputs_visibility(self):
        support_functions.click_tab(self.driver, InputPage.input_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, InputPage.input_content))

    def test5_send_correct_keys_to_input(self):
        support_functions.click_tab(self.driver, InputPage.input_header)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test6_send_incorrect_keys_to_input(self):
        support_functions.click_tab(self.driver, InputPage.input_header)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        support_functions.click_tab(self.driver, DropdownSelectors.dropdown_tab)
        self.assertTrue(support_functions.verify_content_visible(self.driver, DropdownSelectors.dropdown_content))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        support_functions.click_tab(self.driver, AddRemoveSelectors.add_remove_element_header)
        self.assertTrue(
            support_functions.verify_content_visible(self.driver, AddRemoveSelectors.add_remove_element_content))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        support_functions.click_tab(self.driver, AddRemoveSelectors.add_remove_element_header)
        self.assertTrue(
            support_functions.verify_content_visible(self.driver, AddRemoveSelectors.add_remove_element_content))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_successful_login(self, ):
        support_functions.click_tab(self.driver, BasicAuthSelectors.basic_auth_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, BasicAuthSelectors.basic_auth_content))
        self.assertTrue(basic_auth_page.login_success(self.driver, 'admin', 'admin'))

    def test11_unsuccessful_login(self, ):
        support_functions.click_tab(self.driver, BasicAuthSelectors.basic_auth_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, BasicAuthSelectors.basic_auth_content))
        self.assertTrue(basic_auth_page.login_failed(self.driver, 'user', 'user'))

    def test12_send_correct_form(self):
        support_functions.click_tab(self.driver, FormSelectors.form_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, FormSelectors.form_content))
        form_page.send_form_correct_data(self.driver, "Robert", "Essa")
        self.assertTrue(form_page.verify_alert_text_success(self.driver))

    def test13_send_empty_form(self):
        support_functions.click_tab(self.driver, FormSelectors.form_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, FormSelectors.form_content))
        form_page.send_form_correct_data(self.driver, "", "")
        self.assertFalse(form_page.verify_empty_field(self.driver, FormSelectors.first_name_field))
        self.assertFalse(form_page.verify_empty_field(self.driver, FormSelectors.last_name_field))

    def test14_send_character(self):
        support_functions.click_tab(self.driver, KeyPressSelectors.key_press_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, KeyPressSelectors.key_press_content))
        key_press_page.press_key(self.driver, Keys.TAB)
        self.assertTrue(key_press_page.check_key(self.driver, 'TAB'))

    def test15_drag_and_drop(self):
        support_functions.click_tab(self.driver, DragAndDropSelectors.drag_and_drop_header)
        self.assertTrue(
            support_functions.verify_content_visible(self.driver, DragAndDropSelectors.drag_and_drop_content))

    def test16_test_status_codes(self):
        support_functions.click_tab(self.driver, StatusCodeSelectors.status_codes_header)
        self.assertTrue(support_functions.verify_content_visible(self.driver, StatusCodeSelectors.status_codes_content))
        self.assertTrue(status_codes_page.status_codes_check(self.driver))


if __name__ == '__main__':
    unittest.main()
