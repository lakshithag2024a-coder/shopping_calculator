import pytest
from app.calculator import calculate_total

def test_calculate_total_valid():
    assert calculate_total(10.5, 3) == 31.5
    assert calculate_total("20", "2") == 40.0

def test_calculate_total_invalid():
    assert calculate_total("abc", 3) is None
    assert calculate_total(-5, 2) is None
