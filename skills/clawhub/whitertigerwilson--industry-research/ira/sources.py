# -*- coding: utf-8 -*-
"""
sources.py - 统一多数据源调度（K线 + 历史估值 + 港美股）

核心思路：
- K线 / 历史估值 / 港股：东财（主）→ 腾讯（备1）→ akshare（备2）
- 美股：yfinance（主）→ 腾讯美股（备）→ 其他
- 任一源失败自动降级，全部失败才抛异常

数据源差异说明（重要）：
- 东财 K 线 CSV 字段：日期,开,收,高,低,成交量,成交额,振幅,涨跌幅,涨跌额,换手率
- 腾讯 K 线字段：[日期,开,收,高,低,成交量(股), 分红dict]
  ⚠️ 腾讯成交量单位是"股"，东财是"手"，转换：股 = 手 × 100
- akshare stock_zh_a_hist：标准 OHLCV + 振幅/涨跌幅/换手率
"""

from __future__ import annotations
import requests
import time
from typing import Optional

from .api_client import HEADERS, market_prefix, eastmoney_get, tencent_get


# ============== 公共配置 ==============
DEFAULT_TIMEOUT = 12
SOURCES_TRIED = []  # 记录本次调用尝试过的源


def _reset_sources():
    global SOURCES_TRIED
    SOURCES_TRIED = []


def _ok(source: str):
    SOURCES_TRIED.append(source)


def _last_source() -> str:
    """返回最后一次成功的源名（供报告/日志）"""
    return SOURCES_TRIED[-1] if SOURCES_TRIED else "none"


# ============== 主源：东财 push2his ==============
def _fetch_klines_eastmoney(code: str, days: int, klt: int = 101, fqt: int = 1) -> Optional[list[str]]:
    """
    东财 push2his 接口（CSV 字符串列表）。

    Args:
        code: 股票代码
        days: 取多少根 K 线
        klt: 101=日 K / 103=季 K / 60=1小时
        fqt: 1=前复权 / 0=不复权 / 2=后复权
    """
    market = market_prefix(code)
    url = (
        f"https://push2his.eastmoney.com/api/qt/stock/kline/get"
        f"?secid={market}.{code}"
        f"&fields1=f1,f2,f3,f4,f5,f6"
        f"&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61"
        f"&lmt={days}&klt={klt}&fqt={fqt}&end=20500101"
    )
    try:
        r = requests.get(url, headers=HEADERS, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        j = r.json()
    except Exception:
        return None

    if j.get("rc") != 0 or not j.get("data"):
        return None
    klines = j["data"].get("klines", [])
    if not klines:
        return None
    return klines


# ============== 备援源 1：腾讯 ifzq 日 K ==============
def _fetch_klines_tencent(code: str, days: int, fqt: str = "qfq") -> Optional[list[str]]:
    """
    腾讯日 K（前/后复权）。

    Args:
        code: 股票代码（不带前缀）
        days: 取多少根 K 线
        fqt: qfq=前复权 / hfq=后复权 / 不传=不复权

    Returns:
        东财格式的 CSV 列表（与东财字段顺序一致）：日期,开,收,高,低,成交量(手),成交额,...
        注：腾讯返回的成交量单位是"股"，已 /100 转为"手"，与东财保持一致
    """
    market = "sh" if code.startswith(("6", "5")) else "sz"
    fqt_param = f",{fqt}" if fqt else ""
    url = f"http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={market}{code},day,,,{days}{fqt_param}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        j = r.json()
    except Exception:
        return None

    if j.get("code") != 0:
        return None
    data = j.get("data", {}).get(f"{market}{code}", {})
    rows = data.get("qfqday") or data.get("hfqday") or data.get("day", [])
    if not rows:
        return None

    csv_lines = []
    for row in rows:
        if len(row) < 6:
            continue
        date = row[0]
        o = float(row[1]) if row[1] else 0.0
        c = float(row[2]) if row[2] else 0.0
        h = float(row[3]) if row[3] else 0.0
        l = float(row[4]) if row[4] else 0.0
        vol_shares = float(row[5]) if row[5] else 0.0
        vol_hands = vol_shares / 100.0  # 腾讯是股，东财是手
        # 构造与东财一致的 CSV（换手率字段先填0，稍后用实时接口补最新换手率）
        csv_lines.append(
            f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol_hands:.0f},0,,0,0,0"
        )

    # 用腾讯实时接口补最新换手率
    latest_turnover = _get_tencent_realtime_turnover(code)
    if latest_turnover is not None and csv_lines:
        # 替换最后一行的换手率字段（第10列，索引10）
        last = csv_lines[-1].split(",")
        if len(last) >= 11:
            last[10] = f"{latest_turnover:.2f}"
            csv_lines[-1] = ",".join(last)

    return csv_lines


