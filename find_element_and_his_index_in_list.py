def find(required_element, source_list):
    for (index, element) in enumerate(source_list):
        if element == required_element:
            return index, element
    return "Error: element not found"

