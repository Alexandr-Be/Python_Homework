import random
list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_mixed = list_original[:]
list_length = len(list_mixed)
for i in range(list_length):
    index_random = random.randint(0, list_length - 1)
    list_mixed[i], list_mixed[index_random] = list_mixed[index_random], list_mixed[i]

print("Исходный список: ")
print(list_original)
print("Перемешанный список: ")
print(list_mixed)