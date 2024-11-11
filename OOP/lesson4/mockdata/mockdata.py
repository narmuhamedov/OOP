import re

# file_path = 'class_mock_data.txt'
# result_path = 'gmail.txt'
# file_read = open(file_path, mode='r', encoding='Latin')
# file_write = open(result_path, mode='w', encoding='Latin')
# class_text = file_read.read()
# searcher_email = r'[\w\.-]+@[\w\.-]+\.\w+'
# result_all = re.findall(searcher_email, class_text)
#
# for i in result_all:
#     print(i)
#     file_write.write(i+'\n')
# print(f'Result: {str(len(result_all))}')
# #
#
file_path = 'class_mock_data.txt'
result_path = 'type_file.txt'
file_read = open(file_path, mode='r', encoding='Latin')
file_write = open(result_path, mode='w', encoding='Latin')
class_text = file_read.read()
searcher_email = r"\b\w+\.(?:doc|pdf|xls|ppt|mp3|mpeg|mov|jpeg|png|tiff|gif|avi|txt)\b"
# searcher_email = r"\.\w+"
result_all = re.findall(searcher_email, class_text)

for i in result_all:
    print(i)
    file_write.write(i+'\n')
print(f'Result: {str(len(result_all))}')

# #
# # (?:doc|pdf|xls|ppt|mp3|mpeg|mov|jpeg|png|tiff|gif|avi|txt)\b по частям:
# #
# # \b — это граница слова. Она указывает начало или конец слова, то есть позволяет нам найти отдельные слова, которые не связаны с другими буквами или цифрами с обеих сторон. Например, \bfilename найдет "filename", но не "myfilename".
# #
# # \w+ — это одна или несколько буквенно-цифровых символов (буквы, цифры и подчеркивания). Этот фрагмент отвечает за название файла перед расширением, например, "PedeUllamcorper" в "PedeUllamcorper.mpeg".
# #
# # \w соответствует одному символу (букве, цифре или подчеркиванию).
# # + означает, что должно быть одно или более таких символов, т.е. название файла должно содержать как минимум один символ.
# # \. — это точка перед расширением файла. Обратите внимание, что точку нужно экранировать, так как в регулярных выражениях точка сама по себе означает "любой символ". Поэтому \. точно находит точку.
# #
# # (?: ... ) — это группа, содержащая возможные расширения файлов. Знак ?: делает группу "незахватывающей", что означает, что она используется только для сопоставления, но не создает отдельный подгрупповой результат. Это позволяет регулярному выражению найти расширение, но не выделять его отдельно в результате.
# #
# # doc|pdf|xls|ppt|mp3|mpeg|mov|jpeg|png|tiff|gif|avi|txt — это перечисление возможных расширений файлов, разделенных вертикальной чертой |, что обозначает логическое "или". Регулярное выражение проверит наличие любого из этих расширений. Например, mpeg соответствует только "mpeg".
# #
# # \b — еще одна граница слова после расширения файла. Это гарантирует, что расширение будет самостоятельной частью, а не частью более длинного слова (например, jpeg123 не подойдет).