"""
anomaly.py - 量价异动检测（放量/缩量/背离）

策略：
1. 拉近 N 日 K 线
2. 计算 N 日均量基准
3. 当日量 / 均量 > 阈值 → 放量异动
4. 当日量 / 均量 < 阈值 → 缩量异动
5. 价格与量能背离 → 量价背离
"""

from __future__ import annotations
from typing import Optional

from .kline import _fetch_klines


def _volumes(klines: list[str]) -> list[float]:
    return [float(k.split(",")[5]) for k in klines if k]


def _closes(klines: list[str]) -> list[float]:
    return [float(k.split(",")[2]) for k in klines if k]


def detect_volume_anomaly(code: str, days: int = 30, lookback: int = 5) -> dict:
    """
    量价异动检测。

    Args:
        code: 股票代码
        days: 拉取 K 线天数
        lookback: 计算基准均量的回看窗口（默认 5 日）

    Returns:
        {
          "code": str,
          "anomalies": [
            {"date": ..., "type": "放量突破|缩量回调|量价背离", "ratio": 2.1, "price_chg": +3.2, "note": "..."}
          ],
          "baseline_avg_volume_5d": float,
          ...
        }
    """
    klines = _fetch_klines(code, days)
    if len(klines) < lookback + 2:
        return {"code": code, "anomalies": [], "error": "K线不足"}

    closes = _closes(klines)
    volumes = _volumes(klines)

    anomalies = []
    baseline_avg = sum(volumes[:lookback]) / lookback  # 初始基准

    for i in range(lookback, len(klines)):
        # 滚动基准：最近 lookback 日（不含当日）
        ref_window = volumes[max(0, i - lookback):i]
        if not ref_window:
            continue
        baseline = sum(ref_window) / len(ref_window)
        cur_v = volumes[i]
        ratio = cur_v / baseline if baseline > 0 else 0

        d = klines[i].split(",")[0]
        price_chg = (closes[i] - closes[i - 1]) / closes[i - 1] * 100 if closes[i - 1] > 0 else 0

        # 放量：> 2 倍均量
        if ratio >= 2.0 and abs(price_chg) > 1:
            anomaly_type = "放量突破" if price_chg > 0 else "放量下跌"
            anomalies.append({
                "date": d,
                "type": anomaly_type,
                "volume_ratio": round(ratio, 2),
                "price_chg_pct": round(price_chg, 2),
                "note": f"成交量是过去{lookback}日均量的 {round(ratio, 2)} 倍，价格变动 {round(price_chg, 2)}%",
            })
        # 缩量：< 0.4 倍均量
        elif ratio <= 0.4 and abs(price_chg) > 0.5:
            anomaly_type = "缩量上行" if price_chg > 0 else "缩量回调"
            anomalies.append({
                "date": d,
                "type": anomaly_type,
                "volume_ratio": round(ratio, 2),
                "price_chg_pct": round(price_chg, 2),
                "note": f"成交量是过去{lookback}日均量的 {round(ratio, 2)} 倍，价格变动 {round(price_chg, 2)}%",
            })

    # 量价背离：近 5 日价格上涨但量能持续萎缩，或反之
    if len(closes) >= 5:
        recent_closes = closes[-5:]
        recent_volumes = volumes[-5:]
        price_trend = recent_closes[-1] - recent_closes[0]  # 总变动
        vol_avg_first = sum(recent_volumes[:2]) / 2
        vol_avg_last = sum(recent_volumes[-2:]) / 2
        vol_trend = vol_avg_last - vol_avg_first

        # 顶背离：价格上涨 + 成交量萎缩
        if price_trend > 0 and vol_trend < 0 and abs(vol_trend) / vol_avg_first > 0.2:
            anomalies.append({
                "date": klines[-1].split(",")[0],
                "type": "⚠️ 顶背离（量价背离）",
                "volume_ratio": round(vol_avg_last / vol_avg_first, 2),
                "price_chg_pct": round((recent_closes[-1] - recent_closes[0]) / recent_closes[0] * 100, 2),
                "note": "近5日价格上涨但成交量持续萎缩，上攻动能不足，可能回调",
            })
        # 底背离：价格下跌 + 成交量萎缩
        elif price_trend < 0 and vol_trend < 0 and abs(vol_trend) / vol_avg_first > 0.2:
            anomalies.append({
                "date": klines[-1].split(",")[0],
                "type": "✓ 底背离（量价背离）",
                "volume_ratio": round(vol_avg_last / vol_avg_first, 2),
                "price_chg_pct": round((recent_closes[-1] - recent_closes[0]) / recent_closes[0] * 100, 2),
                "note": "近5日价格下跌但成交量持续萎缩，杀跌动能不足，可能反弹",
            })

    return {
        "code": code,
        "klines_count": len(klines),
        "lookback_days": lookback,
        "anomalies": anomalies,
        "anomaly_count": len(anomalies),
    }


def print_report(result: dict):
    code = result["code"]
    anomalies = result.get("anomalies", [])
    print(f"\n{'=' * 55}")
    print(f"  {code} 量价异动检测 (近{result['klines_count']}日, 基准{result['lookback_days']}日)")
    print(f"{'=' * 55}")
    if result.get("error"):
        print(f"  错误: {result['error']}")
        return
    if not anomalies:
        print("  未检测到明显异动")
    else:
        print(f"  共检测到 {len(anomalies)} 个异动信号：\n")
        for a in anomalies:
            print(f"  [{a['date']}] {a['type']}")
            print(f"      量比: {a['volume_ratio']}× | 涨跌: {a['price_chg_pct']}%")
            print(f"      📋 {a['note']}")
            print()
    print(f"{'=' * 55}\n")
