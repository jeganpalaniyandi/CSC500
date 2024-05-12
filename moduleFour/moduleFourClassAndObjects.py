"""
ItemToPurchase class has a default constructor with three parameters
initialized with three parameters with default values as none, 0 & 0.

The class has two methods,

1. add_print_list - returns the item name, count and price formatted.
                    This is used by list in the main method that prints
                    all the items to the receipt.

2. calculate_item_price - returns item_price by multiplying price and
                          count of item.

"""


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def add_print_list(self):
        return '{:<18} --> {:>6.2f}$'.format(self.item_name + ' x ' + str(self.item_quantity), self.item_price*self.item_quantity)

    def calculate_item_price(self):
        return self.item_price * self.item_quantity


if __name__ == '__main__':

    # itemList saves all the formatted item, count and item price
    # returned from add_print_list list
    itemList = []
    totalCost = 0.00

    # This program is designed only for two items
    # If needed, we can leverage this program to
    # loop for the total number of items

    for i in range(0, 2):

        print(f'\nEnter item {i+1} details:')
        print('-'*30)
        name = input('Enter item name --> ')
        price = float(input('Enter item price($) --> '))
        quantity = int(input('Enter item quantity --> '))

        item = ItemToPurchase(name, price, quantity)
        itemList.append(item.add_print_list())
        totalCost += item.calculate_item_price()

    """
        Following section prints the receipt by looping the 
        'itemList' and print the total cost at the bottom using
        'totalCost' variable
    """

    print()
    print('*' * 32)
    print(' ' * 12 + 'TOTAL COST')
    print('*' * 32 + '\n')

    for local_item in itemList:
        print(local_item)

    print('-' * 32)
    print('Total  {:>22.2f}$'.format(totalCost))
    print('-' * 32)
