# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
import math
n = int(input('Input number of random digits: '))
numbers = []
for i in range(0, n):
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

square_list = []
for n in numbers:
    if n > 0:
        x = n**0.5
        if x % 1 == 0:
            square_list.append(int(x))
print("Squares:  ", square_list)
