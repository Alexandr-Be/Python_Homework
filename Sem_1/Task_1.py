# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('введите номер дня недели: '))
if number < 0 or 7 < number:
    print(f' - {number} -> не является номером дня недели')
elif number == 6 or number == 7:
    print(f' - {number} -> да')
else:
    print(f' - {number} -> нет')