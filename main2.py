import random
from Kt_Element import kth_smallest


def run_kth_element_tests():
    print("--- Testing K-th Smallest Element (Quickselect) ---")

    arr = [random.randint(1, 100) for _ in range(15)]
    n = len(arr)

    sorted_arr = sorted(arr)

    print(f"Original Array: {arr}")
    print(f"Sorted Array:   {sorted_arr}\n")


    test_values_for_k = [
        1,
        3,
        n // 2,
        n - 2,
        n
    ]

    all_passed = True

    for k in test_values_for_k:
        expected_value = sorted_arr[k - 1]

        actual_value = kth_smallest(arr, k)

        if expected_value == actual_value:
            status = "✅ PASS"
        else:
            status = "❌ FAIL"
            all_passed = False

        print(f"Looking for k = {k:2d} | Expected: {expected_value:3d} | Actual: {actual_value:3d} | {status}")

    print("\n---------------------------------------------------")
    if all_passed:
        print("🎉 SUCCESS: All Quickselect tests passed perfectly!")
    else:
        print("⚠️ WARNING: Some tests failed. Check your logic.")


if __name__ == "__main__":
    run_kth_element_tests()