"""
technical.py - 高级技术指标

实现：
- MACD (12, 26, 9)
- RSI (14)
- BOLL (20, 2)
- KDJ (9, 3, 3)
"""

from __future__ import annotations
from typing import Optional
import requests

from .api_client import HEADERS, market_prefix
from .kline import _fetch_klines  # 复用 K 线拉取


# ============ 工具函数 ============

def _closes(klines: list[str]) -> list[float]:
    return [float(k.split(",")[2]) for k in klines if k]


def _ema(values: list[float], period: int) -> list[float]:
    """指数移动平均（EMA）"""
    if not values:
        return []
    k = 2 / (period + 1)
    ema = [values[0]]
    for v in values[1:]:
        ema.append(v * k + ema[-1] * (1 - k))
    return ema


# ============ MACD ============

def calc_macd(klines: list[str], fast: int = 12, slow: int = 26, signal: int = 9) -> dict:
    """
    MACD 指标。
    Returns:
        {"diff": [...], "dea": [...], "macd": [...], "latest": (diff, dea, macd)}
    """
    closes = _closes(klines)
    if len(closes) < slow + signal:
        return {"error": "K线不足"}

    ema_fast = _ema(closes, fast)
    ema_slow = _ema(closes, slow)
    diff = [f - s for f, s in zip(ema_fast, ema_slow)]
    dea = _ema(diff, signal)
    macd = [(d - e) * 2 for d, e in zip(diff, dea)]

    return {
        "diff": diff,
        "dea": dea,
        "macd": macd,
        "latest": (round(diff[-1], 3), round(dea[-1], 3), round(macd[-1], 3)),
    }


def judge_macd(macd_data: dict) -> str:
    """MACD 趋势判断"""
    if macd_data.get("error"):
        return "数据不足"
    diff, dea, macd = macd_data["latest"]
    if diff > 0 and dea > 0:
        if diff > dea:
            return "多头强势（DIF > DEA > 0）"
        return "多头行情（DIF、DEA 均在 0 上方）"
    if diff < 0 and dea < 0:
        if diff < dea:
            return "空头强势（DIF < DEA < 0）"
        return "空头行情（DIF、DEA 均在 0 下方）"
    if diff > 0 > dea:
        return "金叉形成中（DIF 上穿 DEA）"
    if diff < 0 < dea:
        return "死叉形成中（DIF 下穿 DEA）"
    return "震荡"


# ============ RSI ============

def calc_rsi(klines: list[str], period: int = 14) -> dict:
    """
    RSI 指标（相对强弱指标）。
    Returns:
        {"values": [...], "latest": float, "overbought": bool, "oversold": bool}
    """
    closes = _closes(klines)
    if len(closes) <= period:
        return {"error": "K线不足"}

    gains, losses = [], []
    for i in range(1, len(closes)):
        ch = closes[i] - closes[i - 1]
        gains.append(max(ch, 0))
        losses.append(max(-ch, 0))

    rsi = []
    avg_g = sum(gains[:period]) / period
    avg_l = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_g = (avg_g * (period - 1) + gains[i]) / period
        avg_l = (avg_l * (period - 1) + losses[i]) / period
        rs = avg_g / avg_l if avg_l > 0 else 100
        rsi.append(round(100 - 100 / (1 + rs), 2))

    latest = rsi[-1]
    return {
        "values": rsi,
        "latest": latest,
        "overbought": latest > 70,
        "oversold": latest < 30,
    }


def judge_rsi(rsi_data: dict) -> str:
    """RSI 状态判断"""
    if rsi_data.get("error"):
        return "数据不足"
    v = rsi_data["latest"]
    if v >= 80:
        return f"严重超买（RSI {v}）"
    if v >= 70:
        return f"超买（RSI {v}）"
    if v <= 20:
        return f"严重超卖（RSI {v}）"
    if v <= 30:
        return f"超卖（RSI {v}）"
    return f"中性（RSI {v}）"


# ============ BOLL ============

def calc_boll(klines: list[str], period: int = 20, k: float = 2.0) -> dict:
    """
    布林带。
    Returns: {"mid": float, "upper": float, "lower": float, "latest_price": float}
    """
    closes = _closes(klines)
    if len(closes) < period:
        return {"error": "K线不足"}

    recent = closes[-period:]
    mid = sum(recent) / period
    variance = sum((c - mid) ** 2 for c in recent) / period
    std = variance ** 0.5
    upper = mid + k * std
    lower = mid - k * std

    return {
        "mid": round(mid, 2),
        "upper": round(upper, 2),
        "lower": round(lower, 2),
        "latest_price": closes[-1],
    }


