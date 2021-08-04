"""
Information hiding refers to the concept of hiding the inner workings of a class
and simply providing an interface through which the outside world can interact with the class
without knowing what’s going on inside.

Encapsulation in OOP refers to binding data and the methods
to manipulate that data together in a single unit, that is, class.

A getter method allows reading a property’s value.
A setter method allows modifying a property’s value.
For encapsulating a class, all the properties should be private
and any access to the properties should be through methods such as getters and setters.
"""

class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())