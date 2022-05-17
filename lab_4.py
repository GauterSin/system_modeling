import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve
from pprint import pprint


"""
Каменьщиков Семён
Вариант 4
"""


def func(
        x1,
        x2,
        x3
        ):
    return x1 * x2 * x3


def func_1(
        x1,
        x2,
        x3
        ):
    return 2 * x1 * x2 + x2 * x3


def func_2(
        x1,
        x2,
        ):
    return 2 * x1 - x2


def func_condition(x: list):
    return [
            2 * x[0] * x[1] + x[1] * x[2] - 12,
            2 * x[0] - x[1] - 8]

# result = fsolve(func_condition, [0,0,0]) 
# print(result)


x1, x2, x3, f = symbols('x1, x2, x3, f')
eq1 = Eq((2 * x1 * x2 + x2 * x3), 12)
eq2 = Eq((2 * x1 - x2), 8)
eq3 = Eq((x1 * x2 * x3), 1)


result = solve((eq1, eq2, eq3), (x1, x2, x3))
pprint(result)

# x1_n, x2_n, x3_n = (x for x in result)
# print(x1_n)

