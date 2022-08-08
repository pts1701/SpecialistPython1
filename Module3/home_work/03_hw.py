# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
for i in range(0, 20):
    i = random.randint(-100, 100)
    numbers.append(i)
print("input= ", numbers)    

even_positive = []
for i in numbers:
    if i > 0 and i % 2 ==0:
        even_positive.append(i)

print("All even positive =", even_positive)

summa = sum(even_positive)

print("Sum of all positives = ", summa)

# TODO: your code here
