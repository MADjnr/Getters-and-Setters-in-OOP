"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")


my_backpack = Backpack()
print(my_backpack.items)

my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)

my_backpack.items = "Hello, World!" # Invalid value.
print(my_backpack.items)
'''

## Define a class for the backpack
## Define the constructor but make the item non public
## build the getter method using @property
## build the setter method using @property_name.setter
## check if the items is a list

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    ##building the setter
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list) and len(new_items) <= 7:
            self._items = new_items

        else:
            print('The items are invalid')

my_backpack = Backpack()

my_backpack.items = ['banana', 'oranges', 'mango']
print(my_backpack.items[2])

my_backpack.items.append('yoha')

print(my_backpack.items)

