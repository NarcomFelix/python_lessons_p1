a = int(input("Введите кол-во км в первый день: "))
b = int(input("Введите кол-во км, которое нужно достичь: "))
i = 1
while a <= b:
    a = a + a * 0.1
    i = i + 1

else:
    print("Кол-во дней для достиженения результата:", i)



