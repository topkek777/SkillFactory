money = int(input('Введите сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [round(0.01 * i * money) for i in per_cent.values()]  # использовал round, чтобы не было числ вида 5599.99999
print(deposit)

print("Максимальная сумма, которую вы можете заработать — %i" % (max(deposit)))