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


tree_dir(os.getcwd())

# сохраним в json, csv, pickle
with (open('new_pr8.json', 'w') as f_json,
    open('new_pr8.csv', 'w', newline='', encoding='utf-8') as f_csv,
    open('new_pr8.pickle', 'wb') as f_pickle):

    #json
    json.dump(l_data, f_json, indent=2)

    #csv
    file_writer = csv.DictWriter(f_csv, delimiter=',', lineterminator="\r", fieldnames=frmt)
    file_writer.writeheader()
    file_writer.writerows(l_data)

    #pickle
    pickle.dump(l_data, f_pickle)