import math

# First example
def add(a, b):
    return a + b

def sub(a,b)
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a

def log(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError()
    else:
        return math.log(b, a)

def exp(a, b):
    return math.pow(a, b)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b): # use math library/raise ValueError
    return math.log(a,b)

def exponent(a, b):
    return a ** b
