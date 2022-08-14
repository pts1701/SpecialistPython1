# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palin(number):
    if str(number) == str(number)[::-1]:
        return True
    
a = 1
b = 999

for i in range(a, b+1):
    if palin(i):
        print(i)
