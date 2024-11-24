import pytest

# Test for calculator functionality
def test_calculator():
    num1 = 5
    num2 = 10
    
    addition_result = num1 + num2
    assert addition_result == 15, "Addition calculation is incorrect"

    subtraction_result = num1 - num2
    assert subtraction_result == -5, "Subtraction calculation is incorrect"

    multiplication_result = num1 * num2
    assert multiplication_result == 50, "Multiplication calculation is incorrect"

    division_result = num1 / num2
    assert division_result == 0.5, "Division calculation is incorrect"

# Test for multiplication table generation
def test_multiplication_table():
    num = 3
    rows = 5
    expected_results = [num * i for i in range(1, rows + 1)]
    for i, result in enumerate(expected_results):
        assert result == num * (i + 1), f"Row {i + 1} in multiplication table is incorrect"
