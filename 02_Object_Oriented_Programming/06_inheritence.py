"""
when do we use inheritance? Wherever we come across an IS A relationship between objects, we can use inheritance.

In Python, whenever we create a class, it is, by default, a subclass of the built-in Python object class.
Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
Child Class (Sub Class or Derived Class): This class inherits or extends the superclass.

super():- Accessing parent class properties, Calling the parent class methods
"""

class Vehicle:
    fuelCap = 100
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    fuelCap = 50
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
obj1.display()