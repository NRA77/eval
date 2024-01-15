from devine_turing import *
import pytest

def test_decomposer():
    assert decomposer(123) == (1, 2, 3)
    assert decomposer(456) == (4, 5, 6)
    assert decomposer(789) == (7, 8, 9)
    assert decomposer(99) is None
    assert decomposer(1000) is None

def test_divisible():
    assert divisible(27)
    assert not divisible(15)

def test_somme():
    assert somme(7, 1, 6)
    assert not somme(1, 2, 3)
    assert somme(10, 0, 5) is None
    assert somme(2, 3, 10) is None
    assert somme(2, -1, 5) is None