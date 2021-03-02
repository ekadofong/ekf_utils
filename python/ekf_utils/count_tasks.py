import re

catgories = {'W':'Writing','S':'Science','L':'Logistics','M':'Meeting'}

def count ( str_input ):
    tasks = str_input.splitlines()
    for task in tasks:
        category = re.findall(f'(?<=[)({''.joincategories.keys()})(?=])',
                              task)
        print(category)
