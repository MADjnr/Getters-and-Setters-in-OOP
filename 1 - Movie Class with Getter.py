"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


my_movie = Movie("The Godfather", 4.8)

print(my_movie.title) # Throws an error

print(my_movie.get_title())
print("My favorite movie is:", my_movie.get_title())
'''

class Vehicle:

    def __init__(self, name, model, color):
        self._name = name ## i made the name to be non_public
        self.model = model
        self.color = color

    def get_title(self):
        return self._name


my_car = Vehicle('Tesla', 'model y', 'green')
print(my_car.get_title())
print('My favourite car is:', my_car.get_title())



