"""
global_stocks.py - 港股 + 美股（按代码查询）

策略：
- 港股：akshare.stock_hk_spot_em()（4688 只，约 1 分钟拉取）+ stock_hk_hist(symbol='00700')
- 美股：akshare.stock_us_zh_spot_em() 中概股（约 1 分钟）+ stock_us_hist(symbol='AAPL') 个股

不走 stock_us_spot_em（全美股列表 135 页，太慢）
"""

from __future__ import annotations
from typing import Optional
import time

try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False

try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False

from .sources import fetch_hk_klines, fetch_us_klines


# 港股热门代码（5/7 位数都行）
POPULAR_HK = {
    "00700": "腾讯控股",
    "09988": "阿里巴巴-W",
    "03690": "美团-W",
    "01024": "快手-W",
    "02318": "中国平安",
    "00939": "建设银行",
    "01398": "工商银行",
    "03988": "中国银行",
    "02628": "中国人寿",
    "01211": "比亚迪股份",
    "02015": "理想汽车-W",
    "09868": "小鹏汽车-W",
    "02333": "长城汽车",
    "09999": "网易-S",
    "09618": "京东集团-SW",
    "09961": "携程集团-S",
    "01810": "小米集团-W",
    "09698": "万国数据-SW",
}

# 美股热门代码
POPULAR_US = {
    "AAPL": "苹果",
    "MSFT": "微软",
    "GOOGL": "谷歌",
    "AMZN": "亚马逊",
    "META": "Meta",
    "TSLA": "特斯拉",
    "NVDA": "英伟达",
    "NFLX": "奈飞",
    "BABA": "阿里巴巴",
    "PDD": "拼多多",
    "JD": "京东",
    "BIDU": "百度",
    "NIO": "蔚来",
    "XPEV": "小鹏汽车",
    "LI": "理想汽车",
    "BILI": "哔哩哔哩",
}


def _code_to_hk_symbol(code: str) -> str:
    """归一化港股代码：'700' -> '00700'"""
    s = code.strip().lstrip("0")
    s = s.zfill(5)
    return s


def get_hk_realtime(code: str) -> dict:
    """港股实时行情（按代码）"""
    if not HAS_AKSHARE:
        return {"error": "akshare 未安装"}
    code5 = _code_to_hk_symbol(code)
    try:
        # 港股盘后实时：按代码查
        df = ak.stock_hk_hist(symbol=code5, period="daily", adjust="qfq")
        if df is None or df.empty:
            return {"error": f"未找到 {code5} 港股数据"}
        last = df.iloc[-1]
        return {
            "market": "港股",
            "code": code5,
            "name": POPULAR_HK.get(code5, "（待查）"),
            "latest_date": str(last.get("日期", "")),
            "latest_close": float(last.get("收盘", 0) or 0),
            "latest_open": float(last.get("开盘", 0) or 0),
            "latest_high": float(last.get("最高", 0) or 0),
            "latest_low": float(last.get("最低", 0) or 0),
            "latest_volume": float(last.get("成交量", 0) or 0),
            "history_rows": len(df),
        }
    except Exception as e:
        return {"error": f"港股 {code5} 拉取失败: {e}"}


def get_us_realtime(code: str) -> dict:
    """美股实时行情（yfinance 首选 → akshare 备援）"""
    code = code.upper().strip()
    last_err = None

    # 优先 yfinance
    if HAS_YFINANCE:
        try:
            ticker = yf.Ticker(code)
            df = ticker.history(period="5d", auto_adjust=True)
            if df is not None and len(df) > 0:
                last = df.iloc[-1]
                return {
                    "market": "美股",
                    "code": code,
                    "name": POPULAR_US.get(code, "（待查）"),
                    "latest_date": str(last.name.strftime("%Y-%m-%d")) if hasattr(last.name, 'strftime') else str(last.name),
                    "latest_close": float(last["Close"]),
                    "latest_open": float(last["Open"]),
                    "latest_high": float(last["High"]),
                    "latest_low": float(last["Low"]),
                    "latest_volume": float(last["Volume"]),
                    "history_rows": len(df),
                    "source": "yfinance",
                }
        except Exception as e:
            last_err = e

    # akshare 备援
    if HAS_AKSHARE:
        try:
            # 兼容不同接口
            df = ak.stock_us_daily(symbol=code, adjust="qfq")
            if df is None or df.empty:
                df = ak.stock_us_hist(symbol=code, period="daily", adjust="qfq")
            if df is None or df.empty:
                return {"error": f"未找到 {code} 美股数据"}
            last = df.iloc[-1]
            return {
                "market": "美股",
                "code": code,
                "name": POPULAR_US.get(code, "（待查）"),
                "latest_date": str(last.get("date", "") or last.name),
                "latest_close": float(last.get("close", 0) or last.get("收盘", 0) or 0),
                "latest_open": float(last.get("open", 0) or last.get("开盘", 0) or 0),
                "latest_high": float(last.get("high", 0) or last.get("最高", 0) or 0),
                "latest_low": float(last.get("low", 0) or last.get("最低", 0) or 0),
                "latest_volume": float(last.get("volume", 0) or last.get("成交量", 0) or 0),
                "history_rows": len(df),
                "source": "akshare",
            }
        except Exception as e:
            last_err = e

    return {"error": f"美股 {code} 拉取失败（yfinance + akshare 均失败）: {last_err}"}


def get_global_realtime(code: str) -> dict:
    """根据代码长度自动判断港股还是美股"""
    code = code.strip().lstrip("0")
    if not code:
        return {"error": "代码为空"}
    # 5 位纯数字 → 港股；字母 → 美股
    if code.isdigit():
        return get_hk_realtime(code)
    return get_us_realtime(code)


def search_hk(keyword: str) -> list[dict]:
    """关键词搜港股（在常用列表里）"""
    results = []
    for code, name in POPULAR_HK.items():
        if keyword in name or keyword in code:
            results.append({"code": code, "name": name})
    return results


def search_us(keyword: str) -> list[dict]:
    """关键词搜美股（在常用列表里）"""
    results = []
    for code, name in POPULAR_US.items():
        if keyword in name or keyword.upper() in code.upper():
            results.append({"code": code, "name": name})
    return results


def print_global(result: dict):
    print(f"\n{'=' * 55}")
    if result.get("error"):
        print(f"  ❌ {result.get('market', '?')} {result.get('code', '?')}")
        print(f"  错误: {result['error']}")
        return
    print(f"  {result.get('market')}: {result.get('code')} {result.get('name')}")
    print(f"{'=' * 55}")
    print(f"  最新: {result.get('latest_close')} ({result.get('latest_date')})")
    print(f"  开/高/低: {result.get('latest_open')} / {result.get('latest_high')} / {result.get('latest_low')}")
    print(f"  成交量: {result.get('latest_volume')}")
    print(f"  历史数据: {result.get('history_rows')} 行")
    print(f"{'=' * 55}\n")