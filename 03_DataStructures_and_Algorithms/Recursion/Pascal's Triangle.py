"""
Implement a function that takes a number and returns the row of the
Pascal’s triangle corresponding with that number.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
.........
"""


def pascal(n):
    if n == 0:
        return [1]
    else:
        line = [1]
        previous = pascal(n - 1)
        for i in range(len(previous) - 1):
            line.append(previous[i] + previous[i + 1])
        line += [1]
    return line


if __name__ == "__main__":
    n = 7
    print(pascal(n))
