"""
futures.py - 期货主力合约数据

主源：akshare.futures_zh_daily_sina（新浪；带 0 后缀拿主力连续合约）
- futures_zh_daily_sina：拿指定品种的连续日数据（开高低收量持结）

实测：沪铜(CU0) / 螺纹钢(RB0) / 黄金(AU0) 全部稳定
"""

from __future__ import annotations
from typing import Optional

try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False


# 中文商品 → 期货代码（带 0 后缀拿主力连续合约）
COMMODITY_TO_SYMBOL = {
    "铜": "CU0",
    "铝": "AL0",
    "锌": "ZN0",
    "黄金": "AU0",
    "白银": "AG0",
    "螺纹钢": "RB0",
    "螺纹": "RB0",
    "热卷": "HC0",
    "铁矿石": "I0",
    "焦煤": "JM0",
    "焦炭": "J0",
    "原油": "SC0",
    "燃油": "FU0",
    "沥青": "BU0",
    "橡胶": "RU0",
    "塑料": "L0",
    "PVC": "V0",
    "PP": "PP0",
    "豆粕": "M0",
    "豆油": "Y0",
    "棕榈油": "P0",
    "玉米": "C0",
    "玉米淀粉": "CS0",
    "鸡蛋": "JD0",
    "棉花": "CF0",
    "白糖": "SR0",
    "PTA": "TA0",
    "甲醇": "MA0",
    "玻璃": "FG0",
    "纯碱": "SA0",
    "尿素": "UR0",
}


def get_main_contract(commodity: str, days: int = 60) -> dict:
    """
    拿到某品种主力连续合约的最近 N 日数据。

    Returns:
        {
          "commodity", "symbol",
          "rows": [{date, open, high, low, close, volume, hold, settle}, ...],
          "klines_count",
          "latest_close", "latest_date", "change_pct_5d",
          "source": "akshare-sina" | "akshare-em" | "fallback",
        }
    """
    if not HAS_AKSHARE:
        return {
            "error": "akshare 未安装，请运行: pip install akshare",
            "commodity": commodity,
        }

    sym = COMMODITY_TO_SYMBOL.get(commodity)
    if not sym:
        return {
            "error": f"未配置 {commodity} 的品种代码。可用：{list(COMMODITY_TO_SYMBOL.keys())}",
            "commodity": commodity,
        }

    try:
        df = ak.futures_zh_daily_sina(symbol=sym)
    except Exception as e:
        return {
            "error": f"数据拉取失败: {e}",
            "commodity": commodity,
            "symbol": sym,
        }

    if df is None or df.empty:
        return {"error": "无活跃合约数据", "commodity": commodity, "symbol": sym}

    rows = []
    for _, row in df.iterrows():
        rows.append({
            "date": str(row.get("date", "")),
            "open": float(row.get("open", 0) or 0),
            "high": float(row.get("high", 0) or 0),
            "low": float(row.get("low", 0) or 0),
            "close": float(row.get("close", 0) or 0),
            "volume": float(row.get("volume", 0) or 0),
            "open_interest": float(row.get("hold", 0) or 0),
            "settle": float(row.get("settle", 0) or 0),
        })

    rows = sorted(rows, key=lambda x: x["date"])
    recent = rows[-min(days, len(rows)):]

    latest = recent[-1] if recent else {}
    change_5d = 0.0
    if len(recent) >= 6:
        ref_close = recent[-6]["close"]
        cur_close = latest.get("close", 0)
        if ref_close:
            change_5d = (cur_close - ref_close) / ref_close * 100

    return {
        "commodity": commodity,
        "symbol": sym,
        "rows": recent,
        "klines_count": len(recent),
        "latest_close": latest.get("close"),
        "latest_open": latest.get("open"),
        "latest_high": latest.get("high"),
        "latest_low": latest.get("low"),
        "latest_date": latest.get("date"),
        "latest_volume": latest.get("volume"),
        "latest_open_interest": latest.get("open_interest"),
        "change_pct_5d": round(change_5d, 2),
        "source": "akshare-sina",
    }


def list_supported_commodities() -> list[str]:
    """返回所有支持的商品列表"""
    return list(COMMODITY_TO_SYMBOL.keys())


def print_report(result: dict):
    print(f"\n{'=' * 60}")
    if result.get("error"):
        print(f"  ❌ {result.get('commodity', '?')} ({result.get('symbol', '?')})")
        print(f"  错误: {result['error']}")
        print(f"{'=' * 60}\n")
        return

    print(f"  商品: {result.get('commodity')} ({result.get('symbol')}) 主力连续")
    print(f"  数据源: {result.get('source')}")
    print(f"{'=' * 60}")
    print(f"  数据天数: {result.get('klines_count')}")
    print(f"  最新: 收 {result.get('latest_close')} (开 {result.get('latest_open')})")
    print(f"       高/低: {result.get('latest_high')} / {result.get('latest_low')}")
    print(f"       日期: {result.get('latest_date')}")
    print(f"  5日累计涨跌: {result.get('change_pct_5d')}%")
    print(f"  持仓量: {result.get('latest_open_interest')}")
    print(f"  成交量: {result.get('latest_volume')}")

    print(f"\n  --- 最近 10 个交易日 ---")
    print(f"  {'日期':<12} {'开盘':>10} {'收盘':>10} {'最高':>10} {'最低':>10} {'持仓量':>12}")
    for r in result.get("rows", [])[-10:]:
        print(f"  {r['date']:<12} {r['open']:>10.0f} {r['close']:>10.0f} {r['high']:>10.0f} {r['low']:>10.0f} {r['open_interest']:>12.0f}")
    print(f"{'=' * 60}\n")
