a = int(input("Введите номер месяца от 1 до 12: "))

year = "зима весна лето осень"
year = list(year.split())

# длинно, но оригинально, можно через цикл и математику через целочисленное деление
b = 1
if a is b:
    print(year[0])
b = 2
if a is b:
    print(year[0])
b = 12
if a is b:
    print(year[0])
b = 3
if a is b:
    print(year[1])
b = 4
if a is b:
    print(year[1])
b = 5
if a is b:
    print(year[1])
b = 6
if a is b:
    print(year[2])
b = 7
if a is b:
    print(year[2])
b = 8
if a is b:
    print(year[2])
b = 9
if a is b:
    print(year[3])
b = 10
if a is b:
    print(year[3])
b = 11
if a is b:
    print(year[3])
b = 12
if a is b:
    print(year[0])

# второй вариант
my_year = {1: "зима", 2: "зима", 12: "зима",
           3: "весна", 4: "весна", 5: "весна",
           6: "лето", 7: "лето", 8: "лето",
           9: "осень", 10: "осень", 11: "осень"}

print(my_year.get(a))







