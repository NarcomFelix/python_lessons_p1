# Создать список
result_list = []

# Наполнить его елементами.
result_list.append(1)
result_list.append(None)
result_list.append(True)
result_list.append('text')
result_list.append(45)
result_list.extend([65.3])
print(result_list)

# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
for el in result_list:
    print(type(el))

# К вопросу о ТЗ (до этого всё было явно и определено):
# "Элементы списка можно не запрашивать у пользователя, а указать явно, в программе"
#  Это к обратной связи. Тут можно понимать задание: добавлять по одному, добавить несколько элементов, создать список и "приравнять"