""" Your task is to make a function that can take any non-negative integer
as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""

import pytest


@pytest.mark.parametrize("num, result", [
    (123, 321),
    (42145, 54421),
    (145263, 654321),
    (123456789, 987654321),
    (0, 0),
    (15, 51),
    (9190, 9910)
])
def test_solution(num, result):
    assert descending_order(num) == result


def descending_order(num: int) -> int:
    num_array = list(str(num))
    num_array.sort(reverse=True)
    return int(''.join(num_array))
