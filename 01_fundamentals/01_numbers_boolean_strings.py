# Numbers :- Integer, Floating Points and Complex numbers

num = 100  # 24 bytes
float_point = 3.1415926535   # 24 bytes
# Python follows the electrical engineering convention which uses j instead of i to denote iota
complex_num = complex(6, 8)  # 32 bytes
print(num, float_point, complex_num)

# Boolean:- The first letter of a bool needs to be capitalized in Python.
print(True, False)

# String
random_string = "This is MY Sample string!"

print(len(random_string))  # The Length of a String
print(random_string[-1])  # Reverse Indexing
print(random_string[1:3])  # String Slicing
print(random_string[0:7:2])  # String Slicing with Step
print(random_string[13:2:-1])  # Reverse Slicing
print(random_string[8:])  # Partial Slicing
print(random_string[::-1]) #  Whole String in reverse
