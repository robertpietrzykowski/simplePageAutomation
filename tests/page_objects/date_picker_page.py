
class DatePickerSelectors:
    # CHECKBOX PAGE REGION
    date_picker_header = 'datepicker-header'
    date_picker_content = 'datepicker-content'
    date_picker_field = 'start'
    date_picker_date = '2020-10-10'
    # ENDREGION


def fill_date_picker(driver_instance, elem_id, date):
    date_picker_elem = driver_instance.find_element_by_id(elem_id)
    driver_instance.execute_script(f"arguments[0].setAttribute('value', '{date}')", date_picker_elem)
