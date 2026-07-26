"""测速：青岛啤酒 600600 各环节耗时"""
import sys; sys.path.insert(0, '.')
from ghdata import config, db_manager as db
import requests, time

code = '600600'
print('=== 各环节耗时 ===')

# WebAPI 连通性
t0 = time.time()
try:
    r = requests.get(config.WEBAPI_BASE_URL + '/klineanalyze/teaser', 
                     json={"code": code}, timeout=10)
    print(f'teaser 连通: HTTP {r.status_code} ({r.elapsed.total_seconds():.2f}s)')
except Exception as e:
    print(f'teaser 不可达: {e}')

# kline_analyze 耗时
t0 = time.time()
r = db.kline_analyze(code)
t1 = time.time()
print(f'kline_analyze({code}): {t1-t0:.3f}s')
print(f'  preview={r.get("preview")}')
print(f'  _error_info={r.get("_error_info")}')
print(f'  _payment_url 存在={"_payment_url" in r}')

# 模拟 17维并行采集（只测调用不真正跑全量）
print()
print('=== 模拟并行采集串行版耗时（8路并行→~2s）===')
t0 = time.time()
from ghdata import data_fetcher as fetcher
# 只测2个典型接口看单次耗时
t2 = time.time()
r1 = fetcher.fetch_realtime(code)
print(f'  fetch_realtime: {time.time()-t2:.2f}s')
t2 = time.time()
r2 = fetcher.fetch_kline(code, 60)
print(f'  fetch_kline(60d): {time.time()-t2:.2f}s')
print(f'  合计: {time.time()-t0:.2f}s (17路并行预计~2s)')
