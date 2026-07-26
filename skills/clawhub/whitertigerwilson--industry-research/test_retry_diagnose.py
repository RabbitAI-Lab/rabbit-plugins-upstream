# -*- coding: utf-8 -*-
"""诊断脚本：东财接口重试 vs 不重试对比"""
import sys, time
sys.path.insert(0, '.')
import requests
from ira.api_client import eastmoney_get, HEADERS

URL = (
    'https://push2his.eastmoney.com/api/qt/stock/kline/get'
    '?secid=1.601899&fields1=f1,f2,f3,f4,f5,f6'
    '&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'
    '&lmt=60&klt=101&fqt=1&end=20500101'
)

print('=== A. 单次裸 requests.get（不重试）===')
t0 = time.time()
try:
    r = requests.get(URL, headers=HEADERS, timeout=10)
    j = r.json()
    k = j.get('data', {}).get('klines', [])
    print(f'  HTTP={r.status_code}  data行数={len(k)}  用时={time.time()-t0:.2f}s')
except Exception as e:
    print(f'  FAIL  用时={time.time()-t0:.2f}s  err={type(e).__name__}: {str(e)[:120]}')

print()
print('=== B. eastmoney_get 带重试（4次指数退避）===')
t0 = time.time()
result = eastmoney_get(URL)
dt = time.time() - t0
if result:
    k = result.get('data', {}).get('klines', [])
    print(f'  OK  data行数={len(k)}  总用时={dt:.1f}s')
else:
    print(f'  FAIL  总用时={dt:.1f}s')

print()
print('=== C. 手动重试 3 次（裸 get）===')
t0 = time.time()
last = None
for i in range(3):
    try:
        r = requests.get(URL, headers=HEADERS, timeout=10)
        j = r.json()
        if j.get('data'):
            k = j['data'].get('klines', [])
            print(f'  第{i+1}次成功  data行数={len(k)}  总用时={time.time()-t0:.1f}s')
            break
    except Exception as e:
        last = e
        print(f'  第{i+1}次失败: {type(e).__name__}: {str(e)[:80]}')
        time.sleep(1.0 * (2 ** i))
else:
    print(f'  3次都失败  最终错误: {last}')