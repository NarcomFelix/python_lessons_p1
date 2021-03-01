# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
# и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_dict = {}
with open('5.6.txt', encoding='utf-8') as f:
    for line in f:
        less, stats = line.split(':') # выделяем название предмета и всё остальное
        less_sum = 0
        help_summ = []
        for el in stats:
            if el == ' ' or (el >= "0" and el < "9"): # из всего остального вычленяем цифры и пробелы (чтобы цифры составные были)
                help_summ.append(el)
        help_summ = ''.join(help_summ).split()
        for el in help_summ: # считаем по каждому предмету
            less_sum = less_sum + int(el)
        print(f"Предмет: {less}; Кол-во занятий:  {less_sum}")
