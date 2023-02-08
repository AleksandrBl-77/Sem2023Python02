my_str = input('Введите строку из нескольких слов: ')
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i}. - {el}')