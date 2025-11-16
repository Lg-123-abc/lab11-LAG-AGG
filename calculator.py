## https://github.com/Lg-123-abc/lab11-LAG-AGG
## Partner 1: Lillian Groudas
## Partner 2: Alexander Groudas

import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a

def logarithm(a, b): # use math library/raise ValueError
    return math.log(a, b)

def exp(a, b):
    return math.pow(a, b)

def square_root(a):
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)