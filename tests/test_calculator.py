import pytest
from app.calculator import calculate_total, calculate_discounted_total

def test_calculate_total_valid():
    assert calculate_total(10.5, 3) == 31.5
    assert calculate_total("20", "2") == 40.0

def test_calculate_total_invalid():
    assert calculate_total("abc", 3) is None
    assert calculate_total(-5, 2) is None

def test_calculate_discounted_total_valid():
    # $10 * 2 items = $20. 10% off of $20 = $18
    assert calculate_discounted_total(10, 2, 10) == 18.0
    # 0% discount
    assert calculate_discounted_total(50, 1, 0) == 50.0

def test_calculate_discounted_invalid():
    assert calculate_discounted_total(10, 2, -5) is None
    assert calculate_discounted_total(10, 2, 105) is None
