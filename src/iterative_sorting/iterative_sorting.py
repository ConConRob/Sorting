# TO-DO: Complete the selection_sort() function below
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

    return arr


print(bubble_sort([5, 4,  123123, 3, 2, 1]))
