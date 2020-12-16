from selenium.webdriver import ActionChains


class DragAndDropSelectors:
    drag_and_drop_header = 'draganddrop-header'
    drag_and_drop_content = 'draganddrop-content'
    column_a = "column-a"
    column_b = "column-b"


def perform_drag_and_drop(driver_instance):
    source = driver_instance.find_element_by_id(DragAndDropSelectors.column_a)
    target = driver_instance.find_element_by_id(DragAndDropSelectors.column_b)
    action = ActionChains(driver_instance)
    action.move_to_element(target)
    action.drag_and_drop(source, target).perform()
