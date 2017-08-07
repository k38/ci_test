import pytest
from calculator import Calculator

#def pytest_funcarg__calc():
@pytest.fixture()
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, r", [(9, 8, 17), (1, 1, 2), (1, 2, 3)])
def test_add(calc, a, b, r):
    assert calc.add(a, b) == r

@pytest.mark.parametrize("a, b, r", [(9, 8, 1), (1, 1, 0)])
def test_sub(calc, a, b, r):
    assert calc.sub(a, b) == r

