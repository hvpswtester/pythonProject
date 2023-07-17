import pytest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


# Test cases for addition
def test_addition():
    assert add(2, 3) == 5
    assert add(-5, 10) == 5
    assert add(0, 0) == 0


# Test cases for subtraction
def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(10, -5) == 15
    assert subtract(0, 0) == 0


# Test cases for multiplication
def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-5, 10) == -50
    assert multiply(0, 5) == 0
