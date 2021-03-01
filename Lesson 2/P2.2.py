result_list = []

result_list.append(int(input("Введите целое число:")))
result_list.append(bool(input("Введите символы:")))
result_list.append(input('Введите любое слово:'))
result_list.append(int(input("Введите целое число:")))
result_list.append(float(input("Введите дробное число:")))
print("Начальный список: ", result_list)

for i in range(1,len(result_list), 2):
    result_list[i-1], result_list[i] = result_list[i], result_list[i-1]

print("Изменённый список: ", result_list)
