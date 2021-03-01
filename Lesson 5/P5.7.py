# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

with open('5.7.json', 'w') as fj:
    with open('5.7.txt', encoding='utf-8') as f:
        # profit ={line.split()[0]: int(line.split()[2])-int(line.split()[3]) for line in f}
        # result =[profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
        #                                           len([int(i) for i in profit.values() if int(i) > 0]))}
        result = {}
        profit = {}
        sum_profit = 0
        n = 0
        for line in f:
            a = line.split()

            if (int(a[2]) - int(a[3])) > 0:
                c = int(a[2]) - int(a[3])
                profit.update({a[0]:c})
                sum_profit = sum_profit + c
                n = n + 1
        av_profit = sum_profit / n
        print(profit)
        profit.update({'average_profit': av_profit})
        result = profit
    json.dump(result, fj, ensure_ascii=False, indent=4)