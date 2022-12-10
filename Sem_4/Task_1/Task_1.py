# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

print(f'π = {math.pi}')


def round_up(degree):
    res = math.pi * (10 ** degree)
    res = int(res + 0.5)
    res = res / (10 ** degree)
    return res


for d in range(1, 11):
    d_value = 10 ** -d
    print(f'при $d = {d_value}, π =  {round_up(d)}.$')
