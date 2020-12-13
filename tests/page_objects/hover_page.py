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








#num_of_users = len(list(self.driver.find_elements_by_css_selector(HoverSelectors.hover_figures_list)))
# for element in range(num_of_users):
#     assert_text = HoverSelectors.hover_users_name_text + str(element + 1)
#     assert_link = BasePage.USERS_URL + str(element + 1)
#     user_elem = f"//*[@id=\"hovers-content\"]/div/div[{str(element + 1)}]"
#     support_functions.click_tab(self.driver, HoverSelectors.hover_header)
#     hover_page.hover_content_displayed(self.driver)
#     support_functions.hover_over_element_by_xpath(self.driver, user_elem)
#     sleep(1)
#     h5_text = self.driver.find_elements_by_css_selector(HoverSelectors.hover_users_name_text_selector)[element].text
#     link_text = self.driver.find_elements_by_css_selector(HoverSelectors.hover_users_name_link_selector)[element].text
#     self.assertEqual(h5_text, assert_text)
#     self.driver.find_element_by_link_text(link_text).click()
#     self.assertEqual(self.driver.current_url, assert_link)
#     self.driver.back()
#

