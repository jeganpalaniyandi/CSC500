# This function calculates and print the total cost including tip and tax
def display_total_cost(meal_charge):
    # 18 percent tip
    # 7 percent sales tax
    calculated_tip = meal_charge * 0.18
    calculated_tax = meal_charge * 0.07

    # Total Cost = meal charge + 18% tip + 7% Sale tax
    total_cost = meal_charge + calculated_tip + calculated_tax

    print(f'\nMeal charge --> $ {format_dollars(meal_charge)}')
    print(f'    18% tip --> $ {format_dollars(calculated_tip)}')
    print(f'     7% tax --> $ {format_dollars(calculated_tax)}')
    print('-' * 24)
    print(f' Total Cost --> $ {format_dollars(total_cost)}')


# This function formats the given amount for equal indentation in the receipt
def format_dollars(amount):
    # format amounts to 6 places with first three places for whole number
    # and last three places for .(dot) and two fractional numbers
    formatted_number = "{: >6.2f}".format(amount)
    return formatted_number


if __name__ == '__main__':
    print()
    print('*' * 65)
    print(' ' * 14 + 'MODULE THREE ASSIGNMENT - PART ONE')
    print(' ' * 16 + '(MEALS TOTAL COST CALCULATOR)')
    print('*' * 65)

# Get the meal charge from user
user_charge = float(input('\nEnter the meal charge: '))

# Validate the user charge entered
if user_charge < 10 or user_charge > 30:
    print('\nEntered charge is out of range with average price. Please re-run the program and enter correct charge.')
    exit(4)

# Calculate and display the receipt including tax and tips
display_total_cost(user_charge)
