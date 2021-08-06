"""
Write a function that takes a number and returns a string that is its equivalent binary number.
"""


def decimal_to_binary(n):
    if n <= 1:
        return str(n)

    else:
        print(decimal_to_binary(n // 2) + decimal_to_binary(n % 2), decimal_to_binary(n // 2) , decimal_to_binary(n % 2))
        return decimal_to_binary(n // 2) + decimal_to_binary(n % 2)


if __name__ == "__main__":
    n = 11
    print("$$",decimal_to_binary(n))
