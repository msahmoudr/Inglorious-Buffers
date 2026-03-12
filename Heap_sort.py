from typing import List


class HeapSort:
    def __init__(self):
        self.heap_size = 0
        self.array_length = 0

    def _parent(self, i: int) :
        return (i - 1) // 2

    def _left(self, i: int) :
        return 2 * i + 1

    def _right(self, i: int) :
        return 2 * i + 2

    def max_heapify(self, arr: List[int], i: int) :
        largest = i
        left = self._left(i)
        right = self._right(i)

        if left < self.heap_size and arr[left] > arr[largest]:
            largest = left

        if right < self.heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest)

    def build_max_heap(self, arr: List[int]) :
        self.array_length = len(arr)
        self.heap_size = len(arr)

        for i in range(self.array_length // 2 - 1, -1, -1):
            self.max_heapify(arr, i)

    def heapsort(self, arr: List[int]) -> List[int]:
        self.array_length = len(arr)
        self.heap_size = len(arr)

        self.build_max_heap(arr)

        for i in range(self.array_length - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heap_size -= 1
            self.max_heapify(arr, 0)

        return arr


class HybridMergeSelectionSort:
    def __init__(self, threshold: int = 10):
        self.threshold = threshold

    def selection_sort(self, arr: List[int], left: int, right: int) :
        for i in range(left, right):
            min_idx = i
            for j in range(i + 1, right + 1):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def merge(self, arr: List[int], left: int, mid: int, right: int) :
        n1 = mid - left + 1
        n2 = right - mid

        left_arr = arr[left:left + n1]
        right_arr = arr[mid + 1:mid + 1 + n2]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def hybrid_merge_selection_sort(self, arr: List[int], left: int = None, right: int = None) :
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1

        if right - left + 1 <= self.threshold:
            self.selection_sort(arr, left, right)
            return arr

        if left < right:
            mid = left + (right - left) // 2

            self.hybrid_merge_selection_sort(arr, left, mid)
            self.hybrid_merge_selection_sort(arr, mid + 1, right)

            self.merge(arr, left, mid, right)

        return arr


