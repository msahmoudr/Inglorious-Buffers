import random
import time


def quick_sort(arr, low, high):

    if low < high:
        # Get the partition index (pivot's final position)
        pivot_index = randomized_partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr


def randomized_partition(arr, low, high):
    """
    Step 1: bageeb el random pivot fe el a5er
    Step 2: then get to business
    """

    random_pivot = random.randint(low, high)

    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]
    return partition(arr, low, high)


def partition(arr, low, high):
    """
    Standard Lomuto partition scheme.
    Pivot is the last element (after randomization).
    """


    pivot = arr[high]
    left_ptr = low
    right_ptr = high
    while(left_ptr < right_ptr):
        while(arr[left_ptr]<=pivot and left_ptr < right_ptr):
            left_ptr = left_ptr + 1
        while(arr[right_ptr]>=pivot  and left_ptr < right_ptr):
            right_ptr = right_ptr - 1
        

    #
    # # Index of smaller element (indicates correct position of pivot so far)
    # i = low - 1
    #
    # for j in range(low, high):
    #     # If current element is smaller than or equal to pivot
    #     if arr[j] <= pivot:
    #         # Increment index of smaller element
    #         i += 1
    #         arr[i], arr[j] = arr[j], arr[i]  # Swap
    #
    # # Place pivot in its correct position
    # arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #
    # # Return the partition index
    # return i + 1


def sort(arr):

    if len(arr) <= 1:
        return arr
    return quick_sort(arr.copy(), 0, len(arr) - 1)


def sort_inplace(arr):
    if len(arr) <= 1:
        return arr
    return quick_sort(arr, 0, len(arr) - 1)