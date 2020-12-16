import requests


class StatusCodeSelectors:
    status_codes_header = 'statuscodes-header'
    status_codes_content = 'statuscodes-content'
    id_elements = ['200siteAnchor', '305siteAnchor', '404siteAnchor', '500siteAnchor']
    codes = [200, 305, 404, 500]


def status_codes_check(driver_instance):
    received_codes = []
    for elem_id in StatusCodeSelectors.id_elements:
        elem = driver_instance.find_element_by_id(elem_id)
        url = elem.get_attribute("href")
        req = requests.get(url)
        status_code = req.status_code
        received_codes.append(status_code)
    if received_codes == StatusCodeSelectors.codes:
        return True
    else:
        return False