def _get_tencent_realtime_turnover(code: str) -> Optional[float]:
    """获取腾讯实时换手率"""
    market = "sh" if code.startswith(("6", "5")) else "sz"
    url = f"http://qt.gtimg.cn/q={market}{code}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        text = r.text.strip()
        if '="' not in text:
            return None
        payload = text.split('="', 1)[1].rstrip('";')
        fields = payload.split('~')
        # 腾讯字段：[38] = 换手率（字符串形式的百分比，如 "1.57"）
        if len(fields) > 38 and fields[38]:
            return float(fields[38])
    except Exception:
        pass
    return None


# ============== 备援源 2：akshare stock_zh_a_hist ==============
def _fetch_klines_akshare(code: str, days: int, adjust: str = "qfq") -> Optional[list[str]]:
    """
    akshare stock_zh_a_hist（最终备援）。

    Args:
        code: 股票代码
        days: 取多少根 K 线（按 end_date 倒推）
        adjust: qfq=前复权 / hfq=后复权 / 不传=不复权
    """
    try:
        import akshare as ak
    except ImportError:
        return None

    from datetime import datetime, timedelta
    end_dt = datetime.now()
    start_dt = end_dt - timedelta(days=int(days * 1.6) + 30)  # 多取些覆盖节假日
    start_str = start_dt.strftime("%Y%m%d")
    end_str = end_dt.strftime("%Y%m%d")

    try:
        df = ak.stock_zh_a_hist(
            symbol=code, period="daily", adjust=adjust,
            start_date=start_str, end_date=end_str,
        )
    except Exception:
        return None

    if df is None or len(df) == 0:
        return None

    csv_lines = []
    # akshare 列：日期,开盘,收盘,最高,最低,成交量,成交额,振幅,涨跌幅,涨跌额,换手率
    for _, row in df.iterrows():
        try:
            date = str(row["日期"])
            o = float(row["开盘"])
            c = float(row["收盘"])
            h = float(row["最高"])
            l = float(row["最低"])
            vol = float(row["成交量"]) if row["成交量"] else 0.0  # 手
            amt = float(row["成交额"]) if row["成交额"] else 0.0
            amp = float(row["振幅"]) if row["振幅"] else 0.0
            chg_pct = float(row["涨跌幅"]) if row["涨跌幅"] else 0.0
            chg_amt = float(row["涨跌额"]) if row["涨跌额"] else 0.0
            turnover = float(row["换手率"]) if row["换手率"] else 0.0
            csv_lines.append(
                f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol:.0f},{amt:.0f},{amp:.2f},{chg_pct:.2f},{chg_amt:.2f},{turnover:.2f}"
            )
        except Exception:
            continue

    if len(csv_lines) > days:
        csv_lines = csv_lines[-days:]
    return csv_lines


