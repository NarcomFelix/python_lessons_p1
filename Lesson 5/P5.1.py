# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("new_f.txt", 'w') as file:
    a = 1
    while a != 0:
        a = file.write(input("Введите строку: "))
        file.write('\n')




