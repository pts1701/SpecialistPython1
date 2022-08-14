# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    lst = []
    for i in range(size):
        x = random.randint(of, to)
        lst.append(x)
    return lst

size = int(input('s'))
of = int(input('of'))
to = int(input('to'))
print(gen_list(size, of, to))

