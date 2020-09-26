"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""

import pytest


@pytest.mark.parametrize("test, result", [
    ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
    ([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
     [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    (["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
     ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    (["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9], [
     "a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([0, 1, None, 2, False, 1, 0], [1, None, 2, False, 1, 0, 0]),
    (["a", "b"], ["a", "b"]),
    (["a"], ["a"]),
    ([0, 0], [0, 0]),
    ([0], [0]),
    ([False], [False]),
    ([], [])
])
def test_move_zeros(test, result):
    assert move_zeros(test) == result


def move_zeros(array):
    zeros = []
    idx = 0
    while idx < len(array):
        if array[idx] == 0 and not isinstance(array[idx], bool):
            array.pop(idx)
            zeros.append(0)
            idx -= 1
        idx += 1
    array.extend(zeros)
    return array
