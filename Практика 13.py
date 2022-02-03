price = []
ticket = int(input("Введите количество билетов"))
for i in range(1, ticket +1):
    age_for_ticket =int(input(f'Для какого возраста билет №{i}? '))
    if age_for_ticket < 18:
        print ("Билет бесплатный")
    elif 25 >= age_for_ticket >= 18:
        price += [990]
        print('Стоимость билета: 990 руб.')
    else:
        price += [1390]
        print ('Стоимость билета: 1390 руб')
    if ticket > 3:
        price_sale = int(sum(price) - sum (price) / 10)
        print(f'Сумма к оплате {price_sale} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше трех человек')
    else:
        print (f'Сумма к оплате {price} руб.')