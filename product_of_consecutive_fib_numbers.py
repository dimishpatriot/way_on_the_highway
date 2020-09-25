"""The Fibonacci numbers are the numbers in the following integer sequence (Fn):
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as
    F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n)
and F(n+1) verifying
    F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou
will return
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)

F(m) being the smallest one such as F(m) * F(m+1) > prod.
Some Examples of Return:

productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
"""

import pytest


@pytest.mark.parametrize("number, result", [
    (0, [0, 1, True]),
    (1, [1, 1, True]),
    (2, [1, 2, True]),
    (6, [2, 3, True]),
    (15, [3, 5, True]),
    (40, [5, 8, True]),
    (104, [8, 13, True]),
    (714, [21, 34, True]),
])
def test_production_fib_pozitive(number, result):
    assert productFib(number) == result


@pytest.mark.parametrize("number, result", [
    (3, [2, 3, False]),
    (5, [2, 3, False]),
    (14, [3, 5, False]),
    (39, [5, 8, False]),
    (103, [8, 13, False]),
    (713, [21, 34, False]),
    (800, [34, 55, False]),
])
def test_production_fib_negative(number, result):
    assert productFib(number) == result


def fib_gen(max):
    s1 = 0
    s2 = 1
    yield s1
    yield s2
    current = 1
    while current < max:
        yield current
        s1 = s2
        s2 = current
        current = s1 + s2


def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    else:
        f = fib_gen(prod + 2)  # +2 for 1 and 2
        try:
            first = next(f)
            second = next(f)
            while True:
                first = second
                second = next(f)
                if first * second == prod:
                    return [first, second, True]
                elif first * second > prod:
                    return [first, second, False]
        except StopIteration:
            pass


"""The best practice for Python is:

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

  FUN :)
  """
