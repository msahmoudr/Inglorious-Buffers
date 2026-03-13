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