"""Define a function that takes in two non-negative integers aaa
and bbb and returns the last decimal digit of aba^bab.
Note that aaa and bbb may be very large!

For example, the last decimal digit of 9^7 is 9,
since 9^7=47829699.
The last decimal digit of (2^200)^(2^300), which has over
10^92 decimal digits, is 6.
Also, please take 0^0 to be 1.

You may assume that the input will always be valid.

=== Examples ===

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""

import pytest


@pytest.mark.parametrize("test, result", [
    ((0, 0), 1),
    ((1000000, 0), 1),
    ((4, 1), 4),
    ((4, 2), 6),
    ((9, 7), 9),
    ((5, 1), 5),
    ((5, 6), 5),
    ((5, 3), 5),
    ((1000, 1000), 0),
    ((1000, 1001), 0),
    ((1000, 1002), 0),
    ((5, 3), 5),
    ((10, 10**10), 0),
    ((2**200, 2**300), 6),
    ((3715290469715693021198967285016729344580685479654510946723,
      68819615221552997273737174557165657483427362207517952651), 7),
])
def test_big_numbers(test, result):
    assert last_digit(*test) == result


def last_digit(n, p):
    if p == 0:
        return 1
    elif n % 10 == 0:
        return 0
    elif p < 10:
        return ((n % 10) ** p) % 10
    else:
        return ((n % 10) ** (p % 100)) % 10


"""Shortest, but not efficient solution:
def last_digit(n1, n2):
    return pow(n1, n2, 10)
"""
