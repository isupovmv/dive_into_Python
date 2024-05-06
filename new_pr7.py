'''Урок 7. Файлы и файловая система
Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию группового переименования файлов. Она должна:
    a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    b. принимать параметр количество цифр в порядковом номере.
    c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    d. принимать параметр расширение конечного файла.
    e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного 
    имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.'''

#2
import os
from pathlib import Path

def rename_files(new_name: str, cnt_num: int, old_ext: str, new_ext: str, range_old_name: list[int]):
    for i, file in enumerate(os.listdir('.')):
        if file.endswith(old_ext):
            #old_file = os.path.join("directory", "a.txt")
            #new_file = os.path.join("directory", "b.kml")
            #os.rename(old_file, new_file)
            Path(file).rename(f'{file.split('.')[0][range_old_name[0]:range_old_name[1]]}{new_name}{i:0>{cnt_num}}.{new_ext}')


rename_files('_new', 3, 'txt', 'doc', [2, 5])

#3 из семинара
'''Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
    расширение
    минимальная длина случайно сгенерированного имени, по умолчанию 6
    максимальная длина случайно сгенерированного имени, по умолчанию 30
    минимальное число случайных байт, записанных в файл, по умолчанию 256
    максимальное число случайных байт, записанных в файл, по умолчанию 4096
    количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''
import random
import os

MIN_LETTER = ord('a')
MAX_LETTER = ord('z')

#Генерирует случайное имя файла
def generate_text(length):
    
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
    return ''.join(name)


#Генерирует файлы с заданными параметрами
def generate_files(extension: str,
                   directory: str,
                   min_length=6,
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
    
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        filename = generate_text(name_length)
        text_length = random.randint(min_bytes, max_bytes)
        text = generate_text(text_length)
        while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break


generate_files('rnd', 'files')
