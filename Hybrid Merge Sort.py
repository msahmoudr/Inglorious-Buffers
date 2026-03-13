from typing import List

from Merge_Sort import MERGE_SORT


class hybrid_merge_sort:

    @staticmethod
    def _selection_sort(arr: List[int], left: int, right: int) -> None:
        for i in range(left, right + 1):
            min_idx = i
            for j in range(i + 1, right + 1):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]



    @staticmethod
    def hybrid_merge_sort(arr: List[int], left: int, right: int, threshold: int) -> List[int]:
        if left < right:
            size = right - left + 1

            if size <= threshold:
                MERGE_SORT._selection_sort(arr, left, right)
                return arr

            mid = (left + right) // 2

            MERGE_SORT.hybrid_merge_sort(arr, left, mid, threshold)
            MERGE_SORT.hybrid_merge_sort(arr, mid + 1, right, threshold)

            MERGE_SORT._merge(arr, left, mid, right)

        return arr