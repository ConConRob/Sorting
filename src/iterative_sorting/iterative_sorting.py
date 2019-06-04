# TO-DO: Complete the selection_sort() function below
import random


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for right_index in range(cur_index, len(arr)):
            if(arr[right_index] < arr[smallest_index]):
                smallest_index = right_index
        # TO-DO: swap
        current = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = current
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    is_not_sorted = True
    while is_not_sorted:
        is_not_sorted = False
        # loop all elements
        for cur_index in range(0, len(arr) - 1):
            # check the next el
            if arr[cur_index] > arr[cur_index + 1]:
                # is_not_sorted
                is_not_sorted = True
                # switch and loop
                current = arr[cur_index]
                arr[cur_index] = arr[cur_index + 1]
                arr[cur_index + 1] = current
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # find max if max not given
    if maximum == -1:
        for num in arr:
            if num > maximum:
                maximum = num
    # make array of zeros up to max the zero index is counts of zero so + 1
    count = [0 for i in range(maximum + 1)]
    # count each number
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1

    for i in range(1, maximum + 1):
        # add previous count to current
        count[i] += count[i - 1]

    # shift the array right
    for i in reversed(range(1, maximum + 1)):
        count[i] = count[i - 1]
    # set index zero to be zero
    if len(arr) > 0:
        count[0] = 0
    # count now has the starting indexs so map them
    for i in range(maximum + 1):
        # cover end case
        if i == maximum:
            for j in range(count[i], len(arr)):
                arr[j] = i
        else:
            for j in range(count[i], count[i+1]):
                arr[j] = i
    return arr
