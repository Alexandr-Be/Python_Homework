# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

number = input('введите число: ')
separated = list(number)
if ',' in separated:
    separated.remove(',')
if '.' in separated:
    separated.remove('.')
if '-' in separated:
    separated.remove('-')

sum_figures = 0
for i in range(len(separated)):
    sum_figures += int(separated[i])
print(f'{number} -> {sum_figures}')
