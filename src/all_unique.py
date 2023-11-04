def is_all_unique(str):
    index = [0] * 100
    for c in list(str):
        index[ord(c) - ord('a')] += 1
        if index[ord(c) - ord('a')] > 1:  # TODO: ord returns the int value of a character
            return False
    return True


if __name__ == "__main__":
    assert is_all_unique('abcd')
    assert is_all_unique('bab') is False
    assert is_all_unique('malayalam') is False
    assert is_all_unique('o') is True
    assert is_all_unique('oo') is False