# ============== 统一 K 线接口 ==============
def fetch_klines(code: str, days: int = 60, klt: int = 101, fqt: int = 1,
                 prefer: str = "eastmoney") -> list[str]:
    """
    K线统一调度：按 prefer → 备援1 → 备援2 顺序尝试。

    Args:
        code: 股票代码
        days: 拉取 K 线根数
        klt: K线周期（101=日/103=季）
        fqt: 复权方式（1=前复权）
        prefer: "eastmoney" / "tencent" / "akshare"

    Returns:
        CSV 字符串列表（与东财字段顺序一致）

    Raises:
        RuntimeError: 三个源全部失败
    """
    _reset_sources()
    sources = []
    if prefer == "eastmoney":
        sources = [
            ("eastmoney", lambda: _fetch_klines_eastmoney(code, days, klt, fqt)),
            ("tencent", lambda: _fetch_klines_tencent(code, days, "qfq")),
            ("akshare", lambda: _fetch_klines_akshare(code, days, "qfq")),
        ]
    elif prefer == "tencent":
        sources = [
            ("tencent", lambda: _fetch_klines_tencent(code, days, "qfq")),
            ("eastmoney", lambda: _fetch_klines_eastmoney(code, days, klt, fqt)),
            ("akshare", lambda: _fetch_klines_akshare(code, days, "qfq")),
        ]
    elif prefer == "akshare":
        sources = [
            ("akshare", lambda: _fetch_klines_akshare(code, days, "qfq")),
            ("eastmoney", lambda: _fetch_klines_eastmoney(code, days, klt, fqt)),
            ("tencent", lambda: _fetch_klines_tencent(code, days, "qfq")),
        ]
    else:
        sources = [
            ("eastmoney", lambda: _fetch_klines_eastmoney(code, days, klt, fqt)),
            ("tencent", lambda: _fetch_klines_tencent(code, days, "qfq")),
            ("akshare", lambda: _fetch_klines_akshare(code, days, "qfq")),
        ]

    last_err = None
    for name, fetcher in sources:
        try:
            result = fetcher()
            if result:
                _ok(name)
                return result
        except Exception as e:
            last_err = e
            continue

    tried = " → ".join([s[0] for s in sources])
    raise RuntimeError(f"所有 K 线源均失败（{tried}）。最后一次错误: {last_err}")


