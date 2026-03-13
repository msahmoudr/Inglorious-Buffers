import Quick_Sort


def kth_smallest(arr, k):
    n = len(arr)
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
