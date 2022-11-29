# Задайте список из n чисел последовательности $(1+1/n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = abs(int(input('введите целое число: ')))
d = {n: round(((1 + 1/n) ** n), 2) for n in range(1, number + 1)}
print(f'пусть N = {number}, тогда {d}')
sum_elements = sum(d.values())
print(f'Сумма: {sum_elements}')

