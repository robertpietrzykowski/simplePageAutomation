from tests.helpers.support_functions import wait_for_visibility_of_element_by_id


# MAIN PAGE REGION
main_page_header = "test-header"
main_page_content = "test-content"
# ENDREGION


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, main_page_header)
    return elem.is_displayed()