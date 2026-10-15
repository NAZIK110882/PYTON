"""Ті самі тести math_utils.py, переписані на pytest (для порівняння)."""
import pytest

from math_utils import add, divide, is_even, factorial


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_add_zero():
    assert add(0, 7) == 7


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


@pytest.mark.parametrize("n, expected", [(4, True), (7, False), (0, True), (-2, True), (-3, False)])
def test_is_even(n, expected):
    assert is_even(n) is expected


@pytest.mark.parametrize("bad", ["4", 2.5, None])
def test_is_even_wrong_type(bad):
    with pytest.raises(TypeError):
        is_even(bad)


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        factorial(3.5)
