# -*- coding: utf-8 -*-
"""验证腾讯实时换手率字段"""
import requests

r = requests.get('http://qt.gtimg.cn/q=sh601899',
                headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
text = r.text.strip()
payload = text.split('="', 1)[1].rstrip('";')
fields = payload.split('~')

# 打印含数字的字段（换手率/PE 应该是小数）
print('含数字的字段（疑似换手率/PE/涨跌）:')
for i in [38, 39, 40, 41, 32, 33]:
    if i < len(fields):
        print(f'  [{i}] = {fields[i]!r}')