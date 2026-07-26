# -*- coding: utf-8 -*-
"""查腾讯实时字段"""
import requests

r = requests.get('http://qt.gtimg.cn/q=sh601899',
                headers={'User-Agent': 'Mozilla/5.0'}, timeout=8)
text = r.text
payload = text.split('="', 1)[1].rstrip('";')
fields = payload.split('~')
print(f'总字段数: {len(fields)}')

# 字段索引参考
labels = [
    '0:未知', '1:名称', '2:代码', '3:现价', '4:昨收', '5:今开',
    '6:成交量(手)', '7:外盘', '8:内盘', '9:买一价', '10:买一量',
    '19:卖一价', '29:日期', '30:时间', '31:?', '32:涨跌额',
    '33:涨跌幅', '34:最高', '35:最低', '36:?', '37:成交量(手)',
    '38:成交额(元)', '39:换手率', '40:PE', '41:?', '42:最高(复权?)',
    '43:最低(复权?)', '44:振幅', '45:流通市值(亿)', '46:总市值(亿)',
    '47:PB', '48:涨停价', '49:跌停价', '50:每股净资产', '51:?'
]
for i in range(min(len(fields), 52)):
    print(f'[{i:2}] {labels[i] if i < len(labels) else "?"} = {fields[i]!r}')