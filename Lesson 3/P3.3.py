# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.#

def my_func(var_1,var_2,var_3):
    a = (var_1,var_2,var_3)
    result = sum(a) - min(a)
    return result

v_1 = float(input("Введите 1ое число: "))
v_2 = float(input("Введите 2ое число: "))
v_3 = float(input("Введите 3ье число: "))

print(my_func(v_1, v_2, v_3))
