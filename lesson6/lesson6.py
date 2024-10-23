# lambda func / Try expect

while True:
    try:
        number_1 = float(input('Enter a number1: '))
        number_2 = float(input('Enter a number2: '))
    except ValueError:
        print('Пожалуйста пишите только число')
        continue

    operation = input('Enter an operation (+ - / *): ')

    if operation not in ['+', '-', '*', '/']:
        print('Пожалуйста, используйте только + - * /')
        continue

    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + number_2}')

    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    elif operation == '*':
        print(f'{number_1} * {number_2} = {number_1 * number_2}')

    elif operation == '/':
        if number_2 != 0:
            print(f'{number_1} / {number_2} = {number_1 / number_2}')
        else:
            print('Division by zero is not allowed')

# a = 'Asema'
# b = 12
#
# try:
#     print(a+b)
# except TypeError:
#     print('Ошибка в типе данных проверьте код')
#
#


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# numbers_1 = list(filter(lambda number: number % 2 == 1, numbers))
# print(numbers_1)
#
#


# numbers = [1, 2, 3, 4, 5]
#
# double_numbers = map(lambda double_number: double_number*2, numbers)
#
# print(list(double_numbers))


# fruits = ['apple', 'banana', 'cherry', 'strawberry', 'orange']
#
# filter_fruits = list(filter(lambda fruit: len(fruit) == 5, fruits))
# print(filter_fruits)


# square = lambda a, b: a * b
#
# count = 0
# while count != 2:
#     count += 1
#     print(square(int(input('Enter a number1: ')),
#                  int(input('Enter a number2: '))))
#


# def square(a, b):
#     return a * b
#
#
# count = 0
#
# while count != 5:
#     count += 1
#     print(square(int(input('Enter a number1: ')),
#                  int(input('Enter a number2: '))))
