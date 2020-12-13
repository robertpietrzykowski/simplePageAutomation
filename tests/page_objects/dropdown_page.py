from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select


class DropdownSelectors:
    dropdown_tab = 'dropdownlist-header'
    dropdown_content = 'dropdownlist-content'
    dropdown_list = 'dropdown'


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(DropdownSelectors.dropdown_list))
    wait_for_visibility_of_element(driver_instance, By.ID, DropdownSelectors.dropdown_list)
    elem_list.select_by_index(1)
