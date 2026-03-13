import random
import time


def quick_sort(arr, low, high):

    if low < high:

        pivot_index = randomized_partition(arr, low, high)


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
2 pointers
    """


    pivot = arr[high]
    left_ptr = low
    right_ptr = high-1
    while(left_ptr <= right_ptr):
        while left_ptr <= right_ptr and arr[left_ptr] <= pivot:
            left_ptr += 1
        while left_ptr <= right_ptr and arr[right_ptr] >= pivot:
            right_ptr -= 1

        if left_ptr < right_ptr:
            arr[left_ptr],arr[right_ptr] = arr[right_ptr],arr[left_ptr]

    arr[high], arr[left_ptr] = arr[left_ptr], arr[high]
    return left_ptr


def sort(arr):

    if len(arr) <= 1:
        return arr
    return quick_sort(arr.copy(), 0, len(arr) - 1)


def sort_inplace(arr):
    if len(arr) <= 1:
        return arr
    return quick_sort(arr, 0, len(arr) - 1)