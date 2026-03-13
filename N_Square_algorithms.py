
import time

from Utilities import UTILITIES


class N_SQUARE_SORT:
    @staticmethod
    def bubble_sort_v4(arr): #cocktail shaker sort
        start_time = time.perf_counter()
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False


            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break
            swapped = False

            end = end - 1


            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start = start + 1

        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        return arr, execution_time_ms

    @staticmethod
    def selection_sort_bidirectional(arr):
        start_time = time.perf_counter()
        n = len(arr)
        left = 0
        right = n - 1

        while left < right:
            min_idx = left
            max_idx = left

            for i in range(left, right + 1):
                if arr[i] < arr[min_idx]:
                    min_idx = i
                if arr[i] > arr[max_idx]:
                    max_idx = i

            arr[left], arr[min_idx] = arr[min_idx], arr[left]

            if max_idx == left:
                max_idx = min_idx

            arr[right], arr[max_idx] = arr[max_idx], arr[right]

            left += 1
            right -= 1
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        return arr,execution_time_ms





    @staticmethod
    def insertion_sort_v3(arr):
        start_time = time.perf_counter()

        n = len(arr)

        for i in range(1, n):
            key = arr[i]

            insert_index = UTILITIES.binary_search_insertion(arr, key, 0, i)

            for j in range(i, insert_index, -1):
                arr[j] = arr[j - 1]

            arr[insert_index] = key

        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000

        return arr, execution_time_ms



