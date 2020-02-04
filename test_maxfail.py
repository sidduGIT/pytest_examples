import math
import pytest

def test_square_pass():
    num=100
    assert math.sqrt(num)==10

def test_square_fail1():
    num=100
    assert math.sqrt(num)==11

def test_square_fail2():
    num=100
    assert math.sqrt(num)==12

def test_square_fail3():
    num=100
    assert math.sqrt(num)==13

def test_square_fail4():
    num=100
    assert math.sqrt(num)==14



