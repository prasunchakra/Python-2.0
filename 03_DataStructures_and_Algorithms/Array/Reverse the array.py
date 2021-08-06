"""
Given an array (or string), the task is to reverse the array/string.
"""


def linear(inp):
    first = 0
    last = len(inp) - 1
    while (first < last):
        inp[first], inp[last] = inp[last], inp[first]
        first += 1
        last -= 1


def recursive(inp, first, last):
    if not first < last:
        return
    inp[first], inp[last] = inp[last], inp[first]
    recursive(inp, first + 1, last - 1)


if __name__ == "__main__":
    Input = [4, 5, 1, 2]
    linear(Input)
    print(Input)
    recursive(Input,0,3)
    print(Input)
