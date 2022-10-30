import pytest
from fizz_buzz import fizz_buzz

def test_for_divisible_by_3():
    """Is number divisible by 3 and not 5."""
    assert fizz_buzz(6) == 'Fizz'
    assert fizz_buzz(12) == 'Fizz'
    assert fizz_buzz(33) == 'Fizz'

def test_for_divisible_by_5():
    """Is number divisible by 5 and not 3."""
    assert fizz_buzz(10) == 'Buzz'
    assert fizz_buzz(25) == 'Buzz'
    assert fizz_buzz(40) == 'Buzz'

def test_for_divisible_by_3_and_5():
    """Is number divisible by 3 AND 5."""
    assert fizz_buzz(30) == 'FizzBuzz'
    assert fizz_buzz(45) == 'FizzBuzz'
    assert fizz_buzz(120) == 'FizzBuzz'

def test_for_not_divisible_by_either():
    """Is number NOT divisible by 3 or 5."""
    assert fizz_buzz(8) == 8
    assert fizz_buzz(34) == 34
    assert fizz_buzz(47) == 47
