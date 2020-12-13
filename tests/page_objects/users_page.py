from tests.helpers.support_functions import *

error_info = "container"


def error_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, error_info)
    return elem.is_displayed()

