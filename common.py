def array_swap_elements_in_place(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def array_reversal_in_place(arr):
    n = len(arr)
    if n > 0:
        for index in range(0, int(n / 2)):
            array_swap_elements_in_place(arr, index, n - index - 1)
    return arr


def compare_arrays(left, right):
    if is_empty_or_null(left) or is_empty_or_null(right):
        if not is_empty_or_null(left) or not is_empty_or_null(right):
            return False
        else:
            return True
    if len(left) is not len(right):
        return False
    else:
        return [a == b for a, b in zip(left, right)]


def is_empty_or_null(arr):
    return arr is None or len(arr) == 0