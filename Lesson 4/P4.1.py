# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, work_in_hours, payment_per_hour, bonus = argv


print("Имя скрипта: ", script_name)
print("Выработка в часах: ", work_in_hours)
print("Ставка в час: ", payment_per_hour)
print("Премия: ", bonus)
print("Заработная плата:", float(work_in_hours) * float(payment_per_hour) + float(bonus))

