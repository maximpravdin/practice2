# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

import json

res = dict()
aver_profit = 0
num = 0
with open("../examples5/text_7.txt", encoding="utf-8") as f:
    for line in f:
        name, type, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            aver_profit += profit
            num += 1
        res[name] = profit
aver_profit /= num
with open("json7.json", "w", encoding="utf-8") as f:
    json.dump([res, {"average_profit": aver_profit}], f, ensure_ascii=False)  # РґР»СЏ РєРёСЂРёР»Р»РёС†С‹
