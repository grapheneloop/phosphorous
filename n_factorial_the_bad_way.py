def fact(n):
    return 1 if n == 0 else fact(n - 1) * n


if __name__ == "__main__":
    assert fact(5) == 120
    assert fact(1) == 1
    assert fact(0) == 1
    assert fact(6) == 720
