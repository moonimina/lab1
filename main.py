from sortings import merge, merge_sort, bubble, shaker
from overloading import Products
from generator import gen
import pandas as pd
import time
import copy

t_bubble = []
t_shaker = []
t_merge = []

n_ = [100, 500, 1000, 5000, 10000, 50000, 100000]

# создание таблицы с наборами данных объемами от 100 до 100000
with pd.ExcelWriter("./export1.xlsx") as wr:
    for i in n_:
        pd.DataFrame(gen(i)).to_excel(wr, sheet_name=f'n={i}', index=False)

products = {}
for j in n_:
    d = pd.read_excel('./export1.xlsx', sheet_name=f'n={j}').to_dict('records')
    d_products = []
    for product in d:
        d_products.append(Products(
            product['Наименование'], product['Страна'], product['Oбъем'], product['Сумма']))
    products[j] = d_products

for l in n_:
    srtd_bubble = copy.deepcopy(products[l])
    time_start = time.time()
    bubble(srtd_bubble)
    time_end = time.time() - time_start
    t_bubble.append(time_end)

    dict__ = {}
    prod_name = []
    country = []
    volume = []
    summa = []
    for k in srtd_bubble:
        prod_name.append(k.prod_name)
        country.append(k.country)
        volume.append(k.volume)
        summa.append(k.summa)
    dict__['Наименование'] = prod_name
    dict__['Страна'] = country
    dict__['Oбъем'] = volume
    dict__['Сумма'] = summa

    if l == 100:
        md = 'w'
    else:
        md = 'a'
    with pd.ExcelWriter("./sorted_bubl.xlsx", mode=md, engine="openpyxl") as wr:
        pd.DataFrame(dict__).to_excel(wr, index=False, sheet_name=f'n={l}')

for l in n_:
    srtd_shaker = copy.deepcopy(products[l])
    time_start = time.time()
    shaker(srtd_shaker)
    time_end = time.time() - time_start
    t_shaker.append(time_end)

    dict__ = {}
    prod_name = []
    country = []
    volume = []
    summa = []
    for k in srtd_shaker:
        prod_name.append(k.prod_name)
        country.append(k.country)
        volume.append(k.volume)
        summa.append(k.summa)
    dict__['Наименование'] = prod_name
    dict__['Страна'] = country
    dict__['Oбъем'] = volume
    dict__['Сумма'] = summa

    if l == 100:
        md = 'w'
    else:
        md = 'a'
    with pd.ExcelWriter("./sorted_shaker.xlsx", mode=md, engine="openpyxl") as wr:
        pd.DataFrame(dict__).to_excel(wr, index=False, sheet_name=f'n={l}')

for l in n_:
    srtd_merge = copy.deepcopy(products[l])
    time_start = time.time()
    merge_sort(srtd_merge, 0, len(srtd_merge)-1)
    time_end = time.time() - time_start
    t_merge.append(time_end)

    dict__ = {}
    prod_name = []
    country = []
    volume = []
    summa = []
    for k in srtd_merge:
        prod_name.append(k.prod_name)
        country.append(k.country)
        volume.append(k.volume)
        summa.append(k.summa)
    dict__['Наименование'] = prod_name
    dict__['Страна'] = country
    dict__['Oбъем'] = volume
    dict__['Сумма'] = summa

    if l == 100:
        md = 'w'
    else:
        md = 'a'
    with pd.ExcelWriter("./sorted_merge.xlsx", mode=md, engine="openpyxl") as wr:
        pd.DataFrame(dict__).to_excel(wr, index=False, sheet_name=f'n={l}')

print('Сортировка пузырьком заняла', t_bubble, 'секунд')
print('Сортировка шейкером заняла', t_shaker, 'секунд')
print('Сортировка слиянием заняла', t_merge, 'секунд')