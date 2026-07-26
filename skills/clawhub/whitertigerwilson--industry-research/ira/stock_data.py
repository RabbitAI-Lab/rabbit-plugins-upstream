"""
stock_data.py - 主营筛选 / 商品-股票映射查询
"""

from __future__ import annotations
import pandas as pd
from typing import Optional

from .constants import KNOWN_MAP, find_commodity
from .api_client import eastmoney_get, tencent_get


def filter_stocks(keyword: str) -> pd.DataFrame:
    """
    按商品关键字查找 A 股相关上市公司。

    Returns:
        DataFrame: [公司名称, 股票代码, 主营收入占比, 毛利润占比, 产能/储量]
    """
    stocks = find_commodity(keyword)
    if not stocks:
        return pd.DataFrame(columns=["公司名称", "股票代码", "主营收入占比", "毛利润占比", "产能/储量"])

    df = pd.DataFrame(stocks, columns=["公司名称", "股票代码", "主营收入占比", "毛利润占比", "产能/储量"])
    return df


def search_industry_concept(keyword: str) -> pd.DataFrame:
    """
    通过东方财富的板块接口查询行业成分股。
    作为预定义池的兜底（处理未覆盖商品）。
    """
    url = (
        "https://push2.eastmoney.com/api/qt/clist/get"
        "?pn=1&pz=20&po=1&np=1&fltt=2&invt=2"
        f"&fid=f3&fields=f12,f14,f3,f62"
        f"&fs=m:90+t:2+f:!50"
    )
    j = eastmoney_get(url)
    if not j or not j.get("data") or not j["data"].get("diff"):
        return pd.DataFrame()

    rows = []
    for s in j["data"]["diff"]:
        name = s.get("f14", "")
        if keyword in name:
            rows.append({
                "公司名称": name,
                "股票代码": s.get("f12", ""),
                "涨跌幅": s.get("f3", 0),
                "净流入(万)": s.get("f62", 0),
            })
    return pd.DataFrame(rows)


def get_realtime(code: str) -> dict | None:
    """获取个股实时价格（腾讯 + 东方财富双源）"""
    # 腾讯优先（轻量、稳）
    tk = tencent_get(code)
    if tk and tk.get("price"):
        return {
            "name": tk.get("name"),
            "code": code,
            "price": tk.get("price"),
            "yesterday": tk.get("yesterday"),
            "change_pct": tk.get("change_pct"),
            "high": tk.get("high"),
            "low": tk.get("low"),
            "turnover_pct": tk.get("turnover_pct"),
            "pe_ttm": tk.get("pe"),
            "timestamp": tk.get("timestamp"),
            "source": "tencent",
        }
    return None
