# -*- coding: utf-8 -*-
"""验证腾讯日K + akshare spot 字段"""
import requests, json

# 腾讯日K
hdrs = {'User-Agent': 'Mozilla/5.0'}
url = 'http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sh601899,day,,,60,qfq'
r = requests.get(url, headers=hdrs, timeout=10)
j = r.json()
data = j.get('data', {}).get('sh601899', {})
qfqday = data.get('qfqday', [])
print(f'qfqday 条数: {len(qfqday)}')
print('最后 3 条:')
for row in qfqday[-3:]:
    print(' ', row)
print('字段含义: [日期, 开, 收, 高, 低, 成交量(手?), ?]')

# 试试加上 volume 字段（不带 qfq）
url2 = 'http://web.ifzq.gtimg.cn/appstock/app/kline/kline?param=sh601899,day,,,60'
r2 = requests.get(url2, headers=hdrs, timeout=10)
j2 = r2.json()
data2 = j2.get('data', {}).get('sh601899', {})
print('\nkline 接口 keys:', list(data2.keys())[:10])
if 'day' in data2:
    print('day 最后 2 条:', data2['day'][-2:])

# akshare spot 看字段
import akshare as ak
spot = ak.stock_zh_a_spot()
print('\nspot 总条数:', len(spot))
print('spot 列名:', list(spot.columns))
row = spot[spot['代码'] == '601899']
if len(row) > 0:
    print('紫金 spot 字段:')
    for k, v in row.iloc[0].to_dict().items():
        print(f'  {k}: {v}')