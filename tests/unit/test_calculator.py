import pytest
from src.calculator import add, divide, subtract, multiply, power, square_root


class TestBasicOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_subtract_negative_numbers(self):
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2


class TestMultiplyDivideWithValidation:
    def test_multiply_input_validation(self):
        with pytest.raises(TypeError):
            multiply("5", 3)
        with pytest.raises(TypeError):
            multiply(5, "3")

    def test_divide_input_validation(self):
        with pytest.raises(TypeError):
            divide("10", 2)


class TestMultiplyDivide:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4


class TestAdvancedOperations:
    def test_power_positive_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25

    def test_square_root_positive_numbers(self):
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative"):
            square_root(-4)


class TestValidationAndErrors:
    def test_add_input_validation(self):
        with pytest.raises(TypeError, match="can only concatenate str"):
            add("2", 3)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="division by zero is undefined"):
            divide(10, 0)
