"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print("Please enter a valid name.")


my_dog = Dog("Nora", 8)

print("My dog is:", my_dog.get_name())

my_dog.set_name("Norita")

print("Her new name is:", my_dog.get_name())
'''
class Laptop:

    def __init__(self, name, model, year):
        self._name = name
        self.model = model
        self._year = year

    def get_name(self):
        return self._name

    def get_year(self):
        return self._year

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name

        else:
            print('Enter valid name')

    def set_year(self, new_year):
        if isinstance(new_year, int) and new_year.bit_length():
            self._name = new_year

        else:
            print('incorrect year')

my_laptop = Laptop('HP', 'probook 4340s', '2000')

print(my_laptop.get_name())
print('The name of my Laptop: ', my_laptop.get_name())

print(my_laptop.get_year())

my_laptop.set_name('Accer')

print('The new name of my laptop is:', my_laptop.get_name())

my_laptop.set_year(3039)

print('my new year name is:', my_laptop.get_name())