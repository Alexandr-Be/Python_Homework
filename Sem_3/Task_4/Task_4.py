# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def conversation(source_number):
    number = source_number
    result = ''
    while number > 0:
        figure = str(number % 2)
        # result = ''.join(figure)
        # result.insert(0, figure)
        result += figure
        number = number // 2
    print(f'{source_number} -> {result}')


conversation(45)
conversation(3)
conversation(2)
