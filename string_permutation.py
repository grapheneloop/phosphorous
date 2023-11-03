from common import swap_characters_at_index_safely
from n_factorial_the_bad_way import fact


def permutation(value, index=0):
    output = set([])
    if index == len(value):
        return {value}
    else:
        for i in range(index, len(value)):
            output.update(permutation(swap_characters_at_index_safely(value, index, i), index + 1))
    return output


def test(value):
    output = permutation(value)
    print(output)
    assert len(output) == fact(len(value))


if __name__ == "__main__":
    test("abcd")
    test("abc")
    test("a")
    test("ab")
