# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# сделал задачу по математическому правилу сложения многочленов:
# - раскрываем скобки
# - складываем элементы многочлена
# - записываем новый многочлен

import unicodedata


# читаем многочлен
def read_polinom(file_name):
    f = open(file_name, 'r')
    source_polinom = f.read() + ' '
    f.close()
    return source_polinom


# находим элементы многочлена
def determine_elements(data):
    elements = []
    while data != '':
        spase_pos = data.index(' ')
        el = data[:spase_pos]
        if el not in ['+', '-', '=', '0\n']:
            elements.append(el)
        data = data[spase_pos + 1:]
    return elements


# находим коэффициенты элементов
def determine_rat(array):
    ratio = []
    for item in array:
        if '*x' in item:
            separator_pos = item.index('*x')
            ratio.append(item[:separator_pos])
        else:
            ratio.append(item)
    return ratio


# находим степени элементов
def determine_degr(array):
    degree = []
    for item in array:
        if '*x' in item:
            separator_pos = item.index('*x')
            degree.append(unicodedata.normalize("NFKC", (item[separator_pos + 2:])))
    return degree


# превращаем строки в числа
def str_to_int(array):
    new_array = []
    for i in array:
        if i:
            new_array.append(int(i))
        else:
            new_array.append(1)
    return new_array


# делаем словарь, где key = степень, а value = коэффициент
def polinom_dict(arr1, arr2):
    arr = {}
    for i in range(len(arr1)):
        arr[arr1[i]] = arr2[i]
    arr[0] = arr2[-1]
    return arr


# складываем словари
def sum_dict(dict1, dict2):
    res_dict = dict1.copy()
    for k, v in dict2.items():
        try:
            res_dict[k] += v
        except KeyError:
            res_dict[k] = v
    return res_dict


# собираем новый многочлен. вспомогательная ф-ция out_determine делает вывод степени надстрочным
def out_determine(degree):
    if 2 <= degree <= 3:
        out = chr(0x00b0 + degree)
    else:
        out = chr(0x2070 + degree)
    return out


def polynomial_assembling(dict_ratios):
    # собираем элементы
    assembled_elements = []
    for i in range(len(dict_ratios) - 1, -1, -1):
        if dict_ratios.get(i) == 0:
            continue
        elif i == 0:
            assembled_elements.append(str(dict_ratios.get(i)))
        elif dict_ratios.get(i) == 1:
            assembled_elements.append('x' + out_determine(i))
        elif i == 1:
            assembled_elements.append(str(dict_ratios.get(i)) + '*x')
        else:
            assembled_elements.append(str(dict_ratios.get(i)) + '*x' + out_determine(i))
        # из элементов собираем многочлен
        polynom_assembled = ''
        for item in assembled_elements:
            if item == assembled_elements[-1]:
                polynom_assembled += item + ' = 0'
            else:
                polynom_assembled += item + ' + '
    return polynom_assembled


# записываем в новый файл
def write_polinom(redy_polinom):
    f = open('file3.txt', 'w')
    f.write(redy_polinom + '\n')
    f.close()
    print('готово')


polinom1 = read_polinom('file1.txt')
polinom2 = read_polinom('file2.txt')
elements1 = determine_elements(polinom1)
elements2 = determine_elements(polinom2)
ratio_str1 = determine_rat(elements1)
ratio_str2 = determine_rat(elements2)
degree_str1 = determine_degr(elements1)
degree_str2 = determine_degr(elements2)
ratios1 = str_to_int(ratio_str1)
ratios2 = str_to_int(ratio_str2)
degrees1 = str_to_int(degree_str1)
degrees2 = str_to_int(degree_str2)
ratios_for_sum1 = polinom_dict(degrees1, ratios1)
ratios_for_sum2 = polinom_dict(degrees2, ratios2)
ratios_for_new_polinom = sum_dict(ratios_for_sum1, ratios_for_sum2)
new_polinom = polynomial_assembling(ratios_for_new_polinom)
write_polinom(new_polinom)
