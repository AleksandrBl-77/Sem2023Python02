n1=int(input('Введите первое натуральное число множества: '))
n_u=int(input('Введите последнее натуральное число множества: '))

i=0

for k in range(n1, n_u+1):
    i+=k
c = (n_u*(n_u+1))/2
if i == c:
    print ('равенство выполняется', i, " = ", c)

else:
    print ('нет')