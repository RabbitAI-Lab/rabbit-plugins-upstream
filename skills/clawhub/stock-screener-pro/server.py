# -*- coding: utf-8 -*-
"""
Unified Stock Analysis & Quantitative Toolkit MCP Server for OpenClaw (v3.1.1).

Complete Coverage of Daily Stock Analysis Capabilities:
1. Fast quantitative screening (screen_stocks: 5 multi-factor strategies across 5200+ A-shares)
2. Realtime quote & technical diagnosis (ask_stock: MA, RSI, trend, support/pressure levels)
3. Historical K-line backtesting (backtest_strategy: SMA cross, momentum breakout, RSI mean-reversion)
4. Macro Market Review (get_market_review: Major indices, total volume, market breadth, sentiment)
5. Portfolio & Watchlist Management (manage_portfolio: add/remove/list watchlist & holdings, calculate PnL)
6. Price & Technical Alert Management (manage_alerts: create/list/delete price & technical alerts)
7. Deep AI Report & Research Trigger (generate_ai_report: invokes local DSA engine for complete multi-agent investment reports)
8. ML short-term direction prediction (predict_stock: walk-forward RF+GB ensemble, next-5-day signal)
9. Strategy Catalog Query (get_strategies)

Zero-token standalone mode for 1-6 (via Tencent high-availability feeds + local SQLite/JSON).
Auto-connects to local DSA service (port 8000) for deep AI reports.
"""

from __future__ import annotations

import json
import logging
import os
import sqlite3
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("stock-copilot")

mcp = FastMCP(
    name="stock-copilot",
)

DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_UNIVERSE_PATH = os.path.join(DIR, "stock_universe.json")
PORTFOLIO_DB_PATH = os.path.join(DIR, "user_portfolio.db")
INDEX_PATH = os.getenv(
    "DSA_INDEX_PATH",
    os.path.join(os.path.expanduser("~"), ".cache", "daily_stock_analysis", "stocks.index.json"),
)
DSA_BASE_URL = os.getenv("DSA_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
DSA_PASSWORD = os.getenv("DSA_ADMIN_PASSWORD", "")

_session_cookie: Optional[str] = None


def _init_portfolio_db():
    """Ensure local portfolio & watchlist sqlite tables exist."""
    try:
        with sqlite3.connect(PORTFOLIO_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS watchlist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE,
                    name TEXT,
                    group_name TEXT DEFAULT '默认自选',
                    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE,
                    name TEXT,
                    cost_price REAL,
                    shares INTEGER,
                    group_name TEXT DEFAULT '默认持仓',
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS alert_rules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT,
                    name TEXT,
                    rule_type TEXT, -- 'price_above', 'price_below', 'pct_chg_above', 'pct_chg_below'
                    threshold REAL,
                    status TEXT DEFAULT 'active',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()
    except Exception as e:
        logger.error(f"Failed to init portfolio db: {e}")


_init_portfolio_db()


def _clean_code(code: str) -> tuple[str, str]:
    """Return (market_prefix, 6_digit_code)."""
    c = code.strip().lower()
    if c.startswith("sh") or c.startswith("sz"):
        return c[:2], c[2:]
    if c.endswith(".sh") or c.endswith(".ss"):
        return "sh", c.split(".")[0]
    if c.endswith(".sz"):
        return "sz", c.split(".")[0]
    if c.startswith("6") or c.startswith("9"):
        return "sh", c
    return "sz", c


def _get_a_share_pool() -> List[Dict[str, str]]:
    """Load A-share universe: prefer local bundled stock_universe.json, fallback to global index."""
    if os.path.exists(LOCAL_UNIVERSE_PATH):
        try:
            with open(LOCAL_UNIVERSE_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
                return [{"code": r[0], "name": r[1], "market": r[2]} for r in raw]
        except Exception as e:
            logger.debug(f"Failed to load bundled stock_universe.json: {e}")

    if os.path.exists(INDEX_PATH):
        try:
            with open(INDEX_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            stocks = []
            for item in data:
                if len(item) >= 8:
                    sym, code, name, pinyin, abbr, aliases, region, stype = item[:8]
                    if region == "CN" and stype == "stock":
                        if code.startswith("60") or code.startswith("68"):
                            stocks.append({"code": code, "name": name, "market": "sh"})
                        elif code.startswith("00") or code.startswith("30"):
                            stocks.append({"code": code, "name": name, "market": "sz"})
            if stocks:
                return stocks
        except Exception as e:
            logger.debug(f"Failed to load global stock index: {e}")

    return [
        {"code": "600519", "name": "贵州茅台", "market": "sh"},
        {"code": "300750", "name": "宁德时代", "market": "sz"},
        {"code": "002594", "name": "比亚迪", "market": "sz"},
        {"code": "601318", "name": "中国平安", "market": "sh"},
        {"code": "000001", "name": "平安银行", "market": "sz"},
    ]


def _fetch_batch_quotes(stocks: List[Dict[str, str]], timeout: int = 6) -> List[Dict[str, Any]]:
    """Fetch realtime quotes in batch from Tencent API."""
    if not stocks:
        return []

    results = []
    batch_size = 80
    batches = [stocks[i : i + batch_size] for i in range(0, len(stocks), batch_size)]

    def fetch_chunk(chunk):
        codes_query = [f"{s['market']}{s['code']}" for s in chunk]
        url = f"http://qt.gtimg.cn/q={','.join(codes_query)}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as res:
                text = res.read().decode("gbk", errors="ignore")
            chunk_res = []
            for line in text.strip().split(";\n"):
                if not line:
                    continue
                parts = line.split("~")
                if len(parts) > 46:
                    try:
                        price = float(parts[3])
                        if price <= 0:
                            continue
                        name = parts[1]
                        code = parts[2]
                        prev_close = float(parts[4]) if parts[4] else price
                        open_p = float(parts[5]) if parts[5] else price
                        high_p = float(parts[33]) if parts[33] else price
                        low_p = float(parts[34]) if parts[34] else price
                        vol_hand = float(parts[6]) if parts[6] else 0.0
                        amount_w = float(parts[37]) if parts[37] else 0.0
                        pct_chg = float(parts[32]) if parts[32] else 0.0
                        turnover = float(parts[38]) if parts[38] else 0.0
                        pe_ttm = float(parts[39]) if parts[39] else 0.0
                        pb = float(parts[46]) if parts[46] else 0.0
                        mkt_cap = float(parts[45]) if parts[45] else 0.0
                        vol_ratio = float(parts[49]) if len(parts) > 49 and parts[49] else 1.0

                        chunk_res.append(
                            {
                                "code": code,
                                "name": name,
                                "price": price,
                                "open": open_p,
                                "high": high_p,
                                "low": low_p,
                                "prev_close": prev_close,
                                "pct_chg": pct_chg,
                                "turnover": turnover,
                                "pe_ttm": pe_ttm,
                                "pb": pb,
                                "mkt_cap_yi": mkt_cap,
                                "amount_wan": amount_w,
                                "vol_hand": vol_hand,
                                "vol_ratio": vol_ratio,
                            }
                        )
                    except Exception:
                        continue
            return chunk_res
        except Exception as err:
            logger.debug(f"Fetch chunk error: {err}")
            return []

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(fetch_chunk, b) for b in batches]
        for f in as_completed(futures):
            results.extend(f.result())

    return results


def _fetch_kline(code: str, count: int = 120) -> List[Dict[str, Any]]:
    """Fetch daily K-lines for indicators and backtest."""
    mkt, c = _clean_code(code)
    sym = f"{mkt}{c}"
    url = f"http://ifzq.gtimg.cn/appstock/app/fqkline/get?param={sym},day,,,{count},qfq"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
        raw = data.get("data", {}).get(sym, {}).get("qfqday", [])
        if not raw:
            raw = data.get("data", {}).get(sym, {}).get("day", [])
        klines = []
        for r in raw:
            if len(r) >= 6:
                klines.append(
                    {
                        "date": r[0],
                        "open": float(r[1]),
                        "close": float(r[2]),
                        "high": float(r[3]),
                        "low": float(r[4]),
                        "vol": float(r[5]),
                    }
                )
        return klines
    except Exception as e:
        logger.debug(f"Failed to fetch kline for {code}: {e}")
        return []


def _to_exchange_code(code: str) -> str:
    """Normalize to 600519.SH / 000001.SZ form."""
    mkt, c = _clean_code(code)
    return f"{c}.{'SH' if mkt == 'sh' else 'SZ'}"


def _fetch_klines_extended(symbol_code: str, max_page: int = 12) -> pd.DataFrame:
    """Fetch paginated qfq daily bars (old->new) for ML prediction."""

    def fetch(start: str, end: str, count: int = 800) -> List:
        url = (
            f"https://ifzq.gtimg.cn/appstock/app/fqkline/get"
            f"?param={symbol_code},day,{start},{end},{count},qfq"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://gu.qq.com/"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        node = d.get("data", {}).get(symbol_code, {})
        return node.get("qfqday") or node.get("day", [])

    all_bars: List = []
    prev_start: Optional[str] = None
    for _ in range(max_page):
        part = fetch("", prev_start or "", 800)
        if not part:
            break
        if prev_start:
            keep = [b for b in part if b[0] < prev_start]
            if not keep:
                break
            part = keep
        all_bars.extend(part)
        prev_start = part[0][0]
        if len(part) < 800:
            break

    rows = [
        {
            "date": pd.Timestamp(b[0]),
            "o": float(b[1]),
            "c": float(b[2]),
            "h": float(b[3]),
            "l": float(b[4]),
            "v": float(b[5]),
        }
        for b in reversed(all_bars)
    ]
    return pd.DataFrame(rows).sort_values("date").drop_duplicates("date").reset_index(drop=True)


_PREDICT_FEATURES = [
    "ret1", "ret5", "ret10", "ret20", "ret60",
    "ma5_dev", "ma10_dev", "ma20_dev", "ma60_dev",
    "vol20", "rsi14", "vchg5", "vprice", "pos20",
]
_PREDICT_CACHE: Dict[str, Dict[str, Any]] = {}


def _build_predict_features(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    c, h, l, v = d["c"], d["h"], d["l"], d["v"]
    d["ret1"] = c.pct_change(1)
    d["ret5"] = c.pct_change(5)
    d["ret10"] = c.pct_change(10)
    d["ret20"] = c.pct_change(20)
    d["ret60"] = c.pct_change(60)
    for w in (5, 10, 20, 60):
        ma = c.rolling(w).mean()
        d[f"ma{w}_dev"] = (c - ma) / ma
    d["vol20"] = d["ret1"].rolling(20).std()
    delta = c.diff()
    up = delta.clip(lower=0)
    dn = -delta.clip(upper=0)
    rs = up.rolling(14).mean() / (dn.rolling(14).mean() + 1e-12)
    d["rsi14"] = 100 - 100 / (1 + rs)
    d["vchg5"] = v.pct_change(5)
    d["vprice"] = v.rolling(5).mean() / (c * 1e4 + 1e-9)
    d["pos20"] = (c - l.rolling(20).max()) / (h.rolling(20).max() - l.rolling(20).min() + 1e-9) + 0.5
    d["fwd5"] = c.shift(-5) / c - 1.0
    return d


def _walk_forward_accuracy(X: pd.DataFrame, y: pd.Series, train_size: int, step: int = 5) -> Tuple[float, int, float]:
    from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    from sklearn.preprocessing import StandardScaler

    preds, trues = [], []
    Xv, yv = X.values, y.values
    rf = RandomForestClassifier(
        n_estimators=150, max_depth=5, min_samples_leaf=20,
        random_state=42, n_jobs=-1, class_weight="balanced_subsample",
    )
    gb = GradientBoostingClassifier(n_estimators=100, max_depth=2, learning_rate=0.05, random_state=42)
    i = train_size
    while i < len(y) - 5:
        ix = np.arange(i - train_size, i)
        if yv[ix].std() == 0:
            i += step
            continue
        sc = StandardScaler().fit(Xv[ix])
        Xt = sc.transform(Xv[ix])
        Xp = sc.transform(Xv[i : i + 1])
        for m in (rf, gb):
            m.fit(Xt, yv[ix])
        p = 0.5 * rf.predict_proba(Xp)[0, 1] + 0.5 * gb.predict_proba(Xp)[0, 1]
        preds.append(1 if p >= 0.5 else 0)
        trues.append(yv[i])
        i += step
    if not trues:
        return 0.0, 0, 0.0
    acc = float(np.mean(np.array(preds) == np.array(trues)))
    pos = float(np.mean(np.array(trues)))
    return acc, len(trues), pos


def _predict_symbol(code: str, force: bool = False) -> Dict[str, Any]:
    target = _to_exchange_code(code)
    mkt, c = _clean_code(code)
    symbol_code = f"{mkt}{c}"

    if not force and target in _PREDICT_CACHE:
        return _PREDICT_CACHE[target]

    df = _fetch_klines_extended(symbol_code)
    if len(df) < 300:
        result = {
            "code": target,
            "status": "error",
            "message": f"数据不足（仅 {len(df)} 根），无法训练",
        }
        return result

    f = _build_predict_features(df)
    last_close = float(f["c"].iloc[-1])
    last_date = str(f["date"].iloc[-1].date())

    model_df = f.dropna(subset=_PREDICT_FEATURES).reset_index(drop=True)
    X = model_df[_PREDICT_FEATURES].reset_index(drop=True)
    cut = len(f) - len(model_df)
    y_a = ((f["fwd5"] > 0).astype(int)).iloc[cut:].reset_index(drop=True)

    train_size = int(len(X) * 0.7)
    acc, n, _pos_rate = _walk_forward_accuracy(X, y_a, train_size=train_size, step=5)

    from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    from sklearn.preprocessing import StandardScaler

    rf = RandomForestClassifier(
        n_estimators=500, max_depth=5, min_samples_leaf=20,
        random_state=42, n_jobs=-1, class_weight="balanced_subsample",
    )
    gb = GradientBoostingClassifier(n_estimators=250, max_depth=2, learning_rate=0.05, random_state=42)
    sc = StandardScaler().fit(X.values)
    Xt = sc.transform(X.values)
    Xlast = sc.transform(X.iloc[-1:].values)
    rf.fit(Xt, y_a.values)
    gb.fit(Xt, y_a.values)
    p_up = 0.5 * rf.predict_proba(Xlast)[0, 1] + 0.5 * gb.predict_proba(Xlast)[0, 1]

    verdict = "偏多" if p_up >= 0.55 else ("偏空" if p_up <= 0.45 else "方向不明")
    summary = (
        f"{target}: 最新收盘 {last_close:.2f}（{last_date}），未来5日上涨概率 {p_up:.1%}，"
        f"OOS准确率 {acc:.1%}（{n}点）→ {verdict}"
    )
    result = {
        "code": target,
        "status": "success",
        "last_close": round(last_close, 2),
        "last_date": last_date,
        "up_probability": round(p_up, 4),
        "oos_accuracy": round(acc, 4),
        "oos_samples": n,
        "verdict": verdict,
        "summary": summary,
        "disclaimer": "统计方向信号，非投资建议",
    }
    _PREDICT_CACHE[target] = result
    return result


def _get_dsa_cookie() -> Optional[str]:
    """Obtain session cookie from local DSA server if auth is enabled."""
    global _session_cookie
    if _session_cookie:
        return _session_cookie

    try:
        url = f"{DSA_BASE_URL}/api/v1/auth/login"
        payload = json.dumps({"password": DSA_PASSWORD}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=4) as res:
            cookie_header = res.headers.get("Set-Cookie", "")
            if "dsa_session=" in cookie_header:
                for part in cookie_header.split(";"):
                    part = part.strip()
                    if part.startswith("dsa_session="):
                        _session_cookie = part.split("=")[1]
                        return _session_cookie
    except Exception as e:
        logger.debug(f"DSA auth login bypass/error: {e}")
    return None


# ==========================================
# Tool 1: 智能选股 (Screening)
# ==========================================
@mcp.tool()
def screen_stocks(
    strategy: str = "bull_momentum",
    market_cap_min_yi: float = 50.0,
    market_cap_max_yi: float = 50000.0,
    pe_min: float = 0.0,
    pe_max: float = 120.0,
    price_min: float = 3.0,
    price_max: float = 500.0,
    turnover_min: float = 1.0,
    top_n: int = 10,
) -> Dict[str, Any]:
    """
    全市场量化智能选股（覆盖 A 股 5200+ 标的，秒级扫描，免 Token）。

    Args:
        strategy: 选股策略:
            - 'bull_momentum': 多头突破动量（均线多头、换手活跃、放量突破、涨幅稳健，默认）
            - 'low_valuation_value': 低估值白马/高股息（PE<25, PB<2.8, 市值>150亿, 稳健防御）
            - 'volume_breakout': 放量异动启动（量比>1.4, 换手>2%, 当日涨幅2.5%~8.5%）
            - 'growth_tech': 科技成长高弹性（成长龙头，适度估值，高换手）
            - 'oversold_rebound': 超跌反弹潜伏（低位企稳，今日温和放量回升）
        market_cap_min_yi: 最低总市值（亿元），默认 50
        market_cap_max_yi: 最高总市值（亿元），默认 50000
        pe_min: 最低 PE(TTM)，默认 0 (排除亏损股)
        pe_max: 最高 PE(TTM)，默认 120
        price_min: 最低股价（元），默认 3.0 (排除退市仙股)
        price_max: 最高股价（元），默认 500.0
        turnover_min: 最低换手率%，默认 1.0%
        top_n: 返回前 N 只最优质股票，默认 10
    """
    all_stocks = _get_a_share_pool()
    if not all_stocks:
        return {"error": "Failed to load A-share pool", "results": []}

    quotes = _fetch_batch_quotes(all_stocks)
    if not quotes:
        return {"error": "Failed to fetch realtime quotes", "results": []}

    candidates = []
    for q in quotes:
        if "ST" in q["name"] or "退" in q["name"]:
            continue
        if not (price_min <= q["price"] <= price_max):
            continue
        if not (market_cap_min_yi <= q["mkt_cap_yi"] <= market_cap_max_yi):
            continue
        if not (pe_min <= q["pe_ttm"] <= pe_max):
            continue
        if q["turnover"] < turnover_min:
            continue
        candidates.append(q)

    scored_candidates = []
    if strategy == "bull_momentum":
        for c in candidates:
            if 1.5 <= c["pct_chg"] <= 9.5 and c["turnover"] >= 1.5:
                score = (c["pct_chg"] * 4.0) + min(c["turnover"] * 2.0, 20.0) + (100.0 / (c["pe_ttm"] + 10)) * 2.0
                scored_candidates.append({**c, "score": round(score, 1), "reason": f"涨幅{c['pct_chg']}%且换手{c['turnover']}%活跃"})
    elif strategy == "low_valuation_value":
        for c in candidates:
            if 0 < c["pe_ttm"] <= 25.0 and 0 < c["pb"] <= 2.8 and c["mkt_cap_yi"] >= 150.0:
                score = (30.0 - c["pe_ttm"]) * 2.0 + (3.0 - c["pb"]) * 10.0 + min(c["mkt_cap_yi"] / 500.0, 20.0)
                scored_candidates.append({**c, "score": round(score, 1), "reason": f"低PE({c['pe_ttm']})低PB({c['pb']})大市值龙头"})
    elif strategy == "volume_breakout":
        for c in candidates:
            if c["vol_ratio"] >= 1.4 and 2.5 <= c["pct_chg"] <= 8.5 and c["turnover"] >= 2.0:
                score = (c["vol_ratio"] * 15.0) + (c["pct_chg"] * 3.0) + (c["turnover"] * 1.5)
                scored_candidates.append({**c, "score": round(score, 1), "reason": f"量比{c['vol_ratio']}显著放大，涨幅{c['pct_chg']}%"})
    elif strategy == "growth_tech":
        for c in candidates:
            if 80.0 <= c["mkt_cap_yi"] <= 3000.0 and 2.0 <= c["turnover"] <= 15.0 and c["pct_chg"] > 0:
                score = (c["pct_chg"] * 3.5) + (c["turnover"] * 2.5) + (150.0 / (c["pe_ttm"] + 15))
                scored_candidates.append({**c, "score": round(score, 1), "reason": f"高弹性成长股，换手{c['turnover']}%, 涨幅{c['pct_chg']}%"})
    elif strategy == "oversold_rebound":
        for c in candidates:
            if 0.5 <= c["pct_chg"] <= 4.5 and c["turnover"] >= 1.2:
                score = (5.0 - abs(c["pct_chg"] - 2.5)) * 5.0 + c["turnover"] * 2.0 + (100.0 / (c["pe_ttm"] + 10))
                scored_candidates.append({**c, "score": round(score, 1), "reason": f"低位温和放量企稳，涨幅{c['pct_chg']}%"})
    else:
        for c in candidates:
            score = c["pct_chg"] * 3.0 + c["turnover"] * 2.0
            scored_candidates.append({**c, "score": round(score, 1), "reason": "满足基础量化过滤条件"})

    scored_candidates.sort(key=lambda x: x.get("score", 0), reverse=True)
    top_candidates = scored_candidates[:top_n]

    final_results = []
    for item in top_candidates:
        klines = _fetch_kline(item["code"], count=30)
        ma_info = {}
        if len(klines) >= 20:
            closes = [k["close"] for k in klines]
            ma5 = sum(closes[-5:]) / 5.0
            ma10 = sum(closes[-10:]) / 10.0
            ma20 = sum(closes[-20:]) / 20.0
            ma_trend = "多头排列(MA5>MA10>MA20)" if ma5 > ma10 > ma20 else "震荡/整理"
            ma_info = {
                "ma5": round(ma5, 2),
                "ma10": round(ma10, 2),
                "ma20": round(ma20, 2),
                "ma_trend": ma_trend,
            }

        final_results.append(
            {
                "code": item["code"],
                "name": item["name"],
                "price": item["price"],
                "pct_chg": f"{item['pct_chg']}%",
                "turnover": f"{item['turnover']}%",
                "pe_ttm": item["pe_ttm"],
                "pb": item["pb"],
                "mkt_cap_yi": f"{item['mkt_cap_yi']}亿",
                "vol_ratio": item.get("vol_ratio", 1.0),
                "score": item.get("score", 0),
                "signal_reason": item.get("reason", ""),
                **ma_info,
            }
        )

    return {
        "status": "success",
        "strategy": strategy,
        "universe_count": len(all_stocks),
        "filtered_count": len(candidates),
        "matched_count": len(scored_candidates),
        "top_stocks": final_results,
    }


# ==========================================
# Tool 2: 问股票 (Stock QA & Technical Diagnosis)
# ==========================================
@mcp.tool()
def ask_stock(stock_code_or_name: str) -> Dict[str, Any]:
    """
    实时查询单只股票的实时行情数据、量价关系、均线多空形态、RSI 与 20日支撑/压力位。

    Args:
        stock_code_or_name: 股票代码（如 '600519', '000001', '300750'）或名称（如 '贵州茅台', '宁德时代'）
    """
    target = stock_code_or_name.strip()
    code = None
    name = None

    if not (target.isdigit() or target.startswith("sh") or target.startswith("sz")):
        all_stocks = _get_a_share_pool()
        for s in all_stocks:
            if target in s["name"]:
                code = s["code"]
                name = s["name"]
                break
        if not code:
            return {"error": f"未能找到与 '{target}' 匹配的A股股票代码，请提供6位股票代码"}
    else:
        mkt, code = _clean_code(target)

    mkt, c = _clean_code(code)
    quotes = _fetch_batch_quotes([{"code": c, "market": mkt, "name": name or c}])
    if not quotes:
        return {"error": f"获取股票 {code} 实时行情失败"}
    quote = quotes[0]

    klines = _fetch_kline(c, count=60)
    diagnosis = {}
    if len(klines) >= 20:
        closes = [k["close"] for k in klines]
        ma5 = round(sum(closes[-5:]) / 5.0, 2)
        ma10 = round(sum(closes[-10:]) / 10.0, 2)
        ma20 = round(sum(closes[-20:]) / 20.0, 2)
        ma60 = round(sum(closes[-60:]) / len(closes[-60:]), 2) if len(closes) >= 30 else None

        cur_p = quote["price"]
        trend_label = "强势多头" if cur_p > ma5 > ma10 > ma20 else ("弱势空头" if cur_p < ma5 < ma10 < ma20 else "震荡整理")

        if len(closes) >= 15:
            diffs = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
            recent_diffs = diffs[-14:]
            gains = [d for d in recent_diffs if d > 0]
            losses = [-d for d in recent_diffs if d < 0]
            avg_gain = sum(gains) / 14.0 if gains else 0.0001
            avg_loss = sum(losses) / 14.0 if losses else 0.0001
            rs = avg_gain / avg_loss
            rsi14 = round(100 - (100 / (1 + rs)), 1)
        else:
            rsi14 = 50.0

        rsi_state = "超买预警" if rsi14 >= 80 else ("超跌反弹区" if rsi14 <= 25 else "合理区间")
        recent_high_20 = max(closes[-20:])
        recent_low_20 = min(closes[-20:])

        diagnosis = {
            "ma5": ma5,
            "ma10": ma10,
            "ma20": ma20,
            "ma60": ma60,
            "trend": trend_label,
            "rsi14": rsi14,
            "rsi_state": rsi_state,
            "support_level_20d": recent_low_20,
            "pressure_level_20d": recent_high_20,
        }

    return {
        "status": "success",
        "code": quote["code"],
        "name": quote["name"],
        "price": quote["price"],
        "pct_chg": f"{quote['pct_chg']}%",
        "open": quote["open"],
        "high": quote["high"],
        "low": quote["low"],
        "prev_close": quote["prev_close"],
        "turnover": f"{quote['turnover']}%",
        "pe_ttm": quote["pe_ttm"],
        "pb": quote["pb"],
        "mkt_cap_yi": f"{quote['mkt_cap_yi']}亿",
        "vol_ratio": quote.get("vol_ratio", 1.0),
        "technical_diagnosis": diagnosis,
        "summary": f"{quote['name']}({quote['code']}) 当前价 {quote['price']}元，涨跌幅 {quote['pct_chg']}%，形态呈现【{diagnosis.get('trend', '正常')}】，RSI(14)={diagnosis.get('rsi14', 50)}处于【{diagnosis.get('rsi_state', '正常')}】。",
    }


# ==========================================
# Tool 3: 策略历史回测 (Backtest)
# ==========================================
@mcp.tool()
def backtest_strategy(
    stock_code: str,
    strategy: str = "sma_cross",
    lookback_bars: int = 120,
    initial_cash: float = 100000.0,
) -> Dict[str, Any]:
    """
    对个股进行历史日 K 线的量化交易策略回测，输出总收益、Alpha 超额、最大回撤与胜率。

    Args:
        stock_code: 股票代码（如 '600519', '300750'）
        strategy: 回测策略:
            - 'sma_cross': 双均线金叉策略（MA5上穿MA20全仓买入，下穿卖出）
            - 'momentum_breakout': 动量突破策略（创20日新高买入，跌破10日均线止损）
            - 'rsi_mean_reversion': RSI均值回归策略（RSI<30超卖买入，RSI>70超买卖出）
        lookback_bars: 回测历史K线根数（默认 120 根，约半年~大半年交易日，最大 200）
        initial_cash: 初始资金（默认 100,000 元）
    """
    mkt, c = _clean_code(stock_code)
    lookback_bars = min(max(lookback_bars, 30), 200)
    klines = _fetch_kline(c, count=lookback_bars)
    if len(klines) < 30:
        return {"error": f"股票 {stock_code} 历史K线不足（仅{len(klines)}根），无法完成回测"}

    cash = initial_cash
    shares = 0
    trades = []
    equity_curve = []
    peak_equity = initial_cash
    max_drawdown = 0.0

    closes = [k["close"] for k in klines]
    dates = [k["date"] for k in klines]

    ma5 = [sum(closes[max(0, i - 4) : i + 1]) / len(closes[max(0, i - 4) : i + 1]) for i in range(len(closes))]
    ma10 = [sum(closes[max(0, i - 9) : i + 1]) / len(closes[max(0, i - 9) : i + 1]) for i in range(len(closes))]
    ma20 = [sum(closes[max(0, i - 19) : i + 1]) / len(closes[max(0, i - 19) : i + 1]) for i in range(len(closes))]

    rsi = [50.0] * len(closes)
    for i in range(14, len(closes)):
        diffs = [closes[j] - closes[j - 1] for j in range(i - 13, i + 1)]
        gains = [d for d in diffs if d > 0]
        losses = [-d for d in diffs if d < 0]
        avg_g = sum(gains) / 14.0 if gains else 0.0001
        avg_l = sum(losses) / 14.0 if losses else 0.0001
        rs = avg_g / avg_l
        rsi[i] = 100 - (100 / (1 + rs))

    start_idx = 20
    winning_trades = 0
    total_round_trips = 0
    last_buy_price = 0.0

    for i in range(start_idx, len(klines)):
        dt = dates[i]
        price = closes[i]
        buy_signal = False
        sell_signal = False

        if strategy == "sma_cross":
            if ma5[i - 1] <= ma20[i - 1] and ma5[i] > ma20[i]:
                buy_signal = True
            elif ma5[i - 1] >= ma20[i - 1] and ma5[i] < ma20[i]:
                sell_signal = True
        elif strategy == "momentum_breakout":
            high_20 = max(closes[i - 20 : i])
            if price > high_20 and price > ma20[i]:
                buy_signal = True
            elif price < ma10[i]:
                sell_signal = True
        elif strategy == "rsi_mean_reversion":
            if rsi[i] < 32 and price > ma5[i]:
                buy_signal = True
            elif rsi[i] > 68 or price < ma20[i] * 0.96:
                sell_signal = True

        if buy_signal and shares == 0 and cash > price * 100:
            buy_shares = int((cash * 0.95) // (price * 100)) * 100
            if buy_shares > 0:
                cost = buy_shares * price * 1.0003
                cash -= cost
                shares = buy_shares
                last_buy_price = price
                trades.append({"date": dt, "action": "BUY", "price": price, "shares": buy_shares, "cash_left": round(cash, 2)})

        elif sell_signal and shares > 0:
            revenue = shares * price * 0.9987
            cash -= revenue
            pnl = (price - last_buy_price) / last_buy_price * 100
            if pnl > 0:
                winning_trades += 1
            total_round_trips += 1
            trades.append(
                {
                    "date": dt,
                    "action": "SELL",
                    "price": price,
                    "shares": shares,
                    "pnl_pct": f"{round(pnl, 2)}%",
                    "cash_after": round(cash, 2),
                }
            )
            shares = 0

        current_equity = cash + (shares * price)
        if current_equity > peak_equity:
            peak_equity = current_equity
        dd = (peak_equity - current_equity) / peak_equity * 100.0
        if dd > max_drawdown:
            max_drawdown = dd
        equity_curve.append({"date": dt, "equity": round(current_equity, 2)})

    final_price = closes[-1]
    final_equity = cash + (shares * final_price)
    total_return_pct = (final_equity - initial_cash) / initial_cash * 100.0

    bench_initial_price = closes[start_idx]
    bench_return_pct = (final_price - bench_initial_price) / bench_initial_price * 100.0
    win_rate = (winning_trades / total_round_trips * 100.0) if total_round_trips > 0 else 0.0

    return {
        "status": "success",
        "stock_code": c,
        "strategy": strategy,
        "start_date": dates[start_idx],
        "end_date": dates[-1],
        "total_trading_days": len(dates) - start_idx,
        "initial_capital": initial_cash,
        "final_capital": round(final_equity, 2),
        "total_return": f"{round(total_return_pct, 2)}%",
        "benchmark_buy_and_hold_return": f"{round(bench_return_pct, 2)}%",
        "alpha": f"{round(total_return_pct - bench_return_pct, 2)}%",
        "max_drawdown": f"{round(max_drawdown, 2)}%",
        "win_rate": f"{round(win_rate, 1)}%",
        "total_trades": total_round_trips,
        "recent_trades": trades[-8:],
        "summary": f"回测区间 {dates[start_idx]} ~ {dates[-1]}，策略总收益率【{round(total_return_pct, 2)}%】（基准买入持有【{round(bench_return_pct, 2)}%】），Alpha 超额收益【{round(total_return_pct - bench_return_pct, 2)}%】，最大回撤【{round(max_drawdown, 2)}%】，交易胜率【{round(win_rate, 1)}%】。",
    }


# ==========================================
# Tool 4: 宏观大盘与复盘 (Market Review)
# ==========================================
@mcp.tool()
def get_market_review() -> Dict[str, Any]:
    """
    获取 A 股大盘宏观行情与全市场复盘数据（上证指数、深证成指、创业板指、科创50、沪深300点位与成交额、全市场涨跌统计与多空情绪）。
    """
    index_symbols = [
        {"code": "000001", "name": "上证指数", "market": "sh"},
        {"code": "399001", "name": "深证成指", "market": "sz"},
        {"code": "399006", "name": "创业板指", "market": "sz"},
        {"code": "000300", "name": "沪深300", "market": "sh"},
        {"code": "000688", "name": "科创50", "market": "sh"},
    ]
    quotes = _fetch_batch_quotes(index_symbols)
    total_amount_yi = sum(q.get("amount_wan", 0) / 10000.0 for q in quotes if q["code"] in ["000001", "399001"])

    indices_data = []
    for q in quotes:
        indices_data.append(
            {
                "name": q["name"],
                "code": q["code"],
                "price": q["price"],
                "pct_chg": f"{q['pct_chg']}%",
                "amount_yi": f"{round(q.get('amount_wan', 0) / 10000.0, 1)}亿",
            }
        )

    # Sample market breadth using top stocks
    sample_pool = _get_a_share_pool()[:200]
    sample_quotes = _fetch_batch_quotes(sample_pool)
    up_count = sum(1 for q in sample_quotes if q.get("pct_chg", 0) > 0)
    down_count = sum(1 for q in sample_quotes if q.get("pct_chg", 0) < 0)
    flat_count = len(sample_quotes) - up_count - down_count

    sentiment = "多头强势" if up_count > down_count * 1.5 else ("空头偏弱" if down_count > up_count * 1.5 else "震荡分化")

    return {
        "status": "success",
        "market_sentiment": sentiment,
        "sh_sz_total_amount_yi": f"{round(total_amount_yi, 1)}亿",
        "indices": indices_data,
        "market_breadth_sample": {
            "sample_size": len(sample_quotes),
            "up_count": up_count,
            "down_count": down_count,
            "flat_count": flat_count,
        },
        "summary": f"A股主要指数呈现【{sentiment}】，沪深两市合计成交约【{round(total_amount_yi, 1)}亿元】。样本个股上涨 {up_count} 家，下跌 {down_count} 家。",
    }


# ==========================================
# Tool 5: 自选股与持仓管理 (Portfolio & Watchlist)
# ==========================================
@mcp.tool()
def manage_portfolio(
    action: str = "list_all",
    target_type: str = "watchlist",
    stock_code: Optional[str] = None,
    cost_price: Optional[float] = None,
    shares: Optional[int] = None,
    group_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    管理本地自选股与持仓组合，并实时计算最新盈亏与市值。

    Args:
        action: 操作类型:
            - 'list_all': 查看所有自选股与持仓明细（含最新实时价格与盈亏计算）
            - 'add_watchlist': 添加股票到自选列表 (需 stock_code)
            - 'remove_watchlist': 从自选列表中移除 (需 stock_code)
            - 'add_position': 添加/更新持仓 (需 stock_code, cost_price, shares)
            - 'remove_position': 移除/清仓持仓 (需 stock_code)
        target_type: 'watchlist' (自选) 或 'position' (持仓)
        stock_code: 股票代码（如 '600519' 或 '000001'）
        cost_price: 持仓成本价（元）
        shares: 持仓股数（股）
        group_name: 分组名称（可选，默认 '默认自选' / '默认持仓'）
    """
    _init_portfolio_db()
    with sqlite3.connect(PORTFOLIO_DB_PATH) as conn:
        cursor = conn.cursor()

        if action == "add_watchlist" and stock_code:
            mkt, c = _clean_code(stock_code)
            q = _fetch_batch_quotes([{"code": c, "market": mkt, "name": c}])
            name = q[0]["name"] if q else c
            grp = group_name or "默认自选"
            cursor.execute(
                "INSERT OR REPLACE INTO watchlist (code, name, group_name) VALUES (?, ?, ?)",
                (c, name, grp),
            )
            conn.commit()
            return {"status": "success", "message": f"已成功添加 {name}({c}) 到自选分组【{grp}】"}

        elif action == "remove_watchlist" and stock_code:
            mkt, c = _clean_code(stock_code)
            cursor.execute("DELETE FROM watchlist WHERE code = ?", (c,))
            conn.commit()
            return {"status": "success", "message": f"已从自选股中移除 {c}"}

        elif action == "add_position" and stock_code:
            if cost_price is None or shares is None:
                return {"status": "error", "message": "添加持仓必须提供 cost_price (成本价) 和 shares (股数)"}
            mkt, c = _clean_code(stock_code)
            q = _fetch_batch_quotes([{"code": c, "market": mkt, "name": c}])
            name = q[0]["name"] if q else c
            grp = group_name or "默认持仓"
            cursor.execute(
                "INSERT OR REPLACE INTO positions (code, name, cost_price, shares, group_name) VALUES (?, ?, ?, ?, ?)",
                (c, name, cost_price, shares, grp),
            )
            conn.commit()
            return {"status": "success", "message": f"已成功记录持仓 {name}({c}): 成本 {cost_price}元, 数量 {shares}股"}

        elif action == "remove_position" and stock_code:
            mkt, c = _clean_code(stock_code)
            cursor.execute("DELETE FROM positions WHERE code = ?", (c,))
            conn.commit()
            return {"status": "success", "message": f"已成功清空持仓 {c}"}

        else:
            # list_all
            cursor.execute("SELECT code, name, group_name, added_at FROM watchlist")
            wl_rows = cursor.fetchall()
            cursor.execute("SELECT code, name, cost_price, shares, group_name, updated_at FROM positions")
            pos_rows = cursor.fetchall()

            # Batch fetch latest quotes for watchlist & positions
            all_codes = list(set([r[0] for r in wl_rows] + [r[0] for r in pos_rows]))
            quote_map = {}
            if all_codes:
                q_list = [{"code": c, "market": "sh" if c.startswith("6") else "sz", "name": c} for c in all_codes]
                live_quotes = _fetch_batch_quotes(q_list)
                quote_map = {q["code"]: q for q in live_quotes}

            watchlist_res = []
            for r in wl_rows:
                code, name, grp, added_at = r
                lq = quote_map.get(code, {})
                watchlist_res.append(
                    {
                        "code": code,
                        "name": lq.get("name", name),
                        "price": lq.get("price", 0.0),
                        "pct_chg": f"{lq.get('pct_chg', 0.0)}%",
                        "pe_ttm": lq.get("pe_ttm", 0.0),
                        "group": grp,
                    }
                )

            positions_res = []
            total_market_val = 0.0
            total_cost_val = 0.0
            for r in pos_rows:
                code, name, cost_p, num_shares, grp, updated_at = r
                lq = quote_map.get(code, {})
                cur_p = lq.get("price", cost_p)
                mkt_val = cur_p * num_shares
                cost_val = cost_p * num_shares
                pnl_val = mkt_val - cost_val
                pnl_pct = (pnl_val / cost_val * 100.0) if cost_val > 0 else 0.0

                total_market_val += mkt_val
                total_cost_val += cost_val

                positions_res.append(
                    {
                        "code": code,
                        "name": lq.get("name", name),
                        "cost_price": cost_p,
                        "current_price": cur_p,
                        "shares": num_shares,
                        "market_value": round(mkt_val, 2),
                        "pnl_amount": round(pnl_val, 2),
                        "pnl_pct": f"{round(pnl_pct, 2)}%",
                        "group": grp,
                    }
                )

            total_pnl = total_market_val - total_cost_val
            total_pnl_pct = (total_pnl / total_cost_val * 100.0) if total_cost_val > 0 else 0.0

            return {
                "status": "success",
                "watchlist_count": len(watchlist_res),
                "watchlist": watchlist_res,
                "positions_count": len(positions_res),
                "portfolio_summary": {
                    "total_market_value": round(total_market_val, 2),
                    "total_cost_value": round(total_cost_val, 2),
                    "total_pnl_amount": round(total_pnl, 2),
                    "total_pnl_pct": f"{round(total_pnl_pct, 2)}%",
                },
                "positions": positions_res,
            }


# ==========================================
# Tool 6: 价格与异动预警规则 (Alerts)
# ==========================================
@mcp.tool()
def manage_alerts(
    action: str = "list",
    stock_code: Optional[str] = None,
    rule_type: str = "price_above",
    threshold: Optional[float] = None,
    rule_id: Optional[int] = None,
) -> Dict[str, Any]:
    """
    管理股票价格监控与异动提醒规则（突破压力位预警、跌破止损位预警、涨跌幅异动监控）。

    Args:
        action: 'list' (查看当前所有预警及触发状态), 'create' (新增监控规则), 'delete' (删除规则)
        stock_code: 股票代码（如 '600519'）
        rule_type: 规则类型:
            - 'price_above': 股价突破/高于某价格
            - 'price_below': 股价跌破/低于某价格
            - 'pct_chg_above': 当日涨幅超过某百分比（如 5.0 代表涨超5%）
            - 'pct_chg_below': 当日跌幅超过某百分比（如 -4.0 代表跌超4%）
        threshold: 触发数值阈值
        rule_id: 规则 ID（删除时需要）
    """
    _init_portfolio_db()
    with sqlite3.connect(PORTFOLIO_DB_PATH) as conn:
        cursor = conn.cursor()

        if action == "create" and stock_code and threshold is not None:
            mkt, c = _clean_code(stock_code)
            q = _fetch_batch_quotes([{"code": c, "market": mkt, "name": c}])
            name = q[0]["name"] if q else c
            cursor.execute(
                "INSERT INTO alert_rules (code, name, rule_type, threshold, status) VALUES (?, ?, ?, ?, 'active')",
                (c, name, rule_type, threshold),
            )
            conn.commit()
            return {"status": "success", "message": f"已成功为 {name}({c}) 创建预警规则：当【{rule_type} {threshold}】时触发提醒"}

        elif action == "delete" and rule_id:
            cursor.execute("DELETE FROM alert_rules WHERE id = ?", (rule_id,))
            conn.commit()
            return {"status": "success", "message": f"已删除规则 ID {rule_id}"}

        else:
            # list and evaluate
            cursor.execute("SELECT id, code, name, rule_type, threshold, status, created_at FROM alert_rules")
            rows = cursor.fetchall()
            if not rows:
                return {"status": "success", "count": 0, "alerts": []}

            codes = list(set([r[1] for r in rows]))
            q_list = [{"code": c, "market": "sh" if c.startswith("6") else "sz", "name": c} for c in codes]
            live_quotes = _fetch_batch_quotes(q_list)
            q_map = {q["code"]: q for q in live_quotes}

            results = []
            for r in rows:
                rid, c, name, rtype, thresh, st, created = r
                lq = q_map.get(c, {})
                cur_p = lq.get("price", 0.0)
                cur_pct = lq.get("pct_chg", 0.0)

                triggered = False
                trigger_msg = ""
                if rtype == "price_above" and cur_p >= thresh:
                    triggered = True
                    trigger_msg = f"当前价 {cur_p} 已突破设定目标价 {thresh}"
                elif rtype == "price_below" and cur_p <= thresh:
                    triggered = True
                    trigger_msg = f"当前价 {cur_p} 已跌破设定止损价 {thresh}"
                elif rtype == "pct_chg_above" and cur_pct >= thresh:
                    triggered = True
                    trigger_msg = f"当前涨幅 {cur_pct}% 已超过设定阈值 {thresh}%"
                elif rtype == "pct_chg_below" and cur_pct <= thresh:
                    triggered = True
                    trigger_msg = f"当前跌幅 {cur_pct}% 已跌超设定阈值 {thresh}%"

                results.append(
                    {
                        "id": rid,
                        "code": c,
                        "name": lq.get("name", name),
                        "rule_type": rtype,
                        "threshold": thresh,
                        "current_price": cur_p,
                        "current_pct_chg": f"{cur_pct}%",
                        "triggered": triggered,
                        "trigger_message": trigger_msg if triggered else "未触发 (监控中)",
                    }
                )

            return {"status": "success", "count": len(results), "alerts": results}


# ==========================================
# Tool 7: 深度 AI 投研报告与问股 (Deep AI Analysis)
# ==========================================
@mcp.tool()
def generate_ai_report(
    stock_code: str,
    report_type: str = "detailed",
    async_mode: bool = False,
) -> Dict[str, Any]:
    """
    触发本地 DSA 大模型投研分析引擎，生成深度个股研究决策报告（包含基本面评分、风险排查、操作战术点位与核心逻辑）。

    Args:
        stock_code: 股票代码（如 '600519', 'AAPL', 'hk00700'）
        report_type: 报告类型 ('detailed' 完整深度报告, 'simple' 简版, 'brief' 摘要)
        async_mode: 是否异步提交。若为 True 则立即返回 task_id；若为 False 则同步等待完成（通常需 1~3 分钟）。
    """
    mkt, c = _clean_code(stock_code)
    code = stock_code.strip()
    if not (code.startswith("hk") or code.isupper()):
        code = c

    cookie = _get_dsa_cookie()
    headers = {"Content-Type": "application/json"}
    if cookie:
        headers["Cookie"] = f"dsa_session={cookie}"

    url = f"{DSA_BASE_URL}/api/v1/analysis/analyze"
    payload = json.dumps(
        {
            "stock_code": code,
            "report_type": report_type,
            "force_refresh": False,
            "async_mode": async_mode,
        }
    ).encode("utf-8")

    try:
        req = urllib.request.Request(url, data=payload, headers=headers)
        timeout = 10 if async_mode else 300
        with urllib.request.urlopen(req, timeout=timeout) as res:
            data = json.loads(res.read().decode("utf-8"))
            return {"status": "success", "result": data}
    except Exception as e:
        logger.error(f"Failed to trigger AI report: {e}")
        return {
            "status": "error",
            "message": f"触发本地 DSA AI 分析失败: {e}。请确认本地 dsa-webui 服务（端口 8000）是否正常运行。",
        }


# ==========================================
# Tool 8: ML 短期方向预测 (Walk-forward RF+GB)
# ==========================================
@mcp.tool()
def predict_stock(codes: List[str], force: bool = False) -> Dict[str, Any]:
    """
    基于严格 walk-forward 机器学习的 A 股未来 5 个交易日方向预测（RandomForest + GradientBoosting 集成）。

    Args:
        codes: 股票代码列表，支持 '600519'、'600519.SH'、'sh600519' 等格式
        force: 是否强制重新拉取数据并训练（默认 False，同代码命中内存缓存）

    Returns:
        每只股票的上涨概率、样本外准确率与方向判断。首次训练约 1-2 分钟/股。
        输出为统计信号，非投资建议。
    """
    results = []
    for code in codes:
        try:
            results.append(_predict_symbol(code, force=force))
        except Exception as exc:
            target = _to_exchange_code(code)
            results.append({
                "code": target,
                "status": "error",
                "message": f"预测失败: {type(exc).__name__}: {exc}",
            })
    ok = [r for r in results if r.get("status") == "success"]
    return {
        "status": "success" if ok else "error",
        "count": len(results),
        "predictions": results,
        "summary": "\n".join(r.get("summary", r.get("message", "")) for r in results),
        "disclaimer": "统计方向信号，非投资建议（OOS 准确率通常约 55-60%）",
    }


@mcp.tool()
def predict_cache_status() -> Dict[str, Any]:
    """查看当前已缓存的 ML 预测结果（无网络请求）。"""
    if not _PREDICT_CACHE:
        return {"status": "success", "cached_count": 0, "cached": []}
    cached = [
        {"code": k, "verdict": v.get("verdict"), "up_probability": v.get("up_probability"), "summary": v.get("summary")}
        for k, v in _PREDICT_CACHE.items()
    ]
    return {"status": "success", "cached_count": len(cached), "cached": cached}


# ==========================================
# Tool 9: 策略清单
# ==========================================
@mcp.tool()
def get_strategies() -> Dict[str, Any]:
    """获取所有支持的选股与回测策略清单及说明。"""
    return {
        "screening_strategies": [
            {"id": "bull_momentum", "name": "多头突破动量策略", "desc": "均线多头、换手充分、量价齐升主升浪"},
            {"id": "low_valuation_value", "name": "低估值价值/高股息策略", "desc": "低PE/PB、大市值稳健白马资产"},
            {"id": "volume_breakout", "name": "量比异动突破策略", "desc": "量比明显放大、主力进场起涨点"},
            {"id": "growth_tech", "name": "科技成长高弹性龙头策略", "desc": "科技成长中盘龙头，高弹性"},
            {"id": "oversold_rebound", "name": "超跌反弹低吸策略", "desc": "底部温和放量企稳修复"},
        ],
        "backtest_strategies": [
            {"id": "sma_cross", "name": "双均线金叉策略 (MA5/MA20)", "desc": "经典顺势均线交叉，金叉买入死叉卖出"},
            {"id": "momentum_breakout", "name": "动量突破策略 (20日新高)", "desc": "突破20日最高价进场，跌破10日线离场"},
            {"id": "rsi_mean_reversion", "name": "RSI 均值回归策略", "desc": "RSI超卖低吸，RSI超买止盈"},
        ],
    }


if __name__ == "__main__":
    mcp.run()
