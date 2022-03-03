"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
from sympy.physics.units import force, velocity

'''
class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid radius.")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color.")

    color = property(get_color, set_color)


my_circle = Circle(10, "Blue")

# Radius
print(my_circle.radius)
my_circle.radius = 16
print(my_circle.radius)

my_circle.radius = 0
print(my_circle.radius)

# Color
print(my_circle.color)
my_circle.color = "Red"
print(my_circle.color)

my_circle.color = "White"
print(my_circle.color)
'''

'''
## In this code i will create a class called Momentum
## i will create its constructor using the init method
## The would have mass, velocity and force as instance attribute
## Then the force and velocity will be protected
## I will create a getter an setter for it 
## For every setter, i will create its corresponding property for it
## I will create instance of the Momentum and access the instance attributes
## Then i will change the values to confirm that the property is truly protecting them
also i will create fixed distances as a tuple
'''
class Momentum:

    MASS = 100

    def __init__(self, velocity, force):
        self._force = force
        self._velocity = velocity
        self.kinetic = 0.5*(Momentum.MASS * velocity**2)

    def get_force(self):
        self._force = force

    def set_force(self, newforce):
        if isinstance(newforce, float) and force > 0:
            self._force = newforce

        else:
            print('Please enter valid value force')

    force = property(get_force, set_force)

    def get_velocity(self):
        self._force = force

    def set_velocity(self, newvelocity):
        if isinstance(newvelocity, float) and velocity > 0:
            self._velocity = newvelocity

        else:
            print('Please enter the right value of the velocity')

    velocity = property(get_velocity, set_velocity)



my_momentum = Momentum(12.0, 10.0)

print(my_momentum.kinetic)

print(my_momentum.force)
print(my_momentum.MASS)
print(Momentum.MASS * (my_momentum.kinetic)**0.5)



