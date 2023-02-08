my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг {my_list}')
# print('Введите число в рейтинг, либо введите 0 для выхода: ')
digit = int(input('Введите число в рейтинг, либо введите 0 для выхода: '))
while digit != 0:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f'Текущий рейтинг - {my_list}')
    digit = int(input('Введите число в рейтинг, либо введите 0 для выхода: '))

