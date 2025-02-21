# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def decor(func):
    def wrapper():
        result = func()
        n = len(result) + 4
        print('*' * n)
        print('*', result, '*')
        print('*' * n)
    return wrapper

@decor
def fun():
    return input('Input smth:')

fun()
