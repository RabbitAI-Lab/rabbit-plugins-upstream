# -*- coding: utf-8 -*-
"""akshare 多接口可用性诊断"""
import akshare as ak
import time

tests = [
    ('stock_zh_a_spot',       lambda: ak.stock_zh_a_spot()),
    ('fund_etf_spot_em',      lambda: ak.fund_etf_spot_em()),
    ('stock_hk_hist',         lambda: ak.stock_hk_hist(symbol='00700', period='daily', adjust='qfq')),
    ('stock_us_daily',        lambda: ak.stock_us_daily(symbol='105.NVDA', adjust='qfq')),
    ('futures_zh_daily_sina', lambda: ak.futures_zh_daily_sina(symbol='CU0')),
    ('stock_billboard_baidu', lambda: ak.stock_lhb_detail_em(start_date='20260623', end_date='20260629')),
]

for name, fn in tests:
    t0 = time.time()
    try:
        df = fn()
        dt = time.time() - t0
        rows = len(df) if hasattr(df, '__len__') else '?'
        print(f'{name:<26} OK    rows={rows}  用时={dt:.1f}s')
    except Exception as e:
        dt = time.time() - t0
        msg = str(e)[:100]
        print(f'{name:<26} FAIL  用时={dt:.1f}s  err={type(e).__name__}: {msg}')