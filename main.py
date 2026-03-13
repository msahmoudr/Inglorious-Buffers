# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

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



