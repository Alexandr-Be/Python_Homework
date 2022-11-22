# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.

for x in True, False:
    for y in True, False:
        for z in True, False:
            statement = (not (x or y or z) == (not x and not y and not z))
            if statement:
                print(f"Утверждение истинно {x} {y} {z}")
            else:
                print(f"Утверждение ложно {x} {y} {z}")
