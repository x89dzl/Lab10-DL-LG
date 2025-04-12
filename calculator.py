'''https://github.com/x89dzl/Lab10-DL-LG
Daniel Li Liam Gale'''
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a): #raise ValueError if a < 0
    if a<0:
        raise ValueError ("A cannot be smaller than 0")
    return math.sqrt(a)

def hypotenuse(a, b): #can have negative nums
    return math.hypot(a, b)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        return "Error cannot divide by 0"
    return b / a

def exp(a, b):
    if b == 0 and a == 0:
        raise ValueError("really bro don't do that")
    return a ** b

def subtract(a, b):
    return a - b

def logarithm(a, b): # use math library + try/catch
    try:
        if a<=0:
            raise ValueError("A must be larger than or equal to 0")
        if a==1:
            raise ValueError("A cannot equal 1")
        if b < 0:
            raise ValueError("Argument cannot be equal to or less than 0 ")
        return math.log(b, a)
    except ValueError as e:
        print(f"Error: {e}")
        raise ValueError
        return None



