class UserDefinedMethods:

    def __init__(self, mobile_number: list):
        self.mobile_number = mobile_number

    def add_special_mobile_number(self):
        """
        Calculates the sum of mobile numbers which contains alphabets.
        Alphabets will be converted to its unicode before performing the sum
        return:Sum of numbers + unicode values of alphabets in the list
        """
        sum_digits = 0
        for digit in self.mobile_number:
            if type(digit) is int:
                sum_digits += digit
            else:
                sum_digits += ord(digit)

        return sum_digits


if __name__ == '__main__':
    typical_mobile_number = [3, 0, 3, 4, 6, 6, 2, 6, 5, 1]
    special_case_mobile_number = [3, 0, 3, 'I', 'A', 'M', 'D', 'I', 'F', 'F']

    print(f'Sum of typical phone number using inbuilt function --> {sum(typical_mobile_number)}')

    # Create an instance to call the method which returns sum of special
    # numbers with alphabets and utilize its add_special_mobile_number

    udm = UserDefinedMethods(special_case_mobile_number)
    print(f'Sum of special phone number using inbuilt function --> {udm.add_special_mobile_number()}')
