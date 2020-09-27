"""Create a function that transforms any positive number to a string
representing the number in words. The function should work for
all numbers between 0 and 999_999.

=== Examples ===
number2words(0)  ==>  "zero"
number2words(10)  ==>  "ten"
number2words(17)  ==>  "seventeen"
number2words(80)  ==>  "eighty"
number2words(99)  ==>  "ninety-nine"
number2words(100)  ==>  "one hundred"
number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"
"""


import pytest
from enum import Enum


@pytest.mark.parametrize("number, s", [
    (0, "zero"),
    (1, "one"),
    (9, "nine"),
    (10, "ten"),
    (17, "seventeen"),
    (20, "twenty"),
    (21, "twenty-one"),
    (45, "forty-five"),
    (80, "eighty"),
    (99, "ninety-nine"),
    (100, "one hundred"),
    (301, "three hundred one"),
    (799, "seven hundred ninety-nine"),
    (800, "eight hundred"),
    (950, "nine hundred fifty"),
    (1000, "one thousand"),
    (1002, "one thousand two"),
    (3051, "three thousand fifty-one"),
    (7200, "seven thousand two hundred"),
    (7219, "seven thousand two hundred nineteen"),
    (8330, "eight thousand three hundred thirty"),
    (18568, "eighteen thousand five hundred sixty-eight"),
    (99999, "ninety-nine thousand nine hundred ninety-nine"),
    (218900, "two hundred eighteen thousand nine hundred"),
    (418054, "four hundred eighteen thousand fifty-four"),
    (800004, "eight hundred thousand four"),
    (888888, "eight hundred eighty-eight thousand eight hundred eighty-eight"),
])
def test_number_translator(number, s):
    assert number2words(number) == s


class Number(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fifteen = 15
    eighteen = 18
    twenty = 20
    thirty = 30
    forty = 40
    fifty = 50
    sixty = 60
    seventy = 70
    eighty = 80
    ninety = 90


def number2words(number):
    if number is 0:
        return "zero"
    else:
        s = ""
        stat = dict()
        start = number
        for n in reversed(range(0, 6)):
            stat[10**n] = number // (10**n)
            number %= 10**n

        for digit in [1000, 1]:
            if Number(stat[100 * digit]).value > 0:
                s += Number(stat[100 * digit]).name + " hundred "
            if Number(stat[10 * digit]).value == 1:
                if Number(stat[1 * digit]).value in [0, 1, 2, 3, 5, 8]:
                    # 11 - 13
                    s += f"{Number(stat[10*digit] * 10 + stat[1*digit]).name}"
                else:
                    s += f"{Number(stat[1*digit]).name}teen"  # 14 - 17, 19
            else:
                if Number(stat[10 * digit]).value > 1:
                    s += f"{Number(stat[10*digit] * 10).name}"
                if Number(stat[1 * digit]).value > 0:
                    if Number(stat[10 * digit]).value > 1:
                        s += "-"
                    s += Number(stat[1 * digit]).name
            if start >= 1000 and digit == 1000:
                s = s.rstrip()
                s += " thousand "
        s = s.lstrip().rstrip()
    return s
