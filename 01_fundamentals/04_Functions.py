# Altering Data
"""
When mutable data is passed to a function, the function can modify or alter it.
These modifications will stay in effect outside the function scope as well.
In the case of immutable data, the function can modify it,
but the data will remain unchanged outside the function’s scope.
Examples of immutable data are numbers, strings, etc.
"""
mutable = ['a', 'e', 'i', 'o', 'u']
immuatable = ('a', 'e', 'i', 'o', 'u')
imm2 = "aeiou"


def checkMute(m, n, o):
    m[0] = 5
    # n[0] = 5 Not Allowed
    # o[0] = 5 Not Allowed
    m.append('X')
    o += 'X'
    print(m, n, o)


print(mutable, immuatable, imm2)
checkMute(mutable, immuatable, imm2)
print(mutable, immuatable, imm2)

#  Built-In Functions: find(), replace(), upper(), lower()

random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

a_string = "Welcome to Mockline!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

print("UpperCase".upper())
print("LowerCase".lower())

# Type Conversions: int(), ord(), float(), str(), bool()
print(ord('a'))
print(ord('0'))


# Lambda Functions
def triple(x): lambda num: num * 3  # Lambda PEP8
print(triple(10))
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

#  Functions as Arguments

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function
result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))