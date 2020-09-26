"""ROT13 is a simple letter substitution cipher that replaces a letter
with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered
with Rot13. If there are numbers or special characters included
in the string, they should be returned as they are. Only letters from
the latin/english alphabet should be shifted, like in the original
Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import pytest


@pytest.mark.parametrize("message, result", [
    ("", ""),
    ("1", "1"),
    ("ABBA", "NOON"),
    ("test", "grfg"),
    ("Test", "Grfg"),
    ("hello", "uryyb"),
    ("Word", "Jbeq"),
    ("in my 1981", "va zl 1981"),
    ("probably", "cebonoyl"),
    ("foo_foo", "sbb_sbb"),
    ("123barbar___", "123oneone___"),
    ("1234567890-a", "1234567890-n"),
])
def test_rot13(message, result):
    assert rot13(message) == result


def rot13(message):
    alphabet = [chr(char) for char in range(ord('A'), ord('Z') + 1)]
    s = ""
    if len(message) > 0:
        for char in message:
            if char.isalpha():
                idx = alphabet.index(char.upper()) + 13
                if idx >= len(alphabet):
                    idx -= len(alphabet)
                if char.upper() == char:
                    s += alphabet[idx]
                else:
                    s += alphabet[idx].lower()
            else:
                s += char
    return s


if __name__ == "__main__":
    """ prepare test data """

    alphabet = [chr(char) for char in range(ord('A'), ord('Z') + 1)]
    print(alphabet)

    data = [
        "",
        "1",
        "ABBA",
        "test",
        "Test",
        "hello",
        "Word",
        "in my 1981",
        "probably",
        "foo_foo",
        "123barbar___",
        "1234567890-a",
    ]
    code = []
    for message in data:
        s = rot13(message)
        code.append(s)

    for d, c in dict(zip(data, code)).items():
        print(f'("{d}", "{c}"),')  # just copy from terminal
