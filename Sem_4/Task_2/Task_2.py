# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('введите натуральное число N = '))
# number = 330
divisors = []
#  ищем все множители и заносим в список
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print(f'список множителей числа N {divisors}')
simple_divisors = []
# ищем простые числа в списке множителей
for i in divisors:
    i_pos = divisors.index(i)
    for j in divisors[1:i_pos]:
        if i % j == 0:
            break
    else:
        simple_divisors.append(i)
print(f'список простых множителей числа N {simple_divisors}')
