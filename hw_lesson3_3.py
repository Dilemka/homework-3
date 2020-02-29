# Задание
# Скачайте файл по ссылке
# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt


with open('referat.txt', 'r', encoding='utf-8') as myfile:

    content = myfile.read()
 
    # Считаю длину строки (кол-во символов)
    ln = len(content.replace('\n', ' '))
    print(f'Длина текста: {ln}')

    # Заменяю точки на воскл знаки
    content = content.replace('.', '!')
    print (content)

# Считаю кол-во слов
world = 0
for wd in content.split():

    if wd != ' ':
        world +=1
    else:
        world +=0
print(f'Общее количество слов в тексте: {world}')

with open('myfile.txt', 'w', encoding='utf-8') as myfile:

    myfile.writelines(content)