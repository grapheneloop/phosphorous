import math


def is_prime(num):
    return False if num in [0, 1] else is_prime_for_more_than_two(num)


def is_prime_for_more_than_two(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(4) is False
    assert is_prime(172) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
