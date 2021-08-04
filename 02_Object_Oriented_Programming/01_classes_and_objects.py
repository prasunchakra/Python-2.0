# Classes, Objects, Initializer, Class variable, Instance variable

class Player:
    teamName = 'Liverpool'  # class variables
    teamMembers = []

    def __init__(self, name, age=0):
        self.name = name  # creating instance variables
        self.age = age
        self.teamMembers.append(self.name)


p1 = Player('Mark', 35)
p2 = Player('Steve')

print("Name:", p1.name)
print("Age:", p1.age)
print("Team Name:", p1.teamName)
print(p1.teamMembers)
print("Name:", p2.name)
print("Age:", p2.age)
print("Team Name:", p2.teamName)
print(p2.teamMembers)
