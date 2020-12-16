from time import sleep

from selenium.webdriver.common.keys import Keys

from tests.helpers.support_functions import *


class KeyPressSelectors:
    key_press_header = 'keypresses-header'
    key_press_content = 'keypresses-content'
    key_press_input = 'target'
    key_press_result = 'keyPressResult'


def press_key(driver_instance, key):
    elem = driver_instance.find_element_by_id(KeyPressSelectors.key_press_input)
    sleep(1)
    elem.click()
    elem.send_keys(key)


def check_key(driver_instance, key):
    elem = driver_instance.find_element_by_id(KeyPressSelectors.key_press_result)
    print(elem.text)
    print(f'You entered: {key}')
    if elem.text == f'You entered: {key}':
        return True
    else:
        return False
