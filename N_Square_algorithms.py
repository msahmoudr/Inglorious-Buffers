
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


if __name__ == "__main__":

    headers = [
        "Array Size",
        "Bubble V1 (ms)", "Bubble V2 (ms)", "Bubble V3 (ms)", "Bubble V4 Cocktail (ms)",
        "Selection Standard (ms)", "Selection Bidirectional (ms)", "Selection Stable (ms)",
        "Insertion V1 (ms)", "Insertion V2 (ms)", "Insertion V3 Binary (ms)", "Insertion V4 Shell (ms)"
    ]

    UTILITIES.add_record_to_csv_File(headers)


    sizes_to_test = [2 ** i for i in range(1, 10)]



    for size in sizes_to_test:
        print(f"--- Testing Array Size: {size} ---")


        master_array = UTILITIES.generate_random_array(size)
        print("  Running Bubble Sorts...")
        _, t_bub1 = SORT.bubble_sort_v1(master_array.copy())
        _, t_bub2 = SORT.bubble_sort_v2(master_array.copy())
        _, t_bub3 = SORT.bubble_sort_v3(master_array.copy())
        _, t_bub4 = SORT.bubble_sort_v4(master_array.copy())
        print("  Running time for bubble sort v1 is {}".format(t_bub1))
        print("  Running time for bubble sort v2 is {}".format(t_bub2))
        print("  Running time for bubble sort v3 is {}".format(t_bub3))
        print("  Running time for bubble sort v4 is {}".format(t_bub4))

        print("  Running Selection Sorts...")
        _, t_sel1 = SORT.selection_sort_standard(master_array.copy())
        _, t_sel2 = SORT.selection_sort_bidirectional(master_array.copy())
        _, t_sel3 = SORT.selection_sort_stable(master_array.copy())
        print("  Running time for selection sort standard is {}".format(t_sel1))
        print("  Running time for selection sort bidirectional is {}".format(t_sel2))
        print("  Running time for selection sort stable is {}".format(t_sel3))


        print("  Running Insertion Sorts...")
        _, t_ins1 = SORT.insertion_sort_v1(master_array.copy())
        _, t_ins2 = SORT.insertion_sort_v2(master_array.copy())
        _, t_ins3 = SORT.insertion_sort_v3(master_array.copy())
        _, t_ins4 = SORT.insertion_sort_v4(master_array.copy())
        print("  Running time for insertion sort v1 is {}".format(t_ins1))
        print("  Running time for insertion sort v2 is {}".format(t_ins2))
        print("  Running time for insertion sort v3 is {}".format(t_ins3))
        print("  Running time for insertion sort v4 is {}".format(t_ins4))


        row_data = [
            size,
            t_bub1, t_bub2, t_bub3, t_bub4,
            t_sel1, t_sel2, t_sel3,
            t_ins1, t_ins2, t_ins3, t_ins4
        ]


        UTILITIES.add_record_to_csv_File(row_data)
        print(f"  -> Finished size {size}. Data saved to CSV.\n")
