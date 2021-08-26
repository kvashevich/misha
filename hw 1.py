from datetime import date

name = input('Ваше имя: ')
lastname = input('Ваша фамилия: ')

country = input('В какой стране живете: \n 1 - Рспублика Беларусь \n 2 - РФ \n 3 - Щэ не вмэрла Украина'
                ' \n Выберите номер: ')

country_dict = {'1': 'Республика Беларусь', '2': 'РФ', '3': 'Щэ не вмэрла Украина'}
year = input('Ваш год рождения:   ')
month = input('Ваш месяц рождения:   ')
day = input('Ваш день рождения:   ')
today = date.today()
extra_year = 1 if (today.month, today.day) < (int(month), int(day)) else 0
age = today.year - int(year) - extra_year
print(f' Ваши данные \n {name} {lastname}, {age}, {country_dict[country]}')


