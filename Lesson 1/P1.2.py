a = int(input("Введите кол-во секунд:"))
# вводим переменные секунд, минут и часов, и присваиваем им нулевые значения
s = 0
m = 0
h = 0
if a / 3600 > 0:
    h = a // 3600
    a = a - s*3600
    if a / 60 > 0:
        m = a // 60
        a = a - m*60
        s = a
print("%-2s %-2s %-2s %-2s %-2s" % (h, ":", m, ":", s)) # не знал как форматирование применить, вот такой способ нашёл