# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import Quick_Sort

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def kth_smallest(arr, k):
    n= len(arr)
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")

    return kth_smallest_helper(arr.copy, 0, n - 1, k)


def kth_smallest_helper(arr, low, high, k):
    """
    mix between quick sort partition and binary search
    """
    # lw one element
    if low == high:
        return arr[low]


    # htraga3 index element fe mkano el mazbot
    pivot_index = Quick_Sort.randomized_partition(arr, low, high)

    # Since array is 0-indexed, left size = pivot_index - low + 1
    left_size = pivot_index - low + 1

    if k == left_size:
        return arr[pivot_index]
    # nafs fekret el binary search
    elif k < left_size:
        return kth_smallest_helper(arr, low, pivot_index - 1, k)
    else:
        return kth_smallest_helper(arr, pivot_index + 1, high, k - left_size)
    
