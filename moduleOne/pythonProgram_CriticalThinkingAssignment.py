def addition_subtraction(n1, n2):
    print('Sum of entered numbers -->', n1 + n2)
    print('Difference of entered numbers -->', n1 - n2)


def multiplication_division(n3, n4):
    print('Multiplying the entered numbers gives-->', n3 * n4)
    print('Dividing the entered numbers gives-->', n3 / n4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print('Part One - Addition and Subtraction')
        print('-----------------------------------')
        print()
        print('Enter the first number:', end='')
        numb1 = int(input())
        print('Enter the second number:', end='')
        numb2 = int(input())
        addition_subtraction(numb1, numb2)

        print('\n\nPart Two - Multiplication and Division')
        print('--------------------------------------')
        print()
        print('Enter the first number:', end='')
        numb3 = int(input())
        print('Enter the second number:', end='')
        numb4 = int(input())
        multiplication_division(numb3, numb4)
    except ZeroDivisionError as e:
        print("Divisor cannot be zero: ", e)
    except Exception as e:
        print("An error occurred: ", e)
