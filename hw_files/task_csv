import csv

# 1. Write a Python program to read each row from a given csv file and print a list of strings.
def read_rows(filename, delimiter):
    with open(filename) as file:
        data = csv.reader(file, delimiter=delimiter)
        for i in data:
            print(', '.join(i))


# 2. Write a Python program to read a given CSV file having tab delimiter.
def read_csv(filename):
    with open(filename) as file:
        data = csv.reader(file, delimiter='\t')
        for i in data:
            print(', '.join(i))


# 3. Write a Python program to read a given CSV file as a list.
def read_list(filename, delimiter):
    with open(filename) as file:
        data = list(csv.reader(file, delimiter=delimiter))
        print(data)


# 4. Write a Python program to read a given CSV file as a dictionary.
def read_dict(filename, delimiter):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = [row for row in reader]
        print(data)


# 5. Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces.
def remove_spaces(filename, delimiter):
    with open(filename) as file:
        data = csv.reader(file, delimiter=delimiter, skipinitialspace=True)
        for row in data:
            print(', '.join(row))


# 6. Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.
def clean_csv(filename, delimiter):
    with open(filename) as file:
        data = csv.reader(file, delimiter=delimiter, skipinitialspace=True, quotechar='"')
        for row in data:
            print(', '.join(row))


# 7. Write a Python program to read specific columns of a given CSV file and print the content of the columns.
def read_columns(file_path, column_indices):
    """Reads specific columns from a CSV file and returns their content."""
    selected_data = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Select only the specified columns
            selected_row = [row[index] for index in column_indices if index < len(row)]
            selected_data.append(selected_row)

    print(selected_data)


# 8. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the
# number of rows and the field names.
def read_and_skip(file_path):
    """Reads a CSV file, skips the header, and prints the field names and number of rows."""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        fieldnames = next(reader)
        row_count = 0
        data = []
        for row in reader:
            data.append(row)
            row_count += 1
    print("\nData Rows:")
    for index, row in enumerate(data):
        print(f"Row {index + 1}: {row}")
    return 'fieldnames:', fieldnames, 'number of rows:', row_count


# 9. Write a Python program to create an object for writing and iterate over the rows to print the values. AND 10.
# Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file
# and display the content.
def csv_list_write(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'Data written to {filename}')
    return open(filename, 'r').read()


# 11. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file
# and display the content.
def csv_dict_write(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()  # Write the header (column names)
        for i in range(len(data['ID'])):
            writer.writerow({field: data[field][i] for field in data.keys()})

    print(f'Data has been written to {filename}')
    with open(filename, mode='r') as file:
        reader = csv.reader(file)

        print("Contents of the CSV file:")
        for row in reader:
            print(row)


if __name__ == '__main__':
    print('#1')
    read_rows('countries.csv', ' ')
    print('___________')

    print('#2')
    read_csv('countries.csv')
    print('___________')

    print('#3')
    read_list('countries.csv', ' ')
    print('___________')

    print('#4')
    read_dict('countries.csv', ' ')
    print('___________')

    print('#5')
    remove_spaces('countries.csv', ' ')
    print('___________')

    print('#6')
    clean_csv('countries.csv', ' ')
    print('___________')

    print('#7')
    read_columns('departments.csv', [0, 1])
    print('___________')

    print('#8')
    print(read_and_skip('departments.csv'))
    print('___________')

    print('#9 and #10')
    data = [
        ['ID', 'Name', 'Age'],
        [1, 'Alice', 30],
        [2, 'Bob', 24],
        [3, 'Charlie', 28]
    ]
    print(csv_list_write('new.csv', data))
    print('___________')

    print('#10')
    data = {
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [30, 24, 28, 22]
    }
    csv_dict_write('new1.csv', data)
    print('___________')
