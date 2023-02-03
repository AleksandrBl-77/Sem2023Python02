revenue = int (input('Введите вуручку Вашей фирмы: '))
costs = int (input('Введите издержки Вашей фирмы: '))
worker = int (input('Введите количестко сотрудников Вашей фирмы: '))
result = (revenue - costs)
profitability = (revenue / costs)
if result > 0:
    print(f'финансовый результат - Прибыль в размаре {result} рентабельность {profitability}')
    print(f'Прибыль фирмы в расчете на одного сотрудника = {result / profitability}')
elif result == 0:
    print('финансовый результат - Фирма работает в 0')
else:
    print(f'финансовый результат - Убыток в размаре {result}')