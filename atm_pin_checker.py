"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true,
else return false.
"""

import pytest


@pytest.mark.parametrize("test, result", [
    ("1234", True),
    ("0000", True),
    ("9999", True),
    ("000000", True),
    ("999999", True),
    ("1", False),
    ("12", False),
    ("123", False),
    ("123,", False),
    ("12345", False),
    (".234", False),
    ("123-", False),
    ("12a4", False),
    ("00000", False),
    ("0000000", False),
    ("99999", False),
    ("9999999", False),
    ("AAAA", False),
    (str(), False),
    ("' '", False),
    ("'    '", False)
])
def test_pin_checker(test, result):
    pass


def validate_pin(pin: str) -> bool:
    if len(pin) in (4, 6):
        if pin.isdigit():
            return True
    return False
