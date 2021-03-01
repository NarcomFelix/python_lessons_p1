# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, divisible, divided):
        self.divisible = divisible
        self.divided = divided

    @staticmethod
    def divide_by_null(divisible, divided):
        try:
            return round(divisible / divided, 2)
        except:
            return f"Деление на ноль не допустимо"


print(OwnError.divide_by_null(10,0))
print(OwnError.divide_by_null(10,3))



