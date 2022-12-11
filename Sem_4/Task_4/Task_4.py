# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def out_determine(degree):
    if 2 <= degree <= 3:
        out = chr(0x00b0 + degree)
    else:
        out = chr(0x2070 + degree)
    return out


def polynomial_assembling(k):
    polynomial = str(random.randrange(0, 100)) + '*x + ' + str(random.randrange(0, 100)) + ' = 0'
    for i in range(1, k):
        ratio = random.randrange(0, 100)
        if ratio == 0:
            polynomial = polynomial
        elif ratio == 1:
            polynomial = '*x' + out_determine(i+1) + ' + ' + polynomial
        else:
            polynomial = str(ratio) + '*x' + out_determine(i+1) + ' + ' + polynomial
    return polynomial


res = open('file.txt', 'w')
for k in range(1, 10):
    res.write('k=' + str(k) + ' => ' + polynomial_assembling(k) + '\n')
res.close()
print('готово')
