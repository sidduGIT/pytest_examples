import pytest

@pytest.mark.great
def test_greater():
    num=100
    assert num>100

@pytest.mark.great
def test_greater_equal():
    num=100
    assert num>=100

@pytest.mark.others
def test_equality():
    num=100
    assert num==100
