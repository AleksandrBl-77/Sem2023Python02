def calculation(n, s, c):
    s = s + c
    c = c / -2
    n -= 1
    if n < 1:
        return s
    return calculation(n, s, c)


num = int(input('Введите число: '))
summa = 0
count = 1
z = (calculation(num, summa, count))
print(z)