import pytest
from math_utils import add, subtract, multiply, divide

# тесты для add
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (1.5, 2.5, 4.0)
])
def test_add_success(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("2", 3),
    (2, [1, 2]),
    (True, 5)
])
def test_add_type_error(a, b):
    with pytest.raises(TypeError):
        add(a, b)


# тесты для subtract
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 5, -5),
    (2.5, 1.5, 1.0)
])
def test_subtract_success(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("5", 3)


# тесты для multiply
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0.5, 2, 1.0)
])
def test_multiply_success(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("2", 3)


# тесты для divide 
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (5, 2, 2.5),
    (-6, 2, -3.0)
])
def test_divide_success(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (5, 0),
    (5, 0.0)
])
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("6", 3)