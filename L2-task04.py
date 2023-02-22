l = list(input('Введите целые числа: '))

l[::2], l[1::2] = l[1::2], l[::2]
print(' '.join([str(i) for i in l]))