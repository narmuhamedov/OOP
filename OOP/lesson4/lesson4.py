import re

# 1 - Поиск конкретного слова
text = 'This dog is very funny!'
pattern = r'dog'
print(re.findall(pattern, text))

# 2 - работа с цифрами
text_2 = "My number is 12345"
pattern2 = r'\d'
print(re.findall(pattern2, text_2))

# 3 последовательность чисел
text_3 = "This code is 12 or 34 or 5 and 67890"
pattern3 = r"\d+"
print(re.findall(pattern3, text_3))

# 4 поиск букв без учета регистра
text_4 = "Hello3World hello PythOn"
pattern4 = r"[a-zA-Z]"
print(re.findall(pattern4, text_4))

# 5 Поиск email адресов
text_5 = "This contact has email - mouse@gmail.com"
pattern5 =  r"\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]{2,}\b"
print(re.findall(pattern5, text_5))
# 6 Поиск по IP
my_ip = "My IP is 192.168.168.1"
pattern_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
print(re.findall(pattern_ip, my_ip))

#\b - \b - граница слова
# \d - цифра от 0 - 9
# {1,3} - кол-во повторов предыдущего действия
# \. - символ точки