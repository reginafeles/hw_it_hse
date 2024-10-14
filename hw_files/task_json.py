import json


# 1. Write a Python program to convert JSON data to Python object.
def convert_json_py(json_obj):
    json_obj = '{"extensions" : ["png", "jpg", "pdf"]}'
    py_obj = json.loads(json_obj)
    print('json:', json_obj)
    print('py', py_obj)


# 2. Write a Python program to convert Python object to JSON data.

def convert_py_json(py_obj):
    json_obj = json.dumps(py_obj)
    print('py', py_obj)
    print('json:', json_obj)


# 3. Write a Python program to convert Python objects into JSON strings. Print all the values.

def convert_all_json(py_obj):
    print('py', py_obj)
    for i in py_obj:
        print('json', json.dumps(i))


# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4.

def convert_dict_json(data):
    print('dict:', data)
    print('json:', json.dumps(data, sort_keys=True, indent=4))


# 5. Write a Python program to convert JSON encoded data into Python objects.
def convert_all_py(json_obj):
    for i in json_obj:
        print(type(json.loads(i)))


# 6. Write a Python program to create a new JSON file from an existing JSON file.

def create_json(filename, key, value):
    with open(filename, 'r') as f:
        student_data = json.load(f)

    student_data[key] = value
    print(student_data)

    with open(filename, 'w') as f:
        json.dump(student_data, f, indent=2)
        print(f'Done!\n{key} and {value} added')


# 7. Write a Python program to check whether an instance is complex or not.

def check_complex(data):
    if isinstance(data, dict):
        if 'complex' in data:
            try:
                if 'real' in data['complex'] and 'imag' in data['complex']:
                    return complex(data['complex']['real'], data['complex']['imag'])
            except TypeError:
                return any(check_complex(value) for value in data.values())
        return any(check_complex(value) for value in data.values())
    elif isinstance(data, list):
        return any(check_complex(element) for element in data)
    elif isinstance(data, complex):
        return data
    else:
        return False


# 8. Write a Python program to check whether a JSON string contains complex object or not.

def check_complex_json(json_data):
    parsed = json.loads(json_data)
    return check_complex(parsed)


# 9. Write a Python program to access only unique key value of a Python object.

def access_unique(data):
    print('data:', data)
    json_data = json.loads(data)
    print('result:', json_data)


if __name__ == '__main__':
    print('#1')
    json_obj = '{"extensions" : ["png", "jpg", "pdf"]}'
    convert_json_py(json_obj)
    print('__________')

    print('#2')
    py_obj = {'extensions': ['png', 'jpg', 'pdf']}
    convert_py_json(py_obj)
    print('__________')

    print('#3')
    py_obj = [{"extensions": ["png", "jpg", "pdf"]}, [1, 2, 3], 'string', 1, 1.5, True, False, None]
    convert_all_json(py_obj)
    print('__________')

    print('#4')
    data = {'Kate': 22, 'Vlad': 25, 'Masha': 23}
    convert_dict_json(data)
    print('__________')

    # creating new json for tasks
    with open('new.json', 'w') as f:
        json.dump(data, f, indent=2)

    print('#5')
    json_obj = ['{"extensions" : ["png", "jpg", "pdf"]}', '[1, 2, 3]', '"string"', '1', '1.5', 'true', 'false', 'null']
    convert_all_py(json_obj)
    print('__________')

    print('#6')
    create_json('new.json', 'Vera', 22)
    print('__________')

    print('#7')
    result_true = check_complex({'complex': {'real': 3, 'imag': 4}})
    result_false = check_complex({'name': 'Volodya'})
    print('Complex:', result_true)
    print('Complex:', result_false)
    print('__________')

    print('#8')
    json_true = '{"value": "Hello", "number": [1, 2, 3], "complex": {"real": 3, "imag": 4}}'
    json_false = '{"value": "Hello", "number": [1, 2, 3]}'
    print('Complex:', check_complex_json(json_true))
    print('Complex:', check_complex_json(json_false))
    print('__________')

    print('#9')
    data = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
    access_unique(data)
    print('__________')

