"""
Public attributes are those that can be accessed inside the class and outside the class.
Technically in Python, all methods and properties in a class are publicly available by default.

Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.
We can make members private using the double underscore __ prefix
To ensure that no one from the outside knows about this private property, the error does not reveal its identity.

Methods are usually public since they provide an interface for the class properties
and the main code to interact with each other.

It is not common to have private variables in Python.
If the user believes it is absolutely necessary to access a private property or a method,
they can access it using the _<ClassName> prefix for the property or method.
Python does not have the protected access modifier.
"""

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
Steve.displaySalary()
#Steve.__displayID()   this will generate an error
#print("Salary:", Steve.__salary)  this will cause an error
print(Steve._Employee__salary)  # accessing a private property
