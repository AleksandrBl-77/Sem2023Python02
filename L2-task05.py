str = input('Введите строку из нескольких слов, разделённых пробелами: ')
a = str.split(' ')
for i, el in enumerate(a, 1):
    print(f"{i}.-{el}")