from selenium.webdriver.common.alert import Alert

from tests.helpers.support_functions import *


class FormSelectors:
    form_header = 'form-header'
    form_content = 'form-header'
    first_name_field = 'fname'
    last_name_field = 'lname'
    form_submit_btn = 'formSubmitButton'


def fill_data_field(driver_instance, elem, data):
    wait_for_visibility_of_element(driver_instance, By.ID, elem)
    elem = driver_instance.find_element_by_id(elem)
    elem.click()
    elem.send_keys(data)


def click_submit_btn(driver_instance, elem):
    elem = driver_instance.find_element_by_id(elem)
    elem.click()


def send_form_correct_data(driver_instance, fname, lname):
    fill_data_field(driver_instance, FormSelectors.first_name_field, fname)
    fill_data_field(driver_instance, FormSelectors.last_name_field, lname)
    click_submit_btn(driver_instance, FormSelectors.form_submit_btn)


def verify_alert_text_success(driver_instance):
    alert = Alert(driver_instance)
    alert_text = alert.text
    if alert_text == 'success':
        return True
    return False


def verify_empty_field(driver_instance, selector):
    elem = driver_instance.find_element_by_id(selector)
    return driver_instance.execute_script("return arguments[0].validity.valid;", elem)
