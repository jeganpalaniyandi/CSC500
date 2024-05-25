class ItemToPurchase:
    """
    ItemToPurchase class has a default constructor with three parameters
    initialized with three parameters with default values as
        item_name = none
        item_price = 0 &
        item_quantity= 0.

    The class has two methods,

    1. add_print_list - returns the item name, count and price formatted.
                        This is used by list in the main method that prints
                        all the items to the receipt.

    2. calculate_item_price - returns item_price by multiplying price and
                              count of item.

    """

    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def add_print_list(self):
        return '{:<32} --> {:>6.2f}$'.format(self.item_name + ' x ' + str(self.item_quantity),
                                             self.item_price * self.item_quantity)

    def calculate_item_price(self):
        return self.item_price * self.item_quantity


class ShoppingCart:
    """
        Class: ShoppingCart
        Constructor:
            non-default params:
                cart_items -> List
            Default params:
                customer_name='none'
                current_date='January 1, 2020'
    """

    def __init__(self, cart_items, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        self.available_items = {'Nike Romaleos': 'Volt color, Weightlifting shoes',
                                'Chocolate Chips': 'Semi - sweet',
                                'Powerbeats 2 Headphones': 'Bluetooth headphones'
                                }
        self.total_cost = 0

    def add_item(self):
        """
             'add_item' handles adding a new item to shopping cart
             It prompts the user to enter the item name, price and quantity
             and saves it to a list which saves itemToPurchase object.
         """
        print(f'\nEnter item details:')
        print('-' * 19)
        name = input('Enter item name --> ')
        price = float(input('Enter item price($) --> '))
        quantity = int(input('Enter item quantity --> '))

        item = ItemToPurchase(name, price, quantity)
        self.cart_items.append(item)
        print('{} {}(s) priced at ${:.2f} added successfully to cart.'.format(quantity, name, price))

    def remove_item(self):
        """
            print('Item not found in cart. Nothing removed.')
        """

    def modify_item(self):
        """
           If item can be found (by name) in cart,
           check if parameter has default values for description, price,
           and quantity. If not, modify item in cart.
           If item cannot be found (by name) in cart,
           output this message: Item not found in cart. Nothing modified.
        """

    def get_num_items_in_cart(self):
        """
            :return:# of items in the shopping cart
        """
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        """
            Outputs total of objects in cart.
            If cart is empty, output this message: SHOPPING CART IS EMPTY
            :return: none
        """

        for item in self.cart_items:
            self.total_cost += item.calculate_item_price()

        # Following section prints the receipt by looping the
        # 'itemList' and print the total cost at the bottom using
        # 'totalCost' variable

        print('-' * 44)
        print('Total  {:>36.2f}$'.format(self.total_cost))
        print('-' * 44)

    def print_total(self):
        """
            prints the total cost of items in cart. Has no parameters.
            :return:none
        """
        print()
        print('*' * 44)
        print(' ' * 12 + '{}\'s Shopping Cart'.format(self.customer_name))
        print(' ' * 16 + '{}'.format(self.current_date))
        print('*' * 44)
        print('{:^44}\n'.format('Total # of items :  ' + str(self.get_num_items_in_cart())))

        for item in self.cart_items:
            print(item.add_print_list())

    def print_descriptions(self):
        """
            prints available items and descriptions in the mart
            :return:none
        """
        print('\n{:>55}'.format('Available Items and Descriptions'))
        print('-' * 88)
        print('|{:>32}        |{:>34}           |'.format('ITEM', 'DESCRIPTION'))
        print('-' * 88)
        for l_item, desc in self.available_items.items():
            print('|{:>32}        |{:>34}           |'.format(l_item, desc))
        print('-' * 88)

    def output_cart(self):
        """
            prints the list of items with their total price
            and at the bottom prints the
            :return:
        """
        if self.get_num_items_in_cart():
            self.print_total()
            self.get_cost_of_cart()
        else:
            print('SHOPPING CART IS EMPTY')


def print_menu_options():
    """
         Prints Menu with options and
         prompt the user to enter an option
        :return: shopping cart options menu
    """
    menu_options = ['a - Add item to cart', 'r - Remove item from cart', 'c - Change item quantity',
                    'i - Output items\'s descriptions', 'o - Output shopping cart', 'q - Quit']
    print()
    for l_option in menu_options:
        print(f'{l_option:^80}')

    selected_option = input('{:>49}'.format('Choose an option: '))
    return selected_option


if __name__ == '__main__':

    # Print CSU groceries banner

    print('*' * 100)
    print(' ' * 25, 'CSU Groceries - User-friendly Online Shopping')
    print('*' * 100)

    # Get and print user and date

    user_name = input('\nEnter your name : ')
    today_date = input('Enter today\'s date as <Month> <date>, <year> : ')
    print('\n{:>50} \'{}\''.format('Welcome valued customer', user_name))
    print('{:>42} {}'.format('Shopping date :', today_date))

    # Create and Initialize an empty shopping cart with entered username and date

    user_cart_items = []
    user_cart = ShoppingCart(user_cart_items, user_name, today_date)

    # Print Menu for options until user enters 'q'

    option_selected = ''
    while option_selected != 'q':
        if option_selected == 'a':
            user_cart.add_item()
        elif option_selected == 'i':
            user_cart.print_descriptions()
        elif option_selected == 'o':
            user_cart.output_cart()
        option_selected = print_menu_options()
