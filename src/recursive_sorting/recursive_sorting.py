# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # split the arr
        arr1 = merge_sort(arr[0: int(len(arr)/2)])
        arr2 = merge_sort(arr[int(len(arr)/2):])
        # merge the returned arrays
        return handle_merge(arr1, arr2)
    # return the sorted array
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

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
