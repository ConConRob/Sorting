# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        print(arr[cur_index])
        for left_index in range(0, cur_index):
            print(f'left: {arr[left_index]}  smallest: {arr[smallest_index]}')
            if(arr[left_index] < arr[smallest_index]):
                smallest_index = left_index
        # TO-DO: swap
        current = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = current
    return arr


print(selection_sort([3, 2, 1, 4]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
