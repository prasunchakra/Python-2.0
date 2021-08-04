"""
One of the major differences between functions and methods in Python is the first argument in the method definition.
This pseudo-variable provides a reference to the calling object,
that is the object to which the method or property belongs to.

Overloading refers to making a method perform different operations based on the nature of its arguments.
Unlike in other programming languages,
methods cannot be explicitly overloaded in Python but can be implicitly overloaded.

If we redefine a method several times and give it different arguments,
Python uses the latest method definition for its implementation.

Method Overloading: Increases Execution Speed, Implements Polymorphism, Same Method names saves memory, Cleaner Code
"""


class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")
print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")
print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
