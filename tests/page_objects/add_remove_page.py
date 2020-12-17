from selenium.common.exceptions import NoSuchElementException

from tests.helpers.support_functions import *


class AddRemoveSelectors:
    add_remove_element_header = 'addremoveelements-header'
    add_remove_element_content = 'addremoveelements-content'
    new_element = '//*[@id="addremoveelements-content"]/div/div/button'
    added_element = '//*[@id="elements"]/button'


def add_element(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, AddRemoveSelectors.new_element)
    elem = driver_instance.find_element_by_xpath(AddRemoveSelectors.new_element)
    elem.click()


def delete_element(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, AddRemoveSelectors.new_element)
    elem = driver_instance.find_element_by_xpath(AddRemoveSelectors.added_element)
    elem.click()
    wait_for_visibility_of_element(driver_instance, By.XPATH, AddRemoveSelectors.added_element)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element(driver_instance, By.XPATH, AddRemoveSelectors.added_element)
        return True
    except NoSuchElementException:
        return False







