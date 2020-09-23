"""Define a function that takes one integer argument and returns logical value
true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater
than 1 that has no positive divisors other than 1 and itself.
"""

import pytest


@pytest.mark.parametrize("test, result", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (19, True),
    (31, True),
    (73, True),
    (5099, True),
    (0, False),
    (1, False),
    (-1, False),
    (4, False),
    (44, False),
    (2**256, False)
])
def test_prime(test, result):
    assert is_prime(test) == result


def is_prime(num: int) -> bool:
    if type(num) is not int or num <= 1:
        return False
    else:
        if num == 2:  # first and the one of even prime's
            return True
        if num % 2 == 0:  # even's
            return False
        else:
            divizor = 3
            while divizor <= num // divizor:
                if num % divizor == 0:
                    return False
                divizor += 2
            return True
