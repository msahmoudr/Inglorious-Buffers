import csv
import random
import time
file_path = "Time Comparison2.csv"

class UTILITIES:
    @staticmethod
    def generate_random_array(size):
        my_array = []
        for i in range(size):
            my_array.append(random.randint(0, 100000000))
        return my_array

    @staticmethod
    def add_record_to_csv_File(line):
            with open(file_path, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(line)

    @staticmethod
    def is_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    @staticmethod
    def binary_search_insertion(arr, key, start, end):
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid
        return start