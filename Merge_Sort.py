from typing import List


class MERGE_SORT:
    @staticmethod
    def _merge(arr: List[int], left: int, mid: int, right: int) -> None:
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    @staticmethod
    def _selection_sort(arr: List[int], left: int, right: int) -> None:
        for i in range(left, right + 1):
            min_idx = i
            for j in range(i + 1, right + 1):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    @staticmethod
    def merge_sort(arr: List[int], left: int, right: int) -> List[int]:


        if left < right:
            mid = (left + right) // 2

            MERGE_SORT.merge_sort(arr, left, mid)
            MERGE_SORT.merge_sort(arr, mid + 1, right)

            MERGE_SORT._merge(arr, left, mid, right)

        return arr

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