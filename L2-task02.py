number = input('Ведите целое положительное число: ')
a = 0
for i in number:
    while int(i) > a:
        a = int(i)
print(a)