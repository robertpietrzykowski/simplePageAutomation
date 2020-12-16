from tests.helpers.support_functions import *


class IframeSelectors:
    iframe_header = 'iframe-header'
    iframe_content = 'iframe-content'
    iframe = '//*[@id="iframe-content"]/div/div/iframe'
    iframe_button1 = 'simpleButton1'
    iframe_button2 = 'simpleButton2'
    msg_selector = 'whichButtonIsClickedMessage'


def click_iframe_button1(driver_instance):
    expected_msg = 'Button 1 was clicked!'
    driver_instance.switch_to.frame(driver_instance.find_element_by_xpath(IframeSelectors.iframe))
    button = driver_instance.find_element_by_id(IframeSelectors.iframe_button1)
    button.click()
    msg = driver_instance.find_element_by_id(IframeSelectors.msg_selector).text
    if expected_msg == msg:
        driver_instance.switch_to.default_content()
        return True
    return False


def click_iframe_button2(driver_instance):
    expected_msg = 'Button 2 was clicked!'
    driver_instance.switch_to.frame(driver_instance.find_element_by_xpath(IframeSelectors.iframe))
    button = driver_instance.find_element_by_id(IframeSelectors.iframe_button2)
    button.click()
    msg = driver_instance.find_element_by_id(IframeSelectors.msg_selector).text
    if expected_msg == msg:
        driver_instance.switch_to.default_content()
        return True
    return False


def verify_iframe_visible(driver_instance, content):
    wait_for_visibility_of_element(driver_instance, By.XPATH, content)
    elem = driver_instance.find_element_by_xpath(content)
    return elem.is_displayed()


