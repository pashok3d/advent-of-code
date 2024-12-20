"""
1. Read input
2. For each equation:
    2.1 generate all combinations of operators
    2.2 evaluate the result
"""

from itertools import product

OPERATORS = ["+", "*"]

with open("2024/7/input7.txt", "r") as f:
    lines = f.readlines()

sum = 0


def evaluate(params: list[int], combination: tuple[str], result: int):
    if combination[0] == "+":
        eval_result = params[0] + params[1]
    else:
        eval_result = params[0] * params[1]

    for param, operator in zip(params[2:], combination[1:]):
        if operator == "+":
            eval_result += param
        else:
            eval_result *= param

    return eval_result == result


for line in lines:
    result = int(line.split(":")[0])
    params = list(map(int, line.split(":")[1].split()))
    for combination in product(OPERATORS, repeat=len(params) - 1):
        if evaluate(params, combination, result):
            sum += result
            break

print(sum)
