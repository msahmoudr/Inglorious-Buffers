import time
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




