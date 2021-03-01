# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


# я перемудрил: создал свой словарь, из файла второй cловарь, поменял ключи одного на ключи другого в 3ьем словаре,
# а потом в файл записал
my_f2 = open("Eng2.txt", "w", encoding="utf-8")

dictionary = {'один':1, 'два':2, 'три':3, 'четыре':4}
dict_1 = {}
with open("Eng1.txt", encoding="utf-8") as my_f1:
    my_f1 = list(my_f1)
    for line in my_f1:
        a = line.split()
        dict_1.update({a[0]:[a[1],a[2]]})
dict_2 = {}
k = list(dictionary.keys())
v = list(dict_1.values())

j = 0
while j < len(k):
    dict_2.update({k[j]: v[j]})
    j = j + 1

for key in dict_2:
   print(f'{key},{dict_2[key]}', file=my_f2)

my_f2.close()