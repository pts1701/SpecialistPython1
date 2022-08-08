# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
index = len(names[0])
for name in names:
    if index < len(name):
        index = len(name)

print(index) 
# TODO: your code here
