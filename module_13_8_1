def num_ver():
    while True:
        try:
            val = int(input())
            if val < 0:
                raise ValueError("Данное значение не может быть меньше нуля...")
            break
        except:
            print('Введите корректное число!!! ', end='')
    return val

print("Введите количество билетов: ", end='')
amount = num_ver()

print("Введите возраст каждого человека (по одному на строку):")
ages = [num_ver() for _ in range(1, amount + 1)]

total_cost = 0
for i in range(len(ages)):
    if ages[i] < 18:
        continue
    total_cost += (990, 1390)[ages[i] >= 25]  # =)

if len(ages) > 3:
    print(f'Вы зарегистрировали более 3-х человек, вам предоставлена скидка 10%"\n"'
          f'Итоговая стоимость: {0.9 * total_cost} руб')
else:
    print(f'Ваша итоговая стоимость: {total_cost} руб')


