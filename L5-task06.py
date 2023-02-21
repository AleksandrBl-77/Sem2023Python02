import random
mysterious_number = random.randrange(0, 100)

for i in range(10, 0, -1):
  x = int(input('Ваше предположение : '))
  if x == mysterious_number:
    print('ВЕРНО !!!')
    exit()
  elif x < mysterious_number:
    print('Это число меньше')
  else:
    print('Это число больше')

print('Вы проиграли, загаданное число: ', mysterious_number)