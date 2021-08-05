"""
Maximum and minimum of an array using minimum number of comparisons
"""
def min_max(arr):
    imin, imax = arr[0], arr[0]
    for elem in arr:
        if elem < imin:
            imin = elem
        elif elem > imax:
            imax = elem
    return imin, imax


if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    print(min_max(arr))
