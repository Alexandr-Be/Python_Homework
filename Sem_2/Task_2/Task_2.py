# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = abs(int(input('введите целое число: ')))
multiplications = []
a = 1
for i in range(1, number+1):
    a = a*i
    multiplications.append(a)
print(f'пусть N = {number}, тогда {multiplications}')
