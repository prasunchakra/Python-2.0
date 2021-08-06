"""
Implement a function that takes two numbers and returns their greatest common divisor.
"""


def gcd(a, b):
    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


if __name__ == "__main__":
    number1 = 6
    number2 = 9
    print(gcd(number1, number2))

"""
The process of calculating GCD is as follows: 
If m>n, then GCD(m,n) is the same as GCD(m-n,n). 
This statement is based on the premise that if m/d and n/d both leave no remainder, 
then (m-n)/d also leaves no remainder.
"""
