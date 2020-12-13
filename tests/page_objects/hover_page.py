from tests.helpers.support_functions import *


class HoverSelectors:
    # HOVER PAGE REGION
    hover_header = 'hovers-header'
    hover_content = 'hovers-content'
    hover_figures_list = ".figure .figcaption"
    hover_figure = 'figure'
    hover_users_name_text = 'name: user'
    hover_users_name_text_selector = ".figcaption h5"
    hover_users_name_link_selector = ".figcaption a"
    gentleman_pic = "//*[@id=\"hovers-content\"]/div/div[1]/img"
    gentleman_link = "//*[@id=\"hovers-content\"]/div/div[1]/div/a"
    # ENDREGION


def hover_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.ID, HoverSelectors.hover_content)
    return elem.is_displayed()


def hover_over_element_and_click(driver_instance):
    hover_over_element_by_xpath(driver_instance, HoverSelectors.gentleman_pic)
    elem = driver_instance.find_element_by_xpath(HoverSelectors.gentleman_link)
    elem.click()
