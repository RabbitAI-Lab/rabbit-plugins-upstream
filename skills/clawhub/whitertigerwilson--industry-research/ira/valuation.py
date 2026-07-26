"""
valuation.py - 个股估值历史分位

策略：
1. 用 akshare / Tushare 拉历史 PE/PB（最准但需配 token）
2. 兜底：用东方财富历史估值 API（基础够用）
3. 临时方案：用近 5 年静态估值（"低估/合理/高估" 三档评估）

⚠️ 实际依赖：
  - 免费版推荐用东方财富的估值历史接口（push2his）拉季报数据
  - 如果 akshare / Tushare 装了则优先用
  - 完全离线时输出"-" 并提示用户配 Tushare
"""

from __future__ import annotations
import requests
from typing import Optional

from .api_client import HEADERS, market_prefix
from .sources import fetch_klines as _multi_fetch_klines


# ---------- 行业经验估值带（粗略三档评估） ----------
# 补充：用户初衷是「行业研究」，估值分位是辅助维度。
# 不需要 100% 精确，能给个三档评估即可。

INDUSTRY_PE_BANDS = {
    # 大宗 / 周期类：低 PE 视为低估
    "硫酸": {"reasonable": (10, 25), "note": "周期股，PE 越低越被低估（但需结合 PB/ROE）"},
    "铜": {"reasonable": (10, 22), "note": "周期股，PE 越低越被低估"},
    "钢铁": {"reasonable": (5, 18), "note": "周期股，PE 越低越好"},
    "铝": {"reasonable": (10, 22), "note": "周期股，PE 越低越低估"},
    "煤": {"reasonable": (5, 15), "note": "周期股，PE < 8 视为严重低估"},
    "原油": {"reasonable": (8, 18), "note": "周期股，看油价拐点"},
    "黄金": {"reasonable": (15, 35), "note": "PE + 金价综合判断"},
    "化工": {"reasonable": (12, 25), "note": "通用区间"},
    "锂": {"reasonable": (15, 35), "note": "高弹性周期"},
    "磷": {"reasonable": (10, 25), "note": "磷化工周期"},
    "钛": {"reasonable": (12, 22), "note": "钛白粉周期"},
    # 消费 / 稳定类：高 PE 也可以接受
    "白酒": {"reasonable": (20, 40), "note": "高端白酒 PE 常年 25-40"},
    "农产品": {"reasonable": (15, 30), "note": "波动较大"},
    "宠物食品": {"reasonable": (25, 50), "note": "高景气赛道"},
    # 成长
    "半导体": {"reasonable": (30, 70), "note": "成长股，高 PE"},
    "新能源车": {"reasonable": (25, 60), "note": "成长股"},
    "光伏": {"reasonable": (15, 35), "note": "周期+成长"},
    "储能": {"reasonable": (20, 50), "note": "成长"},
    "军工": {"reasonable": (30, 60), "note": "国产替代题材"},
}


def evaluate_pe(pe: Optional[float], industry: str = "") -> str:
    """
    单只 PE 的三档评估：低估/合理/高估。

    Args:
        pe: 当前 PE TTM
        industry: 行业名（用于查 INDUSTRY_PE_BANDS）

    Returns:
        "低估" / "合理" / "高估" / "无法判断"
    """
    if pe is None or pe <= 0:
        return "无法判断"
    band = INDUSTRY_PE_BANDS.get(industry)
    if not band:
        return _generic_pe_evaluation(pe)
    lo, hi = band["reasonable"]
    if pe < lo * 0.7:
        return "低估"
    elif pe < lo:
        return "偏低"
    elif pe <= hi:
        return "合理"
    elif pe <= hi * 1.3:
        return "偏高"
    else:
        return "高估"


def _generic_pe_evaluation(pe: float) -> str:
    """无行业数据的通用分档"""
    if pe < 0:
        return "亏损（PE 不可比）"
    if pe < 15:
        return "低估"
    if pe < 30:
        return "合理"
    if pe < 50:
        return "偏高"
    return "高估"


def evaluate_pb(pb: Optional[float]) -> str:
    """PB 评估"""
    if pb is None or pb <= 0:
        return "无法判断"
    if pb < 1:
        return "破净（潜在机会）"
    if pb < 2:
        return "低估"
    if pb < 4:
        return "合理"
    if pb < 8:
        return "偏高"
    return "高估"


