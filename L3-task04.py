products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование обязательно. Попробуйте еще раз: ')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть указанна. Попробуйте еще раз: ')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть указанно. Попробуйте еще раз: ')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица измерения обязательна. Попробуйте еще раз: ')
        continue

    unit = tmp

    products.append((
        order,
        {'Название товара': title, 'Цена товара': price, 'Количество': amount, 'единиц': unit}
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (Y/N)) ')
    if q.lower() == 'y':
        break

# analitics = {'title': [], 'price': [], 'amount': [], 'unit': set()}
#
# for _, item in products:
#     analitics['title'].append(item['title'])
#     analitics['price'].append(item['price'])
#     analitics['amount'].append(item['amount'])
#     analitics['unit'].add(item['unit'])
#
# print(analitics)

#
# goods = []
# while input('Добавить товар? Введите да/нет: ') == 'да':
#     number = int(input('Введите название товара: '))
#     features = {}
#     while input('Добавить данные товара? Ведите да/нет: ') == 'да':
#         feature_key = input('Введите цену товара: ')
#         feature_value = input("Ведите колличество в штуках: ")
#         features[feature_key] = feature_value
#     goods.append(tuple([number, features]))
# print(goods)
# goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
# analitics = {}
# for good in goods:
#     for feature_key, feature_value in good[1].items():
#         if feature_key in analitics:
#             analitics[feature_key].append(feature_value)
#         else:
#          analitics[feature_key] = [feature_value]
# print(analitics)
