import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    input=100
    assert input>100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    input=100
    assert input>=100

@pytest.mark.skip
@pytest.mark.others
def test_equal():
    input=100
    assert input==101


