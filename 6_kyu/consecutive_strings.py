"""You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive
strings taken in the array.

=== Example: ===
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas",
"theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

=== Note ===
consecutive strings : follow one after another without an interruption
"""

import pytest


@pytest.mark.parametrize("strarr, k, result", [
    (["zone", "abigail", "theta", "form", "libe", "zas"], 2, "abigailtheta"),
    (["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1,
     "oocccffuucccjjjkkkjyyyeehh"),
    (["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2,
     "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"),
    (["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3, "ixoyx3452zzzzzzzzzzzz"),
    ([], 1, ""),
    (["a", "b"], 3, ""),
    (["a", "b"], -3, ""),
])
def test_longest_consec(strarr, k, result):
    print(strarr, k, result)
    assert longest_consec(strarr, k) == result


def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    max_len = 0
    max_i = 0
    for i, first_str in enumerate(strarr[:n - k + 1]):
        print(i, first_str)
        s = ""
        for j in range(k):
            s += strarr[i + j]
        if len(s) > max_len:
            max_len = len(s)
            max_i = i
    return "".join(strarr[max_i: max_i + k])
