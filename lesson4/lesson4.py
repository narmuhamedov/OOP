import random

# Ввод количества элементов
N = int(input("Введите количество элементов: "))

# Шаг 1: Генерация списка из N чисел от -30 до 10
numbers = [random.randint(-30, 10) for _ in range(N)]
print("Сгенерированный список:", numbers)
 
# Шаг 2: Поиск максимального элемента и его индекса
max_element = max(numbers)
max_index = numbers.index(max_element)
print("Максимальный элемент:", max_element, "с индексом", max_index)

# Шаг 3: Удаление максимального элемента, если его индекс нечётный
if max_index % 2 != 0:
    numbers.pop(max_index)
    print("Максимальный элемент удалён. Новый список:", numbers)
else:
    print("Максимальный элемент не удалён, так как его индекс чётный.")

# Шаг 4: Добавление индекса максимального элемента в конец списка
numbers.append(max_index)
print("Список после добавления индекса максимального элемента:", numbers)

# Шаг 5: Вывод чисел, расположенных между 1 и 5 элементами
if len(numbers) > 5:
    sublist = numbers[1:5]
    print("Элементы между 1 и 5 позициями:", sublist)
else:
    print("В списке меньше 5 элементов, не удалось извлечь подсписок.")

# Шаг 6: Поиск суммы отрицательных элементов
negative_sum = sum(num for num in numbers if num < 0)
print("Сумма отрицательных элементов:", negative_sum)

