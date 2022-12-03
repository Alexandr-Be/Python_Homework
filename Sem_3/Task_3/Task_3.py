# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def difference(some_list):
    elements_difference = max_fract(some_list) - min_fract(some_list)
    # elements_difference = format(elements_difference, '.2f')
    # elements_difference = round(elements_difference, 4)
    # elements_difference = '%.2f' % elements_difference
    return elements_difference


def max_fract(some_list):
    max_fract_part = (some_list[0] - some_list[0] // 1)
    for i in range(1, len(some_list)):
        if (some_list[i] - some_list[i] // 1) > max_fract_part:
            max_fract_part = (some_list[i] - some_list[i] // 1)
    return max_fract_part


def min_fract(some_list):
    min_fract_part = (some_list[0] - some_list[0] // 1)
    for i in range(1, len(some_list)):
        if (some_list[i] - some_list[i] // 1) < min_fract_part:
            min_fract_part = (some_list[i] - some_list[i] // 1)
    return min_fract_part


list_1 = [1.1, 1.2, 3.1, 5, 10.01]
print(f'{list_1} => {difference(list_1)}')
