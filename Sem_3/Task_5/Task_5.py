# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


#             **РЕШЕНИЕ МЕТОДОМ ЦИКЛА**
k = int(input('введите число k - количество чисел в списке: '))
fib = 0
n_fib = 0
fib_list = [0, 1]
n_fib_list = [1, 0, 1] #задаём начальные значения в списке, т.к. они неизменны
for i in range(2, k+1):
    fib = fib_list[i - 1] + fib_list[i - 2]
    n_fib = ((-1)**(i+1))*fib
    fib_list.append(fib)
    n_fib_list.append(fib)
    n_fib_list.insert(0, n_fib)
print(f'- для k = {k} список будет выглядеть так: {n_fib_list}')

#             **РЕШЕНИЕ МЕТОДОМ РЕКУРСИИ**
#
# def fibonacci(k):
#     if k <= 1:
#         return k
#     else:
#         return fibonacci(k - 1) + fibonacci(k - 2)
#
#
# k = int(input('введите число k - количество чисел в списке: '))
# n_fib = 0
# n_fib_list = [0]
# for i in range(1, k+1):
#     n_fib = ((-1)**(i+1))*fibonacci(i)
#     n_fib_list.append(fibonacci(i))
#     n_fib_list.insert(0, n_fib)
#
# print(f'- для k = {k} список будет выглядеть так: {n_fib_list}')
