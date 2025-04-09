import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a): #raise ValueError if a < 0
    if a<0:
        raise ValueError("A cannot be smaller than 0")
    return math.sqrt(a)

def hypotenuse(a, b): #can have negative nums
    return math.hypot(a, b)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    if b == 0 and a == 0:
        raise ValueError("really bro don't do that")
    return a ** b

def subtract(a, b):
    return a - b

def logarithm(a, b): # use math library + try/catch
    try:
        math.log(a,b)
    except a>=0:
        raise ValueError("A must be larger than or equal to 0")
    except a!=1:
        raise ValueError("A cannot equal 1")
    '''except b=1:'''
