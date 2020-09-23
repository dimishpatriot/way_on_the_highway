"""Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, the cube above will have 
volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be 
an integer m and you have to return the integer n such as 
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

=== Examples: ===
findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""

import pytest


@pytest.mark.parametrize("m, n", [
    (1, 1),
    (9, 2),
    (36, 3),
    (100, 4),
    (225, 5),
    (441, 6),
    (784, 7),
    (1296, 8),
    (2025, 9),
    (3025, 10),
    (4356, 11),
    (6084, 12),
    (8281, 13),
    (11025, 14),
    (14400, 15),
    (18496, 16),
    (23409, 17),
    (29241, 18),
    (36100, 19),
    (44100, 20),
    (53361, 21),
    (64009, 22),
    (76176, 23),
    (90000, 24),
    (105625, 25),
    (1071225, 45),
    (4183059834009, 2022),
    (135440716410000, 4824),
    (40539911473216, 3568),
    (26825883955641, 3218),
])
def test_nb_positive(m, n):
    assert find_nb(m) == n


@pytest.mark.parametrize("m", [
    (91716553919377),
    (24723578342962),
    (64341),
    (53144),
    (450010),
    (2),
    (4),
    (16),
    (76158)
])
def test_nb_negative(m):
    assert find_nb(m) == -1


def find_nb(m):
    if m == 1:
        return 1
    if m < 9:
        return -1
    n = 1
    for i in range(2, int(m**1/3)):
        n += i**3
        print(f"({n}, {i}),")
        if n < m:
            continue
        elif n == m:
            return i
        else:
            return -1

if __name__ == "__main__":
    find_nb(100000)
