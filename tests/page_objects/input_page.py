from tests.helpers.support_functions import *


class InputPage:
    input_header = 'inputs-header'
    input_content = 'inputs-content'
    input = '//*[@id="inputs-content"]/div/input'


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, InputPage.input)
    elem = driver_instance.find_element_by_xpath(InputPage.input)
    elem.send_keys('123456')
    value = 123456
    if value == int(elem.get_attribute('value')):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, InputPage.input)
    elem = driver_instance.find_element_by_xpath(InputPage.input)
    elem.send_keys('essa')
    value = 'essa'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True
