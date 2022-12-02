# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math


def multiplications_couples(some_list):
    couples_list = []
    cykle_len = math.ceil(len(some_list)/2)
    j = -1
    for i in range(0, cykle_len):
        couples_list.append(some_list[i]*some_list[j])
        j -= 1
    return couples_list


list_1 = [2, 3, 4, 5, 6]
list_2 = [2, 3, 5, 6]
list_3 = [12, 5, 15, 29, 32, 8, 9]
list_4 = [2, 3, 5, 9, 3, 7, 4, 2]

print(f'{list_1} => {multiplications_couples(list_1)}')
print(f'{list_2} => {multiplications_couples(list_2)}')
print(f'{list_3} => {multiplications_couples(list_3)}')
print(f'{list_4} => {multiplications_couples(list_4)}')

