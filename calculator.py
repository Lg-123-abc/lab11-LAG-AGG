"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError as e:
        print("Value Error")
        return None

def hypotenuse(a,b):
    return math.hypot(a, b)

# First example

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):   # raise ZeroDivisionError if a == 0
    try:
        a/b
    except ZeroDivisionError as e:
        print("Zero Division Error")

def logarithm(a, b): # use math library/raise ValueError
    return math.log(a,b)

def exponent(a, b):
    return a ** b