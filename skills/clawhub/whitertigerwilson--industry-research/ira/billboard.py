"""
billboard.py - 龙虎榜（个股上榜 + 营业部 + 机构追踪）

主源：akshare 东方财富 + 新浪
- stock_lhb_detail_em(start_date, end_date): 每日上榜个股详情
- stock_lhb_stock_statistic_em(symbol): 个股上榜统计（近一月/三月/六月/一年）
- stock_lhb_hyyyb_em(start_date, end_date): 每日活跃营业部
- stock_lhb_jgzz_sina(symbol): 机构席位追踪（5/10/30/60 天）
"""

from __future__ import annotations
from typing import Optional

try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False


def get_billboard_details(start_date: str, end_date: str) -> dict:
    """
    龙虎榜详情（每日上榜）。

    Args:
        start_date/end_date: YYYYMMDD
    """
    if not HAS_AKSHARE:
        return {"error": "akshare 未安装"}
    try:
        df = ak.stock_lhb_detail_em(start_date=start_date, end_date=end_date)
        if df is None or df.empty:
            return {"error": f"{start_date}-{end_date} 区间无数据"}
        rows = df.to_dict(orient="records")
        return {
            "period": f"{start_date}-{end_date}",
            "row_count": len(rows),
            "rows": rows,
            "source": "eastmoney-lhb",
        }
    except Exception as e:
        return {"error": f"龙虎榜拉取失败: {e}"}


def get_stock_billboard_statistic(period: str = "近一月") -> dict:
    """
    个股上榜统计（按区间）。
    period: 近一月/近三月/近六月/近一年
    """
    if not HAS_AKSHARE:
        return {"error": "akshare 未安装"}
    try:
        df = ak.stock_lhb_stock_statistic_em(symbol=period)
        if df is None or df.empty:
            return {"error": f"{period} 无上榜统计"}
        rows = df.to_dict(orient="records")
        return {
            "period": period,
            "row_count": len(rows),
            "rows": rows[:30],  # 只返回前 30 行，避免输出过多
            "source": "eastmoney-lhb",
        }
    except Exception as e:
        return {"error": f"个股上榜统计拉取失败: {e}"}


def get_institution_tracking(days: str = "30") -> dict:
    """
    机构席位追踪（最近 N 天）。
    days: "5" / "10" / "30" / "60"
    """
    if not HAS_AKSHARE:
        return {"error": "akshare 未安装"}
    try:
        df = ak.stock_lhb_jgzz_sina(symbol=days)
        if df is None or df.empty:
            return {"error": f"近 {days} 天无机构席位数据"}
        rows = df.to_dict(orient="records")
        return {
            "days": days,
            "row_count": len(rows),
            "rows": rows[:30],
            "source": "sina-jgzz",
        }
    except Exception as e:
        return {"error": f"机构席位追踪拉取失败: {e}"}


def print_billboard(result: dict, top: int = 15):
    print(f"\n{'=' * 60}")
    if result.get("error"):
        print(f"  ❌ {result.get('error')}")
        return
    title = result.get("period") or f"近{result.get('days')}天"
    print(f"  龙虎榜: {title} ({result.get('source')})")
    print(f"{'=' * 60}")
    print(f"  数据行数: {result.get('row_count')}")
    rows = result.get("rows", [])[:top]
    if not rows:
        print("  无数据")
        return
    sample = rows[0]
    cols = list(sample.keys())[:8]
    print(f"  字段: {cols}")
    print()
    print(f"  --- 前 {len(rows)} 行 ---")
    for i, r in enumerate(rows, 1):
        # 兼容东财（中文键）和新浪键
        code = r.get("代码") or r.get("股票代码") or r.get("symbol") or "?"
        name = r.get("名称") or r.get("股票名称") or r.get("name") or "?"
        net_buy = r.get("龙虎榜净买额") or r.get("净额") or r.get("net_buy") or r.get("net") or 0
        reason = r.get("上榜原因") or r.get("reason") or ""
        date_str = r.get("最近上榜日") or r.get("日期") or r.get("date") or ""
        change_pct = r.get("涨跌幅") or r.get("change_pct") or 0
        times = r.get("上榜次数") or r.get("times") or ""

        if isinstance(net_buy, (int, float)):
            print(f"  {i}. {code} {name} | {date_str} | 涨跌幅 {change_pct}% | 净额 {net_buy:.2f} 万 | 上榜 {times} 次")
        else:
            print(f"  {i}. {code} {name} | {date_str} | {net_buy} | 上榜 {times} 次")
        if reason and reason != "?":
            print(f"     原因: {reason}")
    print(f"{'=' * 60}\n")