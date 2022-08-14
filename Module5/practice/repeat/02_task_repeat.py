# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    if str(number) == str(number)[::-1]:
        result = "Yes"
    else:
        result = "No"
    return result

chislo = int(input("enter number: "))
print(palindrome(chislo))
