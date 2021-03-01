# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
with open("numbers.txt", 'w', encoding="utf-8") as file:
    file.write("".join([str(randint(1, 100)) for _ in range(100)]))
with open("numbers.txt", encoding="utf-8") as file:

    a = file.read()
    a = a.split()

    print(a)
    summa = 0
    for i in a:
        summa = summa + int(i)
    print("Сумма чисел: ", summa)





