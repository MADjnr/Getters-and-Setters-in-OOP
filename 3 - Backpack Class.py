"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Backpack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")


my_backpack = Backpack()
print(my_backpack.get_items())

my_backpack.set_items("Hello, World!") # Invalid value
my_backpack.set_items(["Water Bottle", "Sleeping Bag", "First Aid Kit"])

print(my_backpack.get_items())
'''

class Bed:

    def __init__(self, bed_name, bed_size, bed_type):
        self._dimension = [] ##the leading underscore means that the attribute is protected
        self._bed_name = bed_name
        self.bed_size = bed_size
        self._bed_type = bed_type

    def get_dimension(self):
        return self._dimension

    def get_bed_name(self):
        return self._bed_name

    def get_bed_type(self):
        return self._bed_type

    def set_bed_name(self, new_bedname):
        if isinstance(new_bedname, str):
            self._bed_name = new_bedname

        else:
            print('Invalid bed name')

    def set_dimension(self, newdimension):
        if isinstance(newdimension, list):
            self._dimension = newdimension

        else:
            print('Enter the length and width as dimensions')

    def set_bed_type(self, newbedtype):
        if isinstance(newbedtype, int):
            self._bed_type = newbedtype

        else:
            print('enter the correct bedtype')



my_bed = Bed('lalofoam',30, 'waterbed')
print(my_bed.bed_size)



#my_bed.get_dimension()

my_bed.set_bed_name('Harofoam')

print('My new bed name is:', my_bed.get_bed_name())
