import pytest
from mathseries.series import lucas, sum_series, fibonacci


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_one():
    actual = fibonacci(2)
    expected = 2
    assert actual == expected

def test_two():
    actual=fibonacci(3)
    expected=3
    assert actual == expected

def test_three():
    actual=fibonacci(4)
    expected=5
    assert actual == expected

def test_four():
    actual=fibonacci(5)
    expected=8
    assert actual == expected
  
# Lucas *********************************************

def test_one_lucas():
    actual = lucas(1)
    expected = 3
    assert actual == expected  


def test_two_lucas():
    actual = lucas(2)
    expected = 4
    assert actual == expected


def test_two_lucas():
    actual = lucas(2)
    expected = 4
    assert actual == expected

# sum series ****************************************

def test_one_sum():
    actual = sum_series(4, 5, 1)
    expected = 20
    assert actual == expected

def test_two_sum():
    actual = sum_series(20, 1, 1)
    expected = 17711
    assert actual == expected