reveneu = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержек: "))

profit = reveneu - cost
if profit >= 0:
    print("Прибыль = ", profit)
    margin = profit / reveneu
    print("Рентабельность выручки = ", "%.2f" %(margin))
    staff = int(input("Введите кол-во персонала: "))
    profit_for_staff = profit / staff
    print("Прибыль на одного сотрудника = ", "%.2f" % (profit_for_staff))
else:
    print("Убыток = ", profit)




