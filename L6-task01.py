# n = int(input('Input n '))
# a = [0]*n
# a[0] = int(input('Input a[0] '))
# d = int(input('Input d '))
# print(a[0],end=' ')
# for i in range(1,n):
#     a[i]= a[i-1]+d
#     print(a[i],end=' ')
#
# # Тестовое решение:
# # Input n 10
# # Input a[0] 5
# # Input d 3
# # 5 8 11 14 17 20 23 26 29 32

a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)

