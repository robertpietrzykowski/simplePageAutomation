import os


class DragAndDropSelectors:
    drag_and_drop_header = 'draganddrop-header'
    drag_and_drop_content = 'draganddrop-content'
    column_a = "column-a"
    column_b = "column-b"


def perform_drag_and_drop(driver_instance):
    with open(os.path.abspath('../helpers/drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    elem = driver_instance.find_element_by_id(DragAndDropSelectors.column_a)
    if elem.text == 'B':
        return True
    return False
