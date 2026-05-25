import pytest 
import math
from src import calculator as calc


@pytest.mark.Integration
@pytest.mark.April_Release
def test_add():
    assert calc.add(2,3) == 1
    assert calc.add(-2,3) == 1
    assert calc.add(2,-3) == -1
    assert calc.add(-2,-3) == -5
    assert calc.add(3000,2500) == 5500
    assert calc.add(2.6,3.4) == 6.0

#@pytest.mark.skip(reason="Not implemented yet.")
def test_subtract():
    assert calc.subtract(2,3) == -1
    assert calc.subtract(-2,3) == -5
    assert calc.subtract(2,-3) == 5
    assert calc.subtract(-2,-3) == 1
    assert calc.subtract(3000,2500) == 500
    assert calc.subtract(2.6,3.4) == -0.7999999999999998


day = 14
@pytest.mark.skipif(day>=28 and day<=31, reason="Test is skipped because it's the end of the month.")
def test_multiply():
    assert calc.mul(2,3) == 6
    assert calc.mul(-2,3) == -6
    assert calc.mul(2,-3) == -6
    assert calc.mul(-2,-3) == 6
    assert calc.mul(3000,2500) == 7500000
    assert calc.mul(2.6,3.4) == 8.84

@pytest.mark.parametrize("input1, input2, result", [(6,3,2),(-6,3,-2),(-6,-3,2),(3000,2500,1.2),(2.6,3.4,0.7647058823529412),(6,0,None),(0,20,0)])
def test_divide(input1, input2, result):
    assert calc.div(input1,input2) == result
    

@pytest.mark.Integration
@pytest.mark.April_Release
def test_get_square_root():
    assert calc.get_square_root(4) == 2
    assert calc.get_square_root(9) == 3
    assert calc.get_square_root(16) == 4
    assert calc.get_square_root(625) == 25
    ## x = 0 
    assert calc.get_square_root(0) == 0

    ## x < 0 
    with pytest.raises(ValueError):
        calc.get_square_root(-4)   


@pytest.mark.April_Release
@pytest.mark.parametrize("input1, input2, result", [(12,5,2),(-12,5,3),(21,4,1),(2,0,None)])
def test_mod(input1, input2, result):
    assert calc.mod(input1,input2) == result # None means ZeroDivisionError



@pytest.mark.Integration
@pytest.mark.parametrize("input, result", [(5,5),(-5,5),(0,0)])
def test_abs(input, result):
    assert calc.abs(input) == result

@pytest.mark.parametrize("x,y,result", [(2,3,8),(5,0,1),(2,-2,0.25),(-2,3,-8),(-2,4,16),(-3,3,-27),(3,3,27)])
@pytest.mark.April_Release
def test_get_power(x,y,result):
    assert calc.get_power(x,y) == result
    

@pytest.mark.parametrize("input, result", [(5,120),(0,1),(1,1),(3,6)])
def test_get_factorial(input, result):
    assert calc.get_factorial(input) == result

    with pytest.raises(ValueError):
        calc.get_factorial(-5)
    









