"""Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw
according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll.
For example, a given "5" can only count as part of a triplet (contributing
to the 500 points) or as a single 50 points, but not both in the same roll.

=== Example scoring ===

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

In some languages, it is possible to mutate the input to the function.
This is something that you should never do. If you mutate the input,
you will not be able to pass all the tests.
"""

import pytest


@pytest.mark.parametrize("dice, result", [
    ([2, 3, 4, 6, 2], 0),

    ([2, 2, 2, 4, 4], 200),
    ([3, 3, 3, 4, 4], 300),
    ([4, 4, 4, 3, 3], 400),
    ([5, 5, 5, 2, 2], 500),
    ([6, 6, 6, 2, 2], 600),
    ([1, 1, 1, 3, 3], 1000),

    ([2, 4, 4, 5, 4], 450),
    ([2, 4, 4, 5, 4], 450),
    ([5, 5, 5, 1, 1], 700),
    ([5, 5, 5, 5, 5], 600),

    ([1, 1, 1, 3, 1], 1100),
    ([1, 1, 1, 5, 5], 1100),
    ([1, 1, 1, 1, 1], 1200),
])
def test_score(dice, result):
    assert score(dice) == result


def score(dice):
    stat = {i: dice.count(i) for i in set(dice)}
    res = 0
    for k, v in stat.items():
        if v >= 3:
            if k == 1:
                res += 1000 + (v - 3) * 100
            elif k == 5:
                res += 500 + (v - 3) * 50
            else:
                res += k * 100
        elif v < 3:
            if k == 1:
                res += v * 100
            elif k == 5:
                res += v * 50

    return res
