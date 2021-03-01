# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


from random import randint
my_list = [randint(-10, 10) for i in range(10)]

new_list = [i for i in my_list if my_list.count(i) == 1]
#print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
