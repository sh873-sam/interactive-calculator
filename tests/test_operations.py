import pytest

from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    DivisionByZeroError,
)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (0, 1, -1),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 2, 6),
        (-2, 4, -8),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 2, 3.0),
        (5, 2, 2.5),
        (-8, 4, -2.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)
