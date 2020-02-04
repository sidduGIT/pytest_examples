import math
import pytest

@pytest.mark.square
def test_square():
    num=8
    assert num**2==64

@pytest.mark.square
def test_sqrt():
    num=36
    assert math.sqrt(num)==6

@pytest.mark.others
def test_equal():
    num=100
    assert num>=100
