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
    return math.log(a,b)

def exp(a, b):
    return math.pow(a, b)

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError as e:
        print("Value Error")
        return None

def hypotenuse(a,b):
    return math.hypot(a, b)