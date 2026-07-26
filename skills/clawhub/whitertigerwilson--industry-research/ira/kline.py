"""
kline.py - K线形态检测 + 均线排列分析
"""

from __future__ import annotations
from typing import Optional

from .api_client import market_prefix
from .sources import fetch_klines as _multi_fetch_klines


def _fetch_klines(code: str, days: int) -> list[str]:
    """K线获取（多源 fallback：东财 → 腾讯 → akshare）"""
    fetch_days = max(days, 25)  # MA20 需要至少 20 根 K 线
    return _multi_fetch_klines(code, fetch_days, klt=101, fqt=1)


def _ma(prices: list[float], period: int) -> Optional[float]:
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


def detect_patterns(klines: list[str]) -> list[tuple]:
    """
    检测常见 K 线形态。
    Returns: [(日期, 收盘价, 形态名, 含义, 信号), ...]
    """
    results = []
    for i in range(1, len(klines)):
        p = klines[i - 1].split(",")
        c = klines[i].split(",")

        d = c[0]
        o = float(c[1])
        close = float(c[2])
        h = float(c[3])
        l = float(c[4])
        v = float(c[5])

        po = float(p[1])
        pc_close = float(p[2])
        pv = float(p[5])

        is_bull = close > o
        body = abs(close - o)
        upper_shadow = h - max(o, close)
        lower_shadow = min(o, close) - l
        full_range = h - l
        body_ratio = body / full_range if full_range > 0 else 0

        signals = []

        # 锤子线（底部）
        if is_bull and lower_shadow > body * 2.5 and upper_shadow < body * 0.2:
            signals.append(("锤子线（底部）", "支撑有效，可能反弹", "WE"))

        # 吊颈线（顶部）
        if not is_bull and lower_shadow > body * 2.5 and upper_shadow < body * 0.2:
            signals.append(("吊颈线（顶部）", "上攻乏力，可能回落", "BE"))

        # 射击之星
        if upper_shadow > body * 2.0 and lower_shadow < body * 0.3 and body_ratio < 0.3:
            if is_bull:
                signals.append(("射击之星（底部反转）", "可能见底回升", "WE"))
            else:
                signals.append(("射击之星（顶部射击）", "可能见顶回落", "BE"))

        # 吞没形态
        body_prev = abs(pc_close - po)
        if is_bull and pc_close < po and close > po and o < pc_close and body > body_prev * 1.1:
            signals.append(("阳包阴（看涨吞没）", "底部反转信号", "WE"))
        if not is_bull and pc_close > po and close < po and o > pc_close and body > body_prev * 1.1:
            signals.append(("阴包阳（看跌吞没）", "顶部反转信号", "BE"))

        # 乌云盖顶
        if pc_close > po and o > pc_close and close < (o + pc_close) / 2:
            penetration = (o - close) / full_range if full_range > 0 else 0
            if penetration > 0.4:
                signals.append(("乌云盖顶", "顶部反转信号", "BE"))

        # 大阳/大阴线放量
        if is_bull and body_ratio > 0.75 and v > pv * 1.5:
            signals.append(("大阳线（放量）", "多头强势，可能延续", "WE"))
        if not is_bull and body_ratio > 0.75 and v > pv * 1.5:
            signals.append(("大阴线（放量）", "空头强势，可能延续", "BE"))

        # 三日早晨/黄昏星
        if i >= 2:
            pp = klines[i - 2].split(",")
            ppo, ppc = float(pp[1]), float(pp[2])
            middle_body = abs(float(c[1]) - float(c[2]))
            if ppc < ppo and middle_body < body * 0.5 and close > o and close > (ppo + ppc) / 2:
                signals.append(("早晨之星（底部反转）", "三日内底部形态", "WE"))
            if ppc > ppo and middle_body < body * 0.5 and close < o and close < (ppo + ppc) / 2:
                signals.append(("黄昏之星（顶部反转）", "三日内顶部形态", "BE"))

        for name, meaning, sig in signals:
            results.append((d, close, name, meaning, sig))

    return results


def judge_arrangement(klines: list[str]) -> tuple:
    """均线排列判定 (MA5/MA10/MA20)"""
    prices = [float(k.split(",")[2]) for k in klines]
    ma5 = _ma(prices, 5)
    ma10 = _ma(prices, 10)
    ma20 = _ma(prices, 20)

    if None in (ma5, ma10, ma20):
        latest = prices[-1] if prices else 0
        return "数据不足", "无法判断", 0, 0, 0, latest

    latest = prices[-1]
    if ma5 > ma10 > ma20 and latest > ma5:
        arr = "多头排列"
        trend = "上升趋势"
    elif ma5 < ma10 < ma20 and latest < ma5:
        arr = "空头排列"
        trend = "下降趋势"
    else:
        arr = "震荡/混合"
        trend = "趋势不明"

    return arr, trend, round(ma5, 2), round(ma10, 2), round(ma20, 2), round(latest, 2)


def analyze(code: str, days: int = 15) -> dict:
    """完整技术面分析"""
    klines = _fetch_klines(code, days)

    arr, trend, ma5, ma10, ma20, latest = judge_arrangement(klines)
    patterns = detect_patterns(klines)

    bullish = [p for p in patterns if p[4] == "WE"]
    bearish = [p for p in patterns if p[4] == "BE"]

    return {
        "code": code,
        "klines_count": len(klines),
        "arrangement": arr,
        "trend": trend,
        "ma5": ma5,
        "ma10": ma10,
        "ma20": ma20,
        "price": latest,
        "patterns": patterns,
        "pattern_count": len(patterns),
        "bullish_count": len(bullish),
        "bearish_count": len(bearish),
    }


def print_report(result: dict):
    code = result["code"]
    print(f"\n{'=' * 55}")
    print(f"  股票: {code}  |  近{result['klines_count']}日数据")
    print(f"{'=' * 55}")
    print(f"  均线排列: {result['arrangement']}")
    print(f"  MA5={result['ma5']}  MA10={result['ma10']}  MA20={result['ma20']}  |  收盘={result['price']}")
    print(f"  趋势判断: {result['trend']}")
    print()
    patterns = result["patterns"]
    print(f"--- K线形态（共检测到{len(patterns)}个信号）---")
    if not patterns:
        print("  未检测到明显形态")
    else:
        print(f"  看多: {result['bullish_count']}个  |  看空: {result['bearish_count']}个")
        for d, close, name, meaning, sig in patterns:
            sig_str = "[WE]" if sig == "WE" else "[BE]"
            print(f"  {d} {sig_str} {name} — 收盘{close:.2f} | {meaning}")
    print(f"{'=' * 55}\n")
