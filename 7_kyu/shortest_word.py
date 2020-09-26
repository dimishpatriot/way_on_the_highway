"""Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""

import pytest


@pytest.mark.parametrize("test, result", [
    ("bitcoin take over the world maybe who knows perhaps", 3),
    ("turns out random test cases are easier than writing out basic ones", 3),
    ("lets talk about javascript the best language", 3),
    ("i want to travel the world writing code one day", 1),
    ("Lets all go on holiday somewhere very cold", 2),
    ("ok", 2),
])
def test_short(test, result):
    assert find_short(test) == result


def find_short(s: str) -> int:
    all_words = s.split()
    ln = len(all_words[0])
    for word in all_words[1:]:
        ln = min(ln, len(word))
    return ln
