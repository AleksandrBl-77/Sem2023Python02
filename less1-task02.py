n = int(input('Введите трех значное число:  '))
summa = 0

while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10

print(summa)













