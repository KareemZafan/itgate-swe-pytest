import pytest 
import math
from src import calculator as calc


@pytest.mark.Integration
@pytest.mark.April_Release
def test_add():
    assert calc.add(2,3) == 5
    assert calc.add(-2,3) == 1
    assert calc.add(2,-3) == -1
    assert calc.add(-2,-3) == -5
    assert calc.add(3000,2500) == 5500
    assert calc.add(2.6,3.4) == 6.0

@pytest.mark.skip(reason="Not implemented yet.")
def test_subtract():
    assert calc.subtract(2,3) == -1
    assert calc.subtract(-2,3) == -5
    assert calc.subtract(2,-3) == 5
    assert calc.subtract(-2,-3) == 1
    assert calc.subtract(3000,2500) == 500
    assert calc.subtract(2.6,3.4) == -0.7999999999999998

def test_multiply():
    assert calc.mul(2,3) == 6
    assert calc.mul(-2,3) == -6
    assert calc.mul(2,-3) == -6
    assert calc.mul(-2,-3) == 6
    assert calc.mul(3000,2500) == 7500000
    assert calc.mul(2.6,3.4) == 8.84

def test_divide():
    assert calc.div(6,3) == 2
    assert calc.div(-6,3) == -2
    assert calc.div(6,-3) == -2
    assert calc.div(-6,-3) == 2
    assert calc.div(3000,2500) == 1.2
    assert calc.div(2.6,3.4) == 0.7647058823529412
    

    ## y = 0 
    # with pytest.raises(ValueError):
        #calc.div(6,0)
    
    assert calc.div(6,0) == None

    ## x = 0
    assert calc.div(0,20) == 0 

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
def test_mod():
    assert calc.mod(12,5) == 2
    assert calc.mod(-12,5) == 3
    assert calc.mod(21,4) == 1

    ## y = 0 
    with pytest.raises(ValueError):
        calc.mod(2,0)


@pytest.mark.Integration
def test_abs():
    assert calc.abs(5) == 5
    assert calc.abs(-5) == 5
    assert calc.abs(0) == 0


@pytest.mark.April_Release
def test_get_power():
    assert calc.get_power(2,3) == 8
    assert calc.get_power(5,0) == 1
    assert calc.get_power(2,-2) == 0.25
    assert calc.get_power(-2,3) == -8
    assert calc.get_power(-2,4) == 16
    assert calc.get_power(3,3) == 27









