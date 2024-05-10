'''Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''

# 2
import json
import csv
import pickle
import os


l_data = []
frmt = ['path', 'name', 'type', 'size']


def tree_dir(directory: str, sum_size=0):

    sl = {}
    print('in: ', directory)

    for i, f in enumerate(os.listdir(directory)):

        full_path = os.path.join(directory, f)

        if os.path.isfile(full_path):
            s = os.path.getsize(full_path)
            sum_size += s
            print(f'file: {i} - {f}  Size: {s}')
            sl = {frmt[0]: directory, frmt[1]: f, frmt[2]: 'F', frmt[3]: s}
        elif os.path.isdir(full_path):
            print(f'dir: {i} - {f}')
            tree_dir(full_path, sum_size)
            sl = {frmt[0]: directory, frmt[1]: f, frmt[2]: 'D', frmt[3]: sum_size}
        else:
            print(f'none object: {i} - {f}')

        l_data.append(sl)
        #return sum_size


# tree_dir(pathlib.Path(__file__))
tree_dir(os.getcwd())
#print(l_data)


# сохраним в json
with open("new_pr8.json", "w") as f:
    json.dump(l_data, f)
