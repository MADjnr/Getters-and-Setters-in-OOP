"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid value for the radius.")


my_circle = Circle(5.0)

print(my_circle.get_radius())

my_circle.set_radius(0) # This will not change the value.
print(my_circle.get_radius())

my_circle.set_radius("Hello, World!") # This will not change the value.
print(my_circle.get_radius())

my_circle.set_radius(10.5) # This will change the value.
print(my_circle.get_radius())

'''
class Rectangle:

    #area = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.area = length * width

    def calculatearea(self):
        return self.area


    def get_length(self):
        return self._length

    def set_length(self, newlength):
        if isinstance(newlength, float) and newlength > 0:
            self._length = newlength

        else:
            print('Please enter a valid value of the length')

    def get_width(self):
        return self._width

    def set_width(self, newwidth):
        if isinstance(newwidth, float) and newwidth > 0:
            self._width = newwidth

        else:
            print('Please enter a valid value of the length')


my_rectangle = Rectangle(15, 27)

print(my_rectangle.get_width())
print(my_rectangle.get_length())
print('The value of my area is:', my_rectangle.calculatearea())
my_rectangle.set_width(34.0)
print('The new width is:', my_rectangle.get_width())

my_rectangle.set_length(24.0)
print('The new length is', my_rectangle.get_length())
print('The value of my new area is:', my_rectangle.get_width() * my_rectangle.get_length())


