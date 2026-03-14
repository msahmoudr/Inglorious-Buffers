import time
from Utilities import UTILITIES
from N_Square_algorithms import N_SQUARE_SORT
from Merge_Sort import MERGE_SORT
from Quick_Sort import sort_inplace as quick_sort_run
from Heap_sort import HeapSort
from Hybrid_Merge_Sort import hybrid_merge_sort

if __name__ == "__main__":

    headers = [
        "Array Size",
        "Bubble V3 (ms)",
        "Selection Bidirectional (ms)",
        "Insertion V3 Binary (ms)",
        "Merge Sort (ms)",
        "Hybrid Merge Sort (ms)",
        "Quick Sort (ms)",
        "Heap Sort (ms)"
    ]

    UTILITIES.add_record_to_csv_File(headers)

    sizes_to_test = [2 ** i for i in range(1, 10)]

    for size in sizes_to_test:
        print(f"--- Testing Array Size: {size} ---")

        master_array = UTILITIES.generate_random_array(size)

        # --- O(N^2) ALGORITHMS ---
        print("  Running N^2 Sorts...")

        arr_bub3, t_bub3 = N_SQUARE_SORT.bubble_sort_v4(master_array.copy())
        is_bub3_sorted = UTILITIES.is_sorted(arr_bub3)
        print(f"  Running time for bubble sort v3 is {t_bub3:.3f} ms | Sorted: {is_bub3_sorted}")

        arr_sel2, t_sel2 = N_SQUARE_SORT.selection_sort_bidirectional(master_array.copy())
        is_sel2_sorted = UTILITIES.is_sorted(arr_sel2)
        print(f"  Running time for selection sort bidirectional is {t_sel2:.3f} ms | Sorted: {is_sel2_sorted}")

        arr_ins3, t_ins3 = N_SQUARE_SORT.insertion_sort_v3(master_array.copy())
        is_ins3_sorted = UTILITIES.is_sorted(arr_ins3)
        print(f"  Running time for insertion sort v3 is {t_ins3:.3f} ms | Sorted: {is_ins3_sorted}")

        # --- O(N log N) ALGORITHMS ---
        print("  Running O(N log N) Sorts...")

        # Merge Sort
        arr_copy = master_array.copy()
        start_time = time.perf_counter()
        MERGE_SORT.merge_sort(arr_copy, 0, len(arr_copy) - 1)
        t_merge = (time.perf_counter() - start_time) * 1000
        is_merge_sorted = UTILITIES.is_sorted(arr_copy)
        print(f"  Running time for merge sort is {t_merge:.3f} ms | Sorted: {is_merge_sorted}")

        # Hybrid Merge Sort
        arr_copy = master_array.copy()
        start_time = time.perf_counter()
        hybrid_merge_sort.hybrid_merge_sort(arr_copy, 0, len(arr_copy) - 1, threshold=15)
        t_hybrid = (time.perf_counter() - start_time) * 1000
        is_hybrid_sorted = UTILITIES.is_sorted(arr_copy)
        print(f"  Running time for hybrid merge sort is {t_hybrid:.3f} ms | Sorted: {is_hybrid_sorted}")

        # Quick Sort
        arr_copy = master_array.copy()
        start_time = time.perf_counter()
        quick_sort_run(arr_copy)
        t_quick = (time.perf_counter() - start_time) * 1000
        is_quick_sorted = UTILITIES.is_sorted(arr_copy)
        print(f"  Running time for quick sort is {t_quick:.3f} ms | Sorted: {is_quick_sorted}")

        # Heap Sort
        arr_copy = master_array.copy()
        hs = HeapSort()
        start_time = time.perf_counter()
        hs.heapsort(arr_copy)
        t_heap = (time.perf_counter() - start_time) * 1000
        is_heap_sorted = UTILITIES.is_sorted(arr_copy)
        print(f"  Running time for heap sort is {t_heap:.3f} ms | Sorted: {is_heap_sorted}")

        # Data serialization
        row_data = [
            size,
            t_bub3,
            t_sel2,
            t_ins3,
            t_merge,
            t_hybrid,
            t_quick,
            t_heap
        ]

        UTILITIES.add_record_to_csv_File(row_data)
        print(f"  -> Finished size {size}. Data saved to CSV.\n")