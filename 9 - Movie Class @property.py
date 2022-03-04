"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")


favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 4.5
print(favorite_movie.rating)

favorite_movie.rating = -5.6 # Invalid value.
print(favorite_movie.rating)
'''

# define a School class
#define the instance attributes
#make one of the instance attributes non-public
# use a property decorator for getter
# use a decorator for the setter

#class School(object):


class School:
    def __init__(self, name, location, population):
        self.name = name
        self._location = location
        self.population = population

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str) and len(new_location) == len(self._location):
            self._location = new_location

        else:
            print('Enter valid location')


my_school = School('University of Nigeria', 'Enugu', 19000)

print(my_school.name)
print(my_school.location)

my_school.location = 'opuka'

print(my_school.location)
