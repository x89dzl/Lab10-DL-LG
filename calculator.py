import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("both the base and the x must be positive")
    return math.log(b, a)

def exp(a, b):
    if b == 0 and a == 0:
        raise ValueError("really bro don't do that")
    return a ** b




