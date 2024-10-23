# условные операторы и циклы
# 24 августа по 22 сентября. - ДЕВА





# while for
# apple = 10
# bad_box = 0
# good_box = 0
#
# while apple != 0:
#     print(f'Кол-во яблок - {apple}')
#     answer = int(input('Какое яблоко 1-хорошее 2-плохое '))
#     good = 1
#     bad = 2
#     if answer == good:
#         apple -= 1
#         good_box += 1
#         print(
#             f'Хорошие яблоки - {good_box}\n'
#             f'Плохие яблоки - {bad_box}')
#     elif answer == bad:
#         apple -= 1
#         bad_box += 1
#         print(
#             f'Хорошие яблоки - {good_box}\n'
#             f'Плохие яблоки - {bad_box}')
#
# print('-'*20)
# print(
#     f'Хорошие яблоки - {good_box}\n'
#     f'Плохие яблоки - {bad_box}')

# while 1:
#     color = str(input('Какой цвет светофора сейчас горит? '))
#
#     green = 'зеленый'
#     red = 'красный'
#     yellow = 'желтый'
#
#     if color == green:
#         print(f'Сейчас горит - {color} Двигайтесь')
#     elif color == red:
#         print(f'Сейчас горит - {color} Остановитесь')
#     elif color == yellow:
#         print(f'Сейчас горит - {color} Готовьтесь')
#     else:
#         print(f'Действуй по ситуации')
#
#     exit = str(input('Вы хотите выключить светофор? да/нет '))
#     if exit == 'да':
#         break
#     elif exit == 'нет':
#         continue
#     else:
#         print('Сломалась программа')
#         break

# count = 0
# while count != 1000:
#     count += 1
#     print(count)


# == , >=, <=, !=, or , and ,not
# day = int(input('Введите день вашего рождения? '))
# month = int(input('Введите месяц рождения? '))
#
# if day >= 24 and month == 8 and day <= 31 or day <= 22 and month == 9 and day >= 1:
#     print('Вы дева')
# else:
#     print('Ошибка в логике  или вы не дева ')

# if elif else


#
# color = str(input('Какой цвет светофора сейчас горит? '))
#
# green = 'зеленый'
# red = 'красный'
# yellow = 'желтый'
#
# if color == green:
#     print(f'Сейчас горит - {color} Двигайтесь')
# elif color == red:
#     print(f'Сейчас горит - {color} Остановитесь')
# elif color == yellow:
#     print(f'Сейчас горит - {color} Готовьтесь')
# else:
#     print(f'Действуй по ситуации')
#


# name = str(input('Как тебя зовут? '))
# print(f'Привет - {name.capitalize()}')
