from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TODO: FIX REDUNDAND METHOD
def hover_over_element_by_xpath(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def hover_over_element_by_class(driver_instance, class_id):
    elem = driver_instance.find_element_by_class_name(class_id)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


# TODO: Do the cleanup of wait for visibility function use DRY pattern
def wait_for_visibility_of_element(driver_instance, by, elem, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((by, elem)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, by, elem, time_to_wait=10):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((by, elem)))
    return inv_elem


def click_tab(driver_instance, header):
    wait_for_visibility_of_element(driver_instance, By.ID, header)
    elem = driver_instance.find_element_by_id(header)
    elem.click()


def verify_content_visible(driver_instance, content):
    wait_for_visibility_of_element(driver_instance, By.ID, content)
    elem = driver_instance.find_element_by_id(content)
    return elem.is_displayed()

