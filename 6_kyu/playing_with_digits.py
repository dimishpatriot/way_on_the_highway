"""Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1

    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and
a positive integer p
We want to find a positive integer k, if it exists, such as the sum of the
digits of n taken to the successive powers of p is equal to k * n.

In other words:
    Is there an integer k such as :
    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.
=== Note: ===
n and p will always be given as strictly positive integers.
"""

import pytest


class TestPower:
    @pytest.mark.parametrize("test, result", [
        ((89, 1), 1),
        ((695, 2), 2),
        ((46288, 3), 51)
    ])
    def test_positive(self, test, result):
        assert dig_pow(*test) == result

    @pytest.mark.parametrize("test", [
        (92, 1)
    ])
    def test_negative(self, test):
        assert dig_pow(*test) == -1


def dig_pow(n: int, p: int) -> int:
    digits = (int(s) for s in str(n))
    pow_sum = 0
    for idx, d in enumerate(digits):
        pow_sum += d**(p + idx)
    k = pow_sum / n
    if int(k) == k:
        return int(k)
    else:
        return -1
