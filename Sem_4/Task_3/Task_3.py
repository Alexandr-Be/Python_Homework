# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

list_start = [1, 2, 5, 7, 10, 14, 25, 1, 2, 14, 5, 7, 35, 50, 14, 70, 175, 14, 5, 7, 350]
list_res = []
for i in list_start:
    for j in list_start[i+1:]:
        if i == j:
            break
    else:
        list_res.append(i)
print(list_start)
print(list_res)
