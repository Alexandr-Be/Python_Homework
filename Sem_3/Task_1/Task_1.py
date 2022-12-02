# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def odd_elements(some_list):
    odd_elements = []
    for i in range(1, len(some_list), 2):
        odd_elements.append(some_list[i])
    odd_elements = str(odd_elements).strip("[]")
    return odd_elements


def sum_odd_elements(some_list):
    sum_elements = 0
    for i in range(1, len(some_list), 2):
        sum_elements += some_list[i]
    return sum_elements


list_1 = [2, 3, 5, 9, 3]
list_2 = [12, 5, 15, 29, 32, 8, 9]
list_3 = [2, 3, 5, 9, 3, 7, 4, 2]

print(f'{list_1} -> на нечётных позициях элементы {odd_elements(list_1)}, ответ: {sum_odd_elements(list_1)}')
print(f'{list_2} -> на нечётных позициях элементы {odd_elements(list_2)}, ответ: {sum_odd_elements(list_2)}')
print(f'{list_3} -> на нечётных позициях элементы {odd_elements(list_3)}, ответ: {sum_odd_elements(list_3)}')
