# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = 'брат мыл и брил бороду'


if text.find('б') == 0:
    end = text.find(" ")
    if end >= 0:
        print(text[0:end])
    else:
        print(text[0:])
else:
    start_b = text.find(" б")
    end = text.find(" ", start_b + 1)
    if end >= 0:
        print(text[start_b:end])
    else:
        print(text[start_b:])
