import random


def partition(data):
    left = []
    pivot = data[0]
    right = []
    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right


def quick_sort(data):
    # pivot
    if data == []:
        return data
    left, right, pivot = partition(data)
    # recursively quick sort lHS and RHS
    return quick_sort(left) + [pivot] + quick_sort(right)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # split the arr
        arr1 = merge_sort(arr[0: int(len(arr)/2)])
        arr2 = merge_sort(arr[int(len(arr)/2):])
        # merge the returned arrays
        return handle_merge(arr1, arr2)
    # return the sorted array -> when array length is 1
    return arr

# must have 2 sorted lists


def handle_merge(arr1, arr2):
    index1 = 0
    while index1 < len(arr1) and len(arr2):
        if arr2[0] < arr1[index1]:
            # removes item from arr2 and puts it in
            arr1.insert(index1, arr2.pop(0))
        # goes to the next index
        # no else because if new item is added to this index we still want to go to next
        index1 += 1
    arr1.extend(arr2)
    return arr1


# print(handle_merge([7], [1, 1]))
# print(merge_sort([2, 1, 1, 2, 2, 1]))
# STRETCH: implement an in-place merge sort algorithm

def merge_in_place(arr, start, mid, end):
    # TO-DO
    #
    # merge items on either side of the mid
    # loop each of right side trying to merge into left
    if start == mid:
        # just compare start and end and maybe switch
        if arr[end] < arr[start]:
            #  insert it before current left and remove it old spot from array
            arr.insert(start, arr[end])
            arr.pop(end + 1)  # add 1 because index was shifted
    l_i = start
    for r_i in range(mid, end):
        # loop the left side using current l_i
        while l_i < mid:
            # if current right is less then current left
            if arr[r_i] < arr[l_i]:
                #  insert it before current left and remove it old spot from array
                arr.insert(l_i, arr[r_i])
                arr.pop(r_i + 1)  # add 1 because index was shifted
                # leave the loop
                # move the mid over
                mid += 1
                break
            l_i += 1
    return arr

# l = left, r = right


def merge_sort_in_place(arr, l, r):
    # TO-DO
    # if length greater then 1 split
    mid = (r-l)//2 + l
    if r - l > 1:
        # lower half
        merge_sort_in_place(arr, l, mid)
        # higher half
        merge_sort_in_place(arr, mid, r)
        # merge the current looking at array
    merge_in_place(arr, l, mid, r)
    return arr


# test = [1, 5, 4, 1, 3, 2, 1, 231, 1, 2, 3]
# print(merge_sort_in_place(test, 0, len(test) - 1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


# make array into chunks of 32 to 64 items and use insertion sort.
# then
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def timsort(arr):
    arr1 = None
    arr2 = None
    # base case
    if len(arr) <= 64:
        return insertionSort(arr)

    # if arr is larger then 32 items take off 32 items and do insertion sort
    if len(arr) > 128:
        # split off 64 long piece
        arr1 = timsort(arr[:64])
        arr2 = timsort(arr[64:])
    elif len(arr) > 64:
        # dived arr in half
        mid = (len(arr)-1)//2
        arr1 = timsort(arr[:mid])
        arr2 = timsort(arr[mid:])
    # merge sort left and right part of array

    return handle_merge(arr1, arr2)


test = random.sample(range(1000), 1000)
print(timsort(test))
