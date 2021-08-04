"""
Class methods work with class variablesClass methods are accessed using the class name
and can be accessed without creating a class object.
To declare a method as a class method, we use the decorator @classmethod.
cls is used to refer to the class just like self is used to refer to the object of the class.

Static methods are methods that are usually limited to class only and not their objects.
They have no direct relation to class variables or instance variables.
They are used as utility functions inside the class or when we do not want the inherited classes
to modify a method definition.
To declare a method as a static method, we use the decorator @staticmethod.
It does not use a reference to the object or class, so we do not have to use self or cls.
"""


class Player:
    teamName = 'India'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @staticmethod
    def demo():
        return "2011 Cricket World Cup"


p1 = Player("Nolan")
print(Player.getTeamName())
print(Player.demo())
print(p1.getTeamName())
print(p1.demo())

