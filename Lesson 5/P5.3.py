# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("new_f.txt", 'w') as file:
    a = 1
    while a != 0:
        a = file.write(input("Введите фамилию сотрудника и велечину оклада через пробел (в рублях): "))
        file.write('\n')

with open("new_f.txt") as file:
    file = list(file)
    file.pop(-1) # удаляем пустую строку, оставшуюся от заполнения
    summa = 0
    for line in file:
        b = line.split()
        summa = summa + int(b[1])
        if int(b[1]) >= 20000:
            print("Фамилия сотрудника с доходом больше 20т.р.: ", b[0])
    av_payment = summa / len(file)
    print("Средняя зарплата:", av_payment)
