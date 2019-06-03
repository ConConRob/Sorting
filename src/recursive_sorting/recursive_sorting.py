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


for i in range(2, 4):
    print(i)

# test = [1, 5, 4, 1, 3, 2, 1, 231, 1, 2, 3]
# print(merge_sort_in_place(test, 0, len(test) - 1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
