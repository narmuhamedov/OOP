university = []
college = []
army = []
married = []

abuturients = [
    {'name': 'Адилет', 'ORT': 110, 'gender': 'male'},
    {'name': 'Арафат', 'ORT': 10, 'gender': 'male'},
    {'name': 'Атай', 'ORT': 70, 'gender': 'male'},
    {'name': 'Асема', 'ORT': 120, 'gender': 'female'},
    {'name': 'Иван', 'ORT': 50, 'gender': 'male'},
    {'name': 'Эльдана', 'ORT': 90, 'gender': 'female'},
    {'name': 'Лия', 'ORT': 40, 'gender': 'female'},
    {'name': 'Адель', 'ORT': 30, 'gender': 'female'},
    {'name': 'Элеонора', 'ORT': 105, 'gender': 'female'},
    {'name': 'Аман', 'ORT': 140, 'gender': 'male'},
]


def all_abit(lst):
    for i in lst:
        for k, v in i.items():
            print(f'{k}-{v}')


all_abit(abuturients)


def selection(lst, university: list, college: list, army: list, married: list):
    for i in lst:
        if i['ORT'] >= 110:
            university.append(i)
        elif i['ORT'] >= 70 and i['ORT'] <= 109:
            college.append(i)
        elif i['ORT'] < 70 and i['gender'] == 'male':
            army.append(i)
        elif i['ORT'] < 70 and i['gender'] == 'female':
            married.append(i)

selection(abuturients, university, college, army, married)

print('-'*50)
print(f'В универ пошли {university}\n'
      f'В колледж пошли {college}\n'
      f'В армию пошли {army}\n'
      f'Замуж вышли {married}')