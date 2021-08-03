def factorial(num):
    if num<=1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))


def isBalanced(str):
    count = 0
    for elem in str:
        if elem=="[":
            count += 1
        elif elem=="]":
            count -= 1
    return count == 0
print(isBalanced("[[[[][]]]]"))

