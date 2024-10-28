class Animal:
    def __init__(self, name, size, weight, color, habitat, diet):
        self.name = name
        self.size = size
        self.weight = weight
        self.color = color
        self.habitat = habitat
        self.diet = diet

    def jump(self, yes_no):
        print(f'{self.name} can jumping{yes_no}')

    def __str__(self):
        return (f'Название - {self.name}\n'
                f'Размер - {self.size}\n'
                f'Вес - {self.weight}\n'
                f'Цвет - {self.color}\n'
                f'Среда обитания - {self.habitat}\n'
                f'Тип питания - {self.diet}')


class Reptiles(Animal):
    def __init__(self, name, size, weight, color, habitat, diet, body_color, show):
        super().__init__(name, size, weight, color, habitat, diet)
        self.body_color = body_color
        self.show = show

    def change_color(self):
        if self.body_color == 'red':
            return 'Опасность'
        elif self.body_color == 'green':
            return 'Все хорошо'
        else:
            return "неизвестно"

    def __str__(self):
        return super().__str__() + f'\nЦвет тела - {self.body_color}'


chameleon = Reptiles(name='Хамелеон', size=12.3, weight=200, color='green', habitat='Africa', diet='insect',
                     body_color='red', show='Играть на пианино')
print(chameleon)
print(chameleon.change_color())
print(chameleon.jump(False))


class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 1
        if zoo.name == chameleon and zoo.show:
            self.ticket = "100$"

    def result(self):
        return f'Шоу будет стоить: {self.ticket}'

    def __str__(self):
        return f'{self.zoo.name} будет {self.zoo.show}'


chameleon_show = Zoo_show(chameleon)
print(chameleon_show)