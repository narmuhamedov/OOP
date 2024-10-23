# сеты

lagman = {'мясо', 'лапша', 'специи', 'картошка', 'редька', 'лук'}

borsh = {'мясо', 'капуста', 'свекла', 'картошка', 'лук', 'перец'}

#нахождение похожих значений
print(lagman.intersection(borsh))

#Выводить микс значения
print(lagman.union(borsh))

#не совпадения значений
print(lagman.difference(borsh))

#вывод не одинаковых значений
print(lagman.symmetric_difference(borsh))





# nominal = (1, 3, 5, 10, 20, 50, 100, 200, 500, '1k', '2k', '5k')
# persons = ('no', 'no', 'no', 'no', 'Togolok Moldo', 'Kurmanjan Datka', 'Toktogul Satylganov',
#            'Alykul Osmonov', 'Sayakbai Karalaev', 'Jusup Balasagyn', 'Manas', 'Chokmorov')
#
# money = dict(zip(nominal, persons))
#
# for key, value in money.items():
#     print(key, value)
#
# print(money)



# словари и сеты

student = {
    'name': 'Radomir',
    'age': 27,
    'city': 'Bishkek',
    'height': 1.86,
    'telefone': ['0555123321', '0773123321'],
    1997: True,
    False: 34.432,
}

# for key, value in student.items():
#     print(f'{key}: {value}')
#
# print(f'{key}- {value}')


# create
student.update(eductation=True)
student['name'] = 'Antony'
# update
student['name2'] = 'Timur'
student.update(age=21)

# delete
del student[False]

# print(student['telefone'][1])
# print(student.get('city'))

#print(student)
