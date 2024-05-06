'''Урок 7. Файлы и файловая система
Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию группового переименования файлов. Она должна:
    a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    b. принимать параметр количество цифр в порядковом номере.
    c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    d. принимать параметр расширение конечного файла.
    e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.'''

#2
import os
from pathlib import Path

def rename_files(new_name: str, cnt_num: int, old_ext: str, new_ext: str, range_old_name: list[int]):
    n = 0
    for i, file in enumerate(os.listdir()):
        if file.endswith(old_ext):
            n += 1
            #os.rename('old.txt', 'new.txt')
            Path(file).rename(f'{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}')


rename_files(4, 'pip', 'zip', [2, 4], "new")
#3
'''import json
l = l_comp = []
sl = {}

with open("pr7.txt", "r", encoding="utf-8") as f:
    sum_aver = i = 0
    for line in f:
        l = line.split(" ")

        sum_n = float(l[2]) - float(l[3])
        if sum_n > 0:
            sum_aver = sum_aver + sum_n
            i += 1

        sl[l[0]] = sum_n
    l_comp.append(sl)
    l_comp.append({"average_profit": sum_aver / i})
print(l_comp)

with open("pr5_7.json", "w") as f:
    json.dump(l_comp, f)
    '''