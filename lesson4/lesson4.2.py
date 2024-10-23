KKC = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
# Удалить bag
del KKC['bag']
# Изменить адрес на нынешний
KKC.update(address='Турусбекова 109/2')
# Добавить номер телефона и инстаграмм аккаунт КИЦА
KKC.update(instagram='kkc.instagram.com')
KKC.update(phone_number='+1555555555')
# Добавить/расширить список актуальными курсами, которые вы знаете.
courses = ['Ux-Ui', 'Server Programming', 'English']
KKC['courses'].extend(courses)
# Затем преобразовать этот список в кортеж
KKC['courses'] = tuple(KKC['courses'])
# Вывести словарь на экран с помощью цикла for с получением всех пар
for key, value in KKC.items():
    print(key, value)