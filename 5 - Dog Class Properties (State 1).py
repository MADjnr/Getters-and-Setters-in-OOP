"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Dog:

    def __init__(self, age):
        self.age = age


my_dog = Dog(8)

print(f"My dog is {my_dog.age} years old.")
print("One year later...")

my_dog.age += 1

print(f"My dog is now {my_dog.age} years old.")
'''

class Cat:

    def __init__(self,age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, newage):
        if isinstance(newage, int) and 0 < newage < 30:
            self._age = newage

        else:
            print('Please enter the right age')

my_cat = Cat(39)

print(f'My cat is {my_cat.age} years old')
print('One year later...')

my_cat.age += 1

print(f'My cat is now {my_cat.age} years old')


