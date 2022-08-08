# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Сергей", "Василий", "Петр", "Дмитрий"]

def Max_dlina(names):
    dlina = len(names[0])
    element = names[0]
    for name in names:
        if dlina < len(name):
            dlina = len(name)
            element = name
    return dlina

Max_dlina = Max_dlina(names)
long_names = []
for name in names:
    if len(name) == Max_dlina:
        long_names.append(name)

print(long_names)

# TODO: your code here
