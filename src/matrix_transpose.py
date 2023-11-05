def rotate_matrix(a):
    n = len(a)
    for i in range(0, int(n / 2) + 1):
        rotate(a, i)
    return a


def rotate(a, i):
    n = len(a) - 1
    for x in range(i, n - i):
        temp = a[i][n - x]
        a[i][n - x] = a[x][i]
        a[x][i] = a[n - i][x]
        a[n - i][x] = a[n - x][n - i]
        a[n - x][n - i] = temp


if __name__ == "__main__":
    assert (rotate_matrix(
        [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '16']]) ==
            [['13', '9', '5', '1'], ['14', '10', '6', '2'], ['15', '11', '7', '3'], ['16', '12', '8', '4']])
