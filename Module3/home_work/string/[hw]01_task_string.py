# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Input text:  ")
stop=[]
comma=[]
for char in text:
    if char == ".":
        stop.append(char)
    if char == ",":
        comma.append(char)
print("Количество точек = ", len(stop))
print("Количество запятых = ", len(comma))

if len(stop) > len(comma):
    print("Точек больше")
elif len(stop) < len(comma):
    print("Запятых больше")
else:
    print("Запятых и точек одинаковое колличество")
