def first_func():
    try:
        var_1 = float(input("Введите 1ое число: "))
        var_2 = float(input("Введите 2ое число: "))
        return var_1 / var_2
    except ZeroDivisionError:
        print("Деление на ноль, Ошибка")

print(first_func())
