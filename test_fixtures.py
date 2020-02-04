import pytest

@pytest.fixture
def input_value():
    input=100
    return input

def test_div(input_value):
    assert input_value%10==0

def test_div1(input_value):
    assert input_value%20==1


