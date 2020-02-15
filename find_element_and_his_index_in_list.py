def find(required_element, source_list):
    for (index, element) in enumerate(source_list):
        if element == required_element:
            return index, element
    return "Error: element not found"


str_list = ['первый', 'второй', 'третий']
numeric_list = [10, 20, 30]

print(find('первый', str_list))
print(find(30, numeric_list))
print(find('fff', str_list))
