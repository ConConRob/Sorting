# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty
    if arr[0] > target:
        return -1  # item looking for is too low
    if arr[len(arr) - 1] < target:
        return -1  # item looking for is too high
    low = 0
    high = len(arr)-1
    middle = int((high-low)/2 + low)
    # TO-DO: add missing code
    while high > low:
        middle = int(high/2)
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            # item is less than current middle
            high = middle
        else:
            # item is greater than current middle
            low = middle

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, dont=None, need=None):

    middle = int(len(arr)/2)

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    elif target == arr[middle]:
        print(arr)
        # found it
        return middle
    elif target < arr[middle]:
        # item is less than current middle
        return binary_search_recursive(arr[0: int(len(arr)/2)], target)
    elif target > arr[middle]:
        # item is less than current middle
        # add the number of index being sliced from the start of the array
        return int(len(arr)/2) + binary_search_recursive(arr[int(len(arr)/2):], target)


print(binary_search_recursive(
    [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -8))
