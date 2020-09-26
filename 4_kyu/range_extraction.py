"""A format for expressing an ordered list of integers is to use a comma
separated list of either individual integers or a range of integers denoted
by the starting integer separated from the end integer in the range
by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers.
For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.

=== Example: ===

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9,
         10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

import pytest


@pytest.mark.parametrize("test, result", [
    ([4, 2, 0], '0,2,4'),
    ([4, 2, 0, 5], '0,2,4,5'),
    ([1, 2, 3, 0, 5], '0-3,5'),
    ([1, 2, 3, 4, 5], '1-5'),
    ([-1, 0, 1], '-1-1'),
    ([-5, -3, -2, -1, 1], '-5,-3--1,1'),
    ([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
     '-6,-3-1,3-5,7-11,14,15,17-20'),
    ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
        '-3--1,2,10,15,16,18-20')
])
def test_range_extraction(test, result):
    assert solution(test) == result


def solution(args: list) -> str:
    res = []
    sorted_args = sorted(args)

    idx = 0
    while idx < len(sorted_args):
        start = sorted_args[idx]
        lenght = 2
        while idx + lenght < len(sorted_args) and\
                sorted_args[idx + lenght] - start == lenght:
            lenght += 1
        if lenght > 2:
            res.append(f"{start}-{sorted_args[idx + lenght - 1]}")
            idx += lenght
            continue
        res.append(str(sorted_args[idx]))
        idx += 1

    return ",".join(res)
