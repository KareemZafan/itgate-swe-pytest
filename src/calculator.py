
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if  y == 0: 
        return None
    return x / y        

def mod(x, y):
    if  y == 0: 
        return None
    return x % y

def abs(x): 
    if x < 0:
        return -x
    return x   

def get_square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def get_power(x,y):
    return math.pow(x,y) 

def get_factorial(x):
    if x < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    return math.factorial(x) # 3 == 6 , 5 == 120,...