# ============== 港股历史 K 线（备援） ==============
def _fetch_hk_klines_tencent(code: str, days: int) -> Optional[list[str]]:
    """
    腾讯港股日 K。

    Args:
        code: 港股 5 位代码（如 '00700'）
        days: 拉取根数
    """
    code_padded = code.zfill(5)
    url = f"http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=hk{code_padded},day,,,{days},qfq"
    try:
        r = requests.get(url, headers=HEADERS, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        j = r.json()
    except Exception:
        return None

    if j.get("code") != 0:
        return None
    data = j.get("data", {}).get(f"hk{code_padded}", {})
    rows = data.get("qfqday") or data.get("day", [])
    if not rows:
        return None

    csv_lines = []
    for row in rows:
        if len(row) < 6:
            continue
        date = row[0]
        o = float(row[1]) if row[1] else 0.0
        c = float(row[2]) if row[2] else 0.0
        h = float(row[3]) if row[3] else 0.0
        l = float(row[4]) if row[4] else 0.0
        vol = float(row[5]) / 100 if row[5] else 0.0  # 股 → 手
        csv_lines.append(f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol:.0f},0,,0,0,0")
    return csv_lines


def fetch_hk_klines(code: str, days: int = 60) -> list[str]:
    """港股 K 线统一调度（东财 → 腾讯）"""
    _reset_sources()
    code_padded = code.zfill(5)
    sources = [
        ("akshare_hk", lambda: _fetch_hk_akshare(code, days)),
        ("tencent_hk", lambda: _fetch_hk_klines_tencent(code, days)),
    ]
    for name, fn in sources:
        try:
            result = fn()
            if result:
                _ok(name)
                return result
        except Exception:
            continue
    raise RuntimeError(f"港股 K 线所有源均失败")


def _fetch_hk_akshare(code: str, days: int) -> Optional[list[str]]:
    """akshare stock_hk_hist 备援"""
    try:
        import akshare as ak
    except ImportError:
        return None
    try:
        df = ak.stock_hk_hist(symbol=code.zfill(5), period="daily", adjust="qfq")
    except Exception:
        return None
    if df is None or len(df) == 0:
        return None

    csv_lines = []
    for _, row in df.iterrows():
        try:
            date = str(row["日期"])
            o = float(row["开盘"])
            c = float(row["收盘"])
            h = float(row["最高"])
            l = float(row["最低"])
            vol = float(row["成交量"]) if row["成交量"] else 0.0
            csv_lines.append(f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol:.0f},0,,0,0,0")
        except Exception:
            continue
    if len(csv_lines) > days:
        csv_lines = csv_lines[-days:]
    return csv_lines


# ============== 美股 K 线（多源） ==============
def _fetch_us_klines_yfinance(code: str, days: int) -> Optional[list[str]]:
    """yfinance 美股日 K（首选）"""
    try:
        import yfinance as yf
    except ImportError:
        return None
    try:
        ticker = yf.Ticker(code)
        df = ticker.history(period=f"{days}d", auto_adjust=True)
    except Exception:
        return None
    if df is None or len(df) == 0:
        return None

    csv_lines = []
    for idx, row in df.iterrows():
        try:
            date = idx.strftime("%Y-%m-%d")
            o = float(row["Open"])
            c = float(row["Close"])
            h = float(row["High"])
            l = float(row["Low"])
            vol = float(row["Volume"])
            csv_lines.append(f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol:.0f},0,,0,0,0")
        except Exception:
            continue
    return csv_lines


def _fetch_us_klines_akshare(code: str, days: int) -> Optional[list[str]]:
    """akshare stock_us_daily 备援（注意：接口可能变更，需 try/except）"""
    try:
        import akshare as ak
    except ImportError:
        return None
    try:
        # 兼容不同版本：symbol 可能是 '105.NVDA' 或 'NVDA'
        df = ak.stock_us_daily(symbol=code, adjust="qfq")
    except Exception:
        try:
            df = ak.stock_us_hist(symbol=code, period="daily", adjust="qfq")
        except Exception:
            return None
    if df is None or len(df) == 0:
        return None

    csv_lines = []
    for _, row in df.iterrows():
        try:
            date = str(row.get("date") or row.get("日期") or row.name)
            o = float(row.get("open") or row.get("开盘"))
            c = float(row.get("close") or row.get("收盘"))
            h = float(row.get("high") or row.get("最高"))
            l = float(row.get("low") or row.get("最低"))
            vol = float(row.get("volume") or row.get("成交量") or 0)
            csv_lines.append(f"{date},{o:.2f},{c:.2f},{h:.2f},{l:.2f},{vol:.0f},0,,0,0,0")
        except Exception:
            continue
    if len(csv_lines) > days:
        csv_lines = csv_lines[-days:]
    return csv_lines


def fetch_us_klines(code: str, days: int = 60) -> list[str]:
    """
    美股 K 线统一调度。

    Args:
        code: 美股代码（多种格式都接受，如 'NVDA' / '105.NVDA'）
    """
    _reset_sources()
    sources = [
        ("yfinance", lambda: _fetch_us_klines_yfinance(code, days)),
        ("akshare_us", lambda: _fetch_us_klines_akshare(code, days)),
    ]
    last_err = None
    for name, fn in sources:
        try:
            result = fn()
            if result:
                _ok(name)
                return result
        except Exception as e:
            last_err = e
            continue
    raise RuntimeError(f"美股 K 线所有源均失败（{[s[0] for s in sources]}）。最后错误: {last_err}")


# ============== 诊断工具 ==============
def diagnose_sources(code: str = "601899") -> dict:
    """
    诊断指定代码的 K 线各源可用性。

    Returns:
        {"code": ..., "results": [{"source": ..., "ok": bool, "rows": N, "error": ...}, ...]}
    """
    results = []
    for name, fn in [
        ("eastmoney", lambda: _fetch_klines_eastmoney(code, 60)),
        ("tencent", lambda: _fetch_klines_tencent(code, 60)),
        ("akshare", lambda: _fetch_klines_akshare(code, 60)),
    ]:
        try:
            r = fn()
            results.append({"source": name, "ok": r is not None and len(r) > 0,
                            "rows": len(r) if r else 0, "error": None})
        except Exception as e:
            results.append({"source": name, "ok": False, "rows": 0,
                            "error": f"{type(e).__name__}: {str(e)[:80]}"})
    return {"code": code, "results": results}