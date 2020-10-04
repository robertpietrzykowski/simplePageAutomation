import time

from tests.helpers.support_functions import wait_for_visibility_of_element_by_id


# CHECKBOX PAGE REGION
checkbox_header = 'checkbox-header'
checkbox_content = 'checkbox-content'
checkbox_container = 'checkboxes'
checkbox_first = '//*[@id="checkboxes"]/input[1]'
checkbox_second = '//*[@id="checkboxes"]/input[2]'
# ENDREGION


def checkbox_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, checkbox_header)
    return elem.is_displayed()


def checkbox_click_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, checkbox_header)
    elem = driver_instance.find_element_by_id(checkbox_header)
    elem.click()


def checkbox_click_all_checkboxes(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, checkbox_container)
    first_checkbox = driver_instance.find_element_by_xpath(checkbox_first)
    first_checkbox.click()
    second_checkbox = driver_instance.find_element_by_xpath(checkbox_second)
    second_checkbox.click()
