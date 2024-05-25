"""
    List operations:
        1. Insert Operations --> Add single element at end, Add multiple elements at end, Add element based on position
        2. Update Operations --> Update element based on position,  order the list ascending, order the list descending
        3. Delete Operations --> Deleting single element at end, Delete element based on position,
                                 Delete element based on value
"""


def list_operations(list_students):
    print(' ' * 30, '*' * 35)
    print(' ' * 40, 'List Operations')
    print(' ' * 30, '*' * 35)

    print('-' * 110)
    print(' ' * 42, 'Insert Operations')
    print(' ' * 16, 'Add single element at end, Add multiple elements at end, Add element based on position ')
    print('-' * 110)

    # insertion of students using append(single element)
    list_students.append('student_five')
    print('\nStudent list after insertion -- Fifth element is added by using append().\n{}'.format(list_students))
    # insertion of students using extend(adding multiple elements)
    list_students.extend(['student_six', 'student_seven'])
    print('\nStudent list after insertion of multiple students-- '
          'Sixth and seventh element is added by using extend().\n{}'.format(list_students))
    list_students.insert(1, 'student_inserted_inbetween')
    print('\nStudent list after insertion of student @ index 1 -- '
          'Sixth and seventh element is added by using extend().\n{}'.format(list_students))

    print('\n' + '-' * 115)
    print(' ' * 42, 'Delete Operations')
    print(' ' * 16, 'Deleting single element at end, Delete element based on position, Delete element based on value ')
    print('-' * 115)

    # remove student
    list_students.pop()
    print('\nStudent list after update -- Fifth/last element is discarded using pop().\n{}'.format(list_students))
    # in-place modification of list
    list_students.pop(2)
    print('\nStudent list after in-place deletion -- third element in the list is deleted using pop(2).\n{}'.format(
        list_students))
    list_students.remove('student_six')
    print('\nStudent list after value based deletion using ''remove()'' -- element, \'student_six\' in the list '
          'is deleted using pop(\'student_six]\').\n{}'.format(
           list_students))

    print('\n' + '-' * 110)
    print(' ' * 42, 'Update Operations')
    print(' ' * 16, 'Update element based on position,  order the list ascending, order the list descending')
    print('-' * 110)

    # update students
    list_students[0] = 'student_one_updated'
    print('\nStudent list after update -- First element is updated using '
          'position/index(student_one --> student_one_updated).\n{}'
          .format(list_students))
    list_students.sort()
    print('\nStudent list after sorting in ascending manner .\n{}'
          .format(list_students))
    list_students.sort(reverse=True)
    print('\nStudent list after sorting in descending manner .\n{}'
          .format(list_students))


"""
    Dictionary operations:
        1. Insert Operations --> 'Add single element, Add multiple elements'
        2. Update Operations --> 'Update element based on key'
        3. Delete Operations --> 'Delete element based on key', 'Delete all the items'
        
"""


def dict_operations(students_dict):
    print('\n', ' ' * 34, '*' * 35)
    print(' ' * 40, 'Dictionary Operations')
    print(' ' * 34, '*' * 35)

    print('-' * 110)
    print(' ' * 42, 'Insert Operations')
    print(' ' * 30, 'Add single element, Add multiple elements')
    print('-' * 110)
    print()

    students_dict['student_six'] = {'name': 'Name_Six', 'id': 6}
    print_dict(students_dict)

    students_dict2 = {'student_seven': {'name': 'Name_Seven', 'id': 7},
                      'student_eight': {'name': 'Name_Eight', 'id': 8}}
    students_dict.update(students_dict2)
    print()
    print_dict(students_dict)

    print('-' * 110)
    print(' ' * 42, 'Update Operations')
    print(' ' * 36, 'Update element based on key')
    print('-' * 110)

    print('\nUpdate "student_six" value using key')
    students_dict['student_six'] = {'name': 'Name_SixtySix', 'id': 66}
    print_dict(students_dict)
    print('\nUpdate student_six\'s value using value\'s key(nested update using key value)')
    students_dict['student_six']['name'] = 77
    print_dict(students_dict)

    print('\nSort students dictionary lexicographically')
    sorted_dict = dict(sorted(students_dict.items()))
    print_dict(sorted_dict)

    print('-' * 110)
    print(' ' * 42, 'Delete Operations')
    print(' ' * 26, 'Delete element based on key & Delete all the items')
    print('-' * 110)

    print('\nDelete dictionary item with key = \'students_eight\'')
    students_dict.pop('student_eight')
    print_dict(students_dict)

    students_dict.clear()
    print('\nDictionary is cleared of all the elements')
    print('students_dict.clear() --> !!!Dictionary is empty!!!')
    print_dict(students_dict)


'''
    Print a dictionary with a next line every third element
'''


def print_dict(dictionary):
    i = 1
    for key, value in dictionary.items():
        if i % 3 == 0 or len(dictionary) == i:
            print('{} --> {}\n'.format(key, value), end='')
        else:
            print('{} --> {}'.format(key, value), end=', ')
        i += 1


if __name__ == "__main__":
    # Part One - Lists - List of CSU students
    students_list = ['student_one', 'student_two', 'student_three', 'student_four']
    students_details = {'students_one': {'name': 'Name_One', 'id': 1},
                        'students_two': {'name': 'Name_Two', 'id': 2},
                        'students_three': {'name': 'Name_Three', 'id': 3},
                        'students_four': {'name': 'Name_Four', 'id': 4},
                        'students_five': {'name': 'Name_Five', 'id': 5}
                        }
    list_operations(students_list)
    dict_operations(students_details)
