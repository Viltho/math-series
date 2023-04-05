import pytest
from mathseries.app import fibonacci
from mathseries.series import lucas


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