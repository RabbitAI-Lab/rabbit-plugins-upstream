"""
financial.py - 个股财务数据（PE/PB/市值/ROE/EPS）

主数据源：腾讯行情 hq.sinajs.cn（轻量、稳定、字段多）
辅助：东方财富 push2his（拉更深的财务详情）
"""

from __future__ import annotations
import requests
from typing import Optional

from .api_client import HEADERS, tencent_get, market_prefix


# 腾讯字段位置（按 ~ 切分，0-based）
# 实测验证（紫金 601899）：
#   f[3]=25.79  现价；f[38]=1.57 换手率(%)；f[39]=11.12 PE(动)；
#   f[43]=3.90 PB；f[44]=5313.20 流通市值(亿)；f[45]=6857.75 总市值(亿)
#   f[46]=3.62 流通股本(亿股)；f[74]=19.83 每股净资产
# 茅台 600519：f[43]=5.48 PB；f[44]=14937.98 流股市值；f[45]=14937.98 总市值
TENCENT_FIELDS = {
    "name": 1,
    "code": 2,
    "price": 3,
    "prev_close": 4,
    "open": 5,
    "high": 33,
    "low": 34,
    "change_pct": 32,
    "turnover_pct": 38,
    "pe_ttm": 39,
    "pb": 43,
    "market_cap_float_yi": 44,
    "market_cap_total_yi": 45,
    "float_share_yi": 46,         # 流通股本（亿股）
    # 47-73 是各种主营业务、分红、财务详情，可从东方财富补
    "pb_per_share": 74,            # 每股净资产（元）
}


def _parse_tencent_fields(code: str) -> Optional[dict]:
    """
    直接拿腾讯原始 CSV，按索引精确切。
    """
    market = "sh" if code.startswith("6") or code.startswith("5") else "sz"
    url = f"https://qt.gtimg.cn/q={market}{code}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[financial] tencent 网络失败: {e}")
        return None

    text = r.text.strip()
    if '="' not in text or text.endswith('""'):
        return None
    payload = text.split('="', 1)[1].rstrip('";')
    fields = payload.split("~")
    if len(fields) < 50:
        print(f"[financial] 腾讯字段不足: {len(fields)}")
        return None

    out = {"code": code, "source": "tencent"}
    for name, idx in TENCENT_FIELDS.items():
        try:
            v = fields[idx]
            if v == "" or v == "-":
                out[name] = None
            else:
                out[name] = float(v) if name != "name" and name != "code" else v
        except (IndexError, ValueError):
            out[name] = None
    return out


def _fetch_eastmoney_pe_pb(code: str) -> Optional[dict]:
    """
    东方财富备用：拉一个字段集，重点取 PE_TTM / PB / ROE。
    """
    market = market_prefix(code)
    secid = f"{market}.{code}"
    url = (
        f"https://push2his.eastmoney.com/api/qt/stock/get"
        f"?secid={secid}&fields=f43,f57,f58,f9,f23,f37,f107,f171,f191"
    )
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        j = r.json()
    except Exception as e:
        print(f"[financial] eastmoney 网络失败: {e}")
        return None

    d = j.get("data") or {}
    if not d:
        return None

    # ⚠️ 注意东方财富 f10 接口字段值普遍是实际的 100 倍
    def dec(v):
        try:
            f = float(v)
            return round(f / 100, 2)
        except (TypeError, ValueError):
            return None

    return {
        "source": "eastmoney",
        "name": d.get("f58"),
        "price": dec(d.get("f43")),
        "pe_ttm": dec(d.get("f9")),
        "pb": dec(d.get("f171")),
        "eps_ttm": dec(d.get("f107")),
        "pb_per_share": dec(d.get("f191")),
        "roe_pct": dec(d.get("f37")),
    }


def get_financial(code: str) -> dict:
    """
    综合财务摘要。优先腾讯行情（实时、稳），东方财富补充 ROE 等深度。

    Returns:
      {
        "code", "name", "price", "prev_close",
        "pe_ttm", "pb", "eps_ttm",
        "market_cap_total_yi", "market_cap_float_yi",
        "turnover_pct", "pb_per_share", "roe_pct",
        "high", "low",
        "source": "tencent" | "tencent+eastmoney" | "eastmoney" | "none",
      }
    """
    # 1. 腾讯主源
    tk = _parse_tencent_fields(code)
    if tk and tk.get("price"):
        # 2. 东方财富补 ROE / 每股净资产
        try:
            em = _fetch_eastmoney_pe_pb(code)
            if em:
                # 用东方财富的 ROE / 每股净资产补充
                if em.get("roe_pct") is not None:
                    tk["roe_pct"] = em["roe_pct"]
                if em.get("pb_per_share") is not None:
                    tk["pb_per_share"] = em["pb_per_share"]
                tk["source"] = "tencent+eastmoney"
        except Exception as e:
            print(f"[financial] eastmoney 合并失败: {e}")
        return tk

    # 3. 腾讯兜底失败，单用东方财富
    em = _fetch_eastmoney_pe_pb(code)
    if em and em.get("price"):
        em["code"] = code
        em["market_cap_total_yi"] = None
        em["market_cap_float_yi"] = None
        return em

    return {
        "code": code,
        "source": "none",
        "error": "所有数据源均不可用，请稍后重试",
    }


def print_report(fin: dict):
    """打印财务摘要"""
    print(f"\n{'=' * 55}")
    name = fin.get("name") or fin.get("code", "?")
    print(f"  {name} ({fin.get('code', '?')})  |  数据源: {fin.get('source')}")
    print(f"{'=' * 55}")
    if fin.get("error"):
        print(f"  ⚠ {fin['error']}")
        return

    rows = [
        ("最新价", _fmt_yuan(fin.get("price"))),
        ("昨收", _fmt_yuan(fin.get("prev_close"))),
        ("今开", _fmt_yuan(fin.get("open"))),
        ("最高", _fmt_yuan(fin.get("high"))),
        ("最低", _fmt_yuan(fin.get("low"))),
        ("换手率", _fmt_pct(fin.get("turnover_pct"))),
        ("PE(动)", _fmt_ratio(fin.get("pe_ttm"))),
        ("PB", _fmt_ratio(fin.get("pb"))),
        ("EPS(TTM)", _fmt_yuan(fin.get("eps_ttm"))),
        ("每股净资产", _fmt_yuan(fin.get("pb_per_share"))),
        ("ROE", _fmt_pct(fin.get("roe_pct"))),
        ("总市值", _fmt_yi(fin.get("market_cap_total_yi"))),
        ("流通市值", _fmt_yi(fin.get("market_cap_float_yi"))),
    ]
    for name, val in rows:
        if val is None or val == "—":
            print(f"  {name:<10}  —")
        else:
            print(f"  {name:<10}  {val}")
    print(f"{'=' * 55}\n")


def _fmt_yuan(v):
    if v is None:
        return None
    try:
        return f"{float(v):,.2f} 元"
    except (TypeError, ValueError):
        return None


def _fmt_pct(v):
    if v is None:
        return None
    try:
        return f"{float(v):.2f} %"
    except (TypeError, ValueError):
        return None


def _fmt_ratio(v):
    if v is None:
        return None
    try:
        return f"{float(v):.2f} 倍"
    except (TypeError, ValueError):
        return None


def _fmt_yi(v):
    if v is None:
        return None
    try:
        return f"{float(v):,.2f} 亿元"
    except (TypeError, ValueError):
        return None
