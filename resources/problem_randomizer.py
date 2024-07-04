import random

import math


def randomize():
    operands = ['+', '-', '*', '/', 'sqrt']
    operand = random.choice(operands)
    if operand in ['sqrt']:
        value = None
    elif operand == '/':
        value = random.randint(1, 10)
    else:
        value = random.randint(1, 20)
    return operand, value


def get_bonus_problems(score):
    while True:
        operand1, value1 = randomize()
        operand2, value2 = randomize()

        if operand1 != operand2 or value1 != value2:
            result1 = apply_operation(score, operand1, value1)
            result2 = apply_operation(score, operand2, value2)
            if abs(result1 - result2) >= score * 0.2 and (result1 > 0 or result2 > 0):
                break

    return operand1, value1, operand2, value2


def apply_operation(score, operand, value):
    result = score
    if operand == '+':
        result += value
    elif operand == '-':
        result -= value
    elif operand == '*':
        result *= value
    elif operand == '/':
        result //= value
    elif operand == 'sqrt':
        result **= 0.5

    return int(result)
