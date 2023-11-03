from common import compare_arrays, array_reversal_in_place

if __name__ == "__main__":
    assert compare_arrays(array_reversal_in_place([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
    assert compare_arrays(array_reversal_in_place([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    assert compare_arrays(array_reversal_in_place([1]), [1])
    assert compare_arrays(array_reversal_in_place([1, 2]), [1, 2])
    assert compare_arrays(array_reversal_in_place([]), [])
