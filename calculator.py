import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):   # raise ZeroDivisionError if a == 0
    try:
        result = a/b
        return result
    except:
        ZeroDivisionError
        return "Zero Division Error: Cannot Divide by 0"
def logarithm(a, b): # use math library + try/catch
    try:
        result = math.log(a,b)
    except:
        b=1
        result = 0
        a>=0
        a!=1
def exponent(a, b): # use math library + try/catch
    try:
        return a**b
    except:
        a=0
        b=0
        return "cannot raise 0 to 0th power"