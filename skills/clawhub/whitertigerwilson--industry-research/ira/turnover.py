"""
turnover.py - 换手率分析
"""

from __future__ import annotations
from typing import Optional

from .sources import fetch_klines as _multi_fetch_klines


def _fetch_klines(code: str, days: int) -> list[str]:
    """拉取 K 线原始 CSV 行（多源 fallback：东财 → 腾讯 → akshare）"""
    lmt = max(days + 10, int(days * 1.5))
    klines = _multi_fetch_klines(code, lmt, klt=101, fqt=1)
    if len(klines) > days:
        klines = klines[-days:]
    return klines


def get_turnover(code: str, days: int = 30) -> dict:
    """
    获取股票最近 N 个交易日换手率统计。

    Returns:
        {
          "code": str,
          "days": int,
          "total": float,            # 累计换手率 (%)
          "high_days": int,          # 超过 5% 换手的天数
          "activity": str,           # 活跃度（高度活跃/正常活跃/相对冷清）
          "daily": list[dict],       # 每日明细
        }
    """
    klines = _fetch_klines(code, days)

    total = 0.0
    high_days = 0
    daily = []
    for k in klines:
        f = k.split(",")
        try:
            turnover = float(f[10]) if len(f) > 10 and f[10] else 0.0
        except Exception:
            turnover = 0.0
        total += turnover
        if turnover > 5:
            high_days += 1
        daily.append({"date": f[0], "close": float(f[2]) if f[2] else 0.0, "turnover": turnover})

    if total > 100:
        activity = "HIGHLY ACTIVE"
    elif total > 50:
        activity = "Normal Activity"
    else:
        activity = "Relatively Quiet"

    return {
        "code": code,
        "days": len(daily),
        "total": round(total, 1),
        "high_days": high_days,
        "activity": activity,
        "daily": daily,
    }


def print_report(result: dict):
    print(f"\n{'=' * 55}")
    print(f"  股票代码: {result['code']}  |  统计天数: {result['days']}")
    print(f"{'=' * 55}")
    print(f"  {'日期':<12} {'收盘价':>8}  {'换手率':>8}")
    print(f"  {'-' * 12} {'-' * 8}  {'-' * 8}")
    for d in result["daily"]:
        marker = " ★" if d["turnover"] > 5 else ""
        print(f"  {d['date']:<12} {d['close']:>8.2f}  {d['turnover']:>7.2f}%{marker}")
    print(f"{'=' * 55}")
    print(f"  {result['days']}日累计换手率: {result['total']}%  |  {result['activity']}")
    print(f"  超5%换手天数:   {result['high_days']}天")
    print(f"{'=' * 55}\n")
