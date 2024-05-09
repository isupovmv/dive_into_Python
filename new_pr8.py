'''Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''

# 2
import json
import os
import pathlib

l = []
l_comp = []
sl = {}


def tree_dir(directory: str):
    print(directory)
    for i, f in enumerate(os.listdir(directory)):
        print(f'{i} - {f}')

        if os.path.isfile(f):
            s = os.path.getsize(f)
            print(f'{i} - {f} size {s}')
        elif os.path.isdir(f):
            tree_dir(f)
            #os.chdir('..') # подняться на уровень выше


# tree_dir(pathlib.Path(__file__))
tree_dir(os.getcwd())

'''
        with open("pr5_7.txt", "r", encoding="utf-8") as f:
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