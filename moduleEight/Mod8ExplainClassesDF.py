class Student:
    def __init__(self, name, tag='student'):
        # protected attribute
        self._name = name
        # private attribute
        self.__tag = tag

    '''
    This is a PROTECTED method.
    Can only be accessed by this class
    or classes that inherit Student
    '''

    def _display_student_details_protected(self):
        print(f'I am a {self.__tag} and my name is {self._name}')
        print('I belong to a protected campus')

    '''
    This is a PRIVATE method.
    Can only be accessed by this class
    Can access this method only if someone
    knows the method name
    '''

    def __display_student_details_private(self):
        print()
        print("Name:", self._name, self.__tag)
        print(f'I am a {self.__tag} and my name is {self._name}')
        print('I reside with in campus and have access to ALL(private and protected)'
              '\nrecords without MANGLING')


class CsuStudent(Student):
    """
    This class inherits Student class
    """
    def display_details(self):
        print()
        # Accessing a semi-private attribute with mangled name
        print("Name:", self._name, self._Student__tag)
        # Accessing a protected method since this class inherits Student
        self._display_student_details_protected()
        print('I reside outside campus and have access to protected)'
              '\nand can only access private records with MANGLING.')


instance_of_student = Student('Manny')
# Accessing a semi-private method with mangled name
instance_of_student._Student__display_student_details_private()

instance_of_csu_student = CsuStudent('Jegan')
instance_of_csu_student.display_details()