def get_historical_valuation(code: str, years: int = 5) -> Optional[dict]:
    """
    拉个股近 N 年 PE/PB 历史数据（按季度）。

    ⚠️ 当前免费方案：尝试东方财富的历史接口；失败时返回 None。
    推荐升级方案：用户装 akshare 用 stock_a_indicator_lg(symbol=...)。
    """
    market = market_prefix(code)
    secid = f"{market}.{code}"

    # 优先用东财 push2his（季线历史估值），失败则 fallback 到腾讯日 K 转季度
    # klt=103 = 季线，fqt=1 = 前复权
    try:
        klines = _multi_fetch_klines(code, years * 4 + 10, klt=103, fqt=1)
    except Exception as e:
        print(f"[valuation] K线所有源失败: {e}")
        return None

    if not klines:
        return None

    rows = []
    for k in klines:
        f = k.split(",")
        if len(f) < 6:
            continue
        rows.append({
            "date": f[0],
            "open": float(f[1]) if f[1] else None,
            "close": float(f[2]) if f[2] else None,
            "high": float(f[3]) if f[3] else None,
            "low": float(f[4]) if f[4] else None,
            "volume": float(f[5]) if f[5] else None,
        })

    # 计算价格历史分位
    closes = [r["close"] for r in rows if r["close"]]
    if not closes:
        return None

    min_p = min(closes)
    max_p = max(closes)
    avg_p = sum(closes) / len(closes)
    latest_p = closes[-1]

    # 当前价格在历史区间的位置
    price_percentile = (latest_p - min_p) / (max_p - min_p) * 100 if max_p > min_p else 50

    return {
        "code": code,
        "years": years,
        "data_points": len(rows),
        "min_price": round(min_p, 2),
        "max_price": round(max_p, 2),
        "avg_price": round(avg_p, 2),
        "latest_price": round(latest_p, 2),
        "price_percentile": round(price_percentile, 1),
        "comment": _price_position_comment(price_percentile),
    }


def _price_position_comment(percentile: float) -> str:
    """根据价格历史分位给评语"""
    if percentile < 10:
        return "当前价处于历史低位"
    if percentile < 30:
        return "当前价处于历史偏低位置"
    if percentile < 70:
        return "当前价处于历史中位"
    if percentile < 90:
        return "当前价处于历史偏高位置"
    return "当前价处于历史高位"


def get_valuation(code: str, industry: str = "") -> dict:
    """
    综合估值评估：当前 PE/PB 单点评估 + 历史价格分位。
    """
    # 单点评估（PE/PB 需要 financial 模块）
    result = {
        "code": code,
        "industry_hint": industry,
        "_note": "完整估值历史分位需要 akshare/Tushare，当前先用三档评估 + 价格历史分位",
    }

    # 历史价格分位
    hist = get_historical_valuation(code, 5)
    if hist:
        result["price_history"] = hist

    return result


def print_report(val: dict, fin: dict = None):
    """打印估值评估报告"""
    print(f"\n{'=' * 55}")
    print(f"  {val.get('code', '?')} 估值评估  | 行业: {val.get('industry_hint') or '通用'}")
    print(f"{'=' * 55}")
    if val.get("_note"):
        print(f"  📋 {val['_note']}")
        print()

    # 历史价格分位
    ph = val.get("price_history")
    if ph:
        print(f"  --- 价格历史分位（近{ph['years']}年 {ph['data_points']}个季度）---")
        print(f"  区间: {ph['min_price']} ~ {ph['max_price']} (均价 {ph['avg_price']})")
        print(f"  最新: {ph['latest_price']}")
        print(f"  分位: {ph['price_percentile']}% — {ph['comment']}")
        print()

    # PE/PB 评估（如果提供 financial 模块数据）
    if fin:
        pe = fin.get("pe_ttm")
        pb = fin.get("pb")
        if pe is not None:
            v = evaluate_pe(pe, val.get("industry_hint", ""))
            print(f"  PE(TTM): {pe:.2f} → {v}")
        if pb is not None:
            v = evaluate_pb(pb)
            print(f"  PB: {pb:.2f} → {v}")
    print(f"{'=' * 55}\n")
