from time import sleep

from tests.helpers.support_functions import *


class BasicAuthSelectors:
    basic_auth_header = 'basicauth-header'
    basic_auth_content = 'basicauth-content'
    username = 'ba_username'
    password = 'ba_password'
    login_btn = '//*[@id="content"]/button'
    success_login_msg = 'loggedInMessage'
    failed_login_msg = 'loginFormMessage'


def fill_field(driver_instance, elem, value):
    field = driver_instance.find_element_by_id(elem)
    wait_for_visibility_of_element(driver_instance, By.ID, elem, 2)
    field.click()
    field.send_keys(value)


def login_success(driver_instance, username, password):
    fill_field(driver_instance, BasicAuthSelectors.username, username)
    fill_field(driver_instance, BasicAuthSelectors.password, password)
    login_btn = driver_instance.find_element_by_xpath(BasicAuthSelectors.login_btn)
    login_btn.click()
    login_message = driver_instance.find_element_by_id(BasicAuthSelectors.success_login_msg)
    if login_message.text == 'You are logged in!':
        return True
    else:
        return False


def login_failed(driver_instance, username, password):
    fill_field(driver_instance, BasicAuthSelectors.username, username)
    fill_field(driver_instance, BasicAuthSelectors.password, password)
    login_btn = driver_instance.find_element_by_xpath(BasicAuthSelectors.login_btn)
    login_btn.click()
    login_message = driver_instance.find_element_by_id(BasicAuthSelectors.failed_login_msg)
    if login_message.text == 'Invalid credentials':
        return True
    else:
        return False

