# Задание
# * Создайте список словарей:
#         [
#         {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#         {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#         {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#     ]
# * Запишите содержимое списка словарей в файл в формате csv


import csv

with open('export.csv', 'w', encoding='utf-8') as myfile:
    mylist = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(myfile, fields, delimiter=';')
    writer.writeheader()
    for user in mylist:
        writer.writerow(user)