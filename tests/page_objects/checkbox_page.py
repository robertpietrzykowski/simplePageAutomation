from selenium.webdriver.common.by import By

from tests.helpers.support_functions import wait_for_visibility_of_element


class CheckboxSelectors:
    # CHECKBOX PAGE REGION
    checkbox_header = 'checkbox-header'
    checkbox_content = 'checkbox-content'
    checkbox_container = 'checkboxes'
    checkbox_first = '//*[@id="checkboxes"]/input[1]'
    checkbox_second = '//*[@id="checkboxes"]/input[2]'
    # ENDREGION


def checkbox_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, CheckboxSelectors.checkbox_header)
    return elem.is_displayed()


def checkbox_click_all_checkboxes(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.ID, CheckboxSelectors.checkbox_container)
    first_checkbox = driver_instance.find_element_by_xpath(CheckboxSelectors.checkbox_first)
    first_checkbox.click()
    second_checkbox = driver_instance.find_element_by_xpath(CheckboxSelectors.checkbox_second)
    second_checkbox.click()