def judge_boll(boll_data: dict) -> str:
    """布林带状态判断"""
    if boll_data.get("error"):
        return "数据不足"
    p = boll_data["latest_price"]
    u = boll_data["upper"]
    l = boll_data["lower"]
    if p >= u:
        return f"突破上轨，可能回归（{p:.2f} ≥ {u:.2f}）"
    if p <= l:
        return f"跌破下轨，可能反弹（{p:.2f} ≤ {l:.2f}）"
    if p > boll_data["mid"]:
        return "中轨上方运行"
    return "中轨下方运行"


# ============ KDJ ============

def calc_kdj(klines: list[str], n: int = 9, k_period: int = 3, d_period: int = 3) -> dict:
    """
    KDJ 指标。
    Returns: {"k": float, "d": float, "j": float, "latest_price": float}
    """
    if len(klines) < n:
        return {"error": "K线不足"}

    k_vals, d_vals, j_vals = [], [], []
    prev_k, prev_d = 50.0, 50.0

    for i in range(n - 1, len(klines)):
        window = klines[i - n + 1 : i + 1]
        h = max(float(x.split(",")[3]) for x in window)
        l = min(float(x.split(",")[4]) for x in window)
        c = float(klines[i].split(",")[2])
        rsv = (c - l) / (h - l) * 100 if h > l else 50
        k = (prev_k * (k_period - 1) + rsv) / k_period
        d = (prev_d * (d_period - 1) + k) / d_period
        j = 3 * k - 2 * d
        k_vals.append(round(k, 2))
        d_vals.append(round(d, 2))
        j_vals.append(round(j, 2))
        prev_k, prev_d = k, d

    return {
        "k": k_vals[-1],
        "d": d_vals[-1],
        "j": j_vals[-1],
        "latest_price": _closes(klines)[-1],
    }


def judge_kdj(kdj_data: dict) -> str:
    """KDJ 状态判断"""
    if kdj_data.get("error"):
        return "数据不足"
    k, d, j = kdj_data["k"], kdj_data["d"], kdj_data["j"]
    if j < 0:
        return f"严重超卖（J={j}, K={k}, D={d}）"
    if j > 100:
        return f"严重超买（J={j}, K={k}, D={d}）"
    if k > d and k < 50:
        return f"金叉（K={k} 上穿 D={d}）"
    if k < d and k > 50:
        return f"死叉（K={k} 下穿 D={d}）"
    if k > d:
        return f"K 高于 D（多头偏强）"
    return f"K 低于 D（空头偏强）"


# ============ 整合 ============

def analyze(code: str, days: int = 30) -> dict:
    """完整技术面分析（基础 + 高级指标）"""
    klines = _fetch_klines(code, days)

    return {
        "code": code,
        "klines_count": len(klines),
        "macd": calc_macd(klines),
        "rsi": calc_rsi(klines),
        "boll": calc_boll(klines),
        "kdj": calc_kdj(klines),
    }


def print_report(result: dict):
    code = result["code"]
    print(f"\n{'=' * 55}")
    print(f"  {code} 高级技术指标")
    print(f"{'=' * 55}")

    # MACD
    m = result.get("macd", {})
    if not m.get("error"):
        d, dea, macd = m["latest"]
        print(f"  MACD: DIF={d}  DEA={dea}  MACD={macd}")
        print(f"        {judge_macd(m)}")

    # RSI
    r = result.get("rsi", {})
    if not r.get("error"):
        print(f"  RSI:  {r['latest']}  → {judge_rsi(r)}")

    # BOLL
    b = result.get("boll", {})
    if not b.get("error"):
        print(f"  BOLL: 上={b['upper']}  中={b['mid']}  下={b['lower']}")
        print(f"        价格={b['latest_price']} → {judge_boll(b)}")

    # KDJ
    k = result.get("kdj", {})
    if not k.get("error"):
        print(f"  KDJ:  K={k['k']}  D={k['d']}  J={k['j']}")
        print(f"        {judge_kdj(k)}")

    print(f"{'=' * 55}\n")
