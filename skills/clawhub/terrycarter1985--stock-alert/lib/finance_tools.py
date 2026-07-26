"""Finance skill tools for stock prices and financial data.

Resilient design:
- Paths are resolved relative to this file (portable across environments),
  with an optional STOCK_ALERT_DATA_DIR override.
- Live quotes use yfinance when available; on any failure (network, rate
  limit / HTTP 429, missing dependency) we fall back to the bundled local
  CSV snapshot so downstream callers always get a well-formed dict.
"""
import os
from pathlib import Path
from typing import Dict, Optional

import pandas as pd

try:
    import yfinance as yf
    _HAS_YF = True
except Exception:  # pragma: no cover - dependency optional at runtime
    yf = None
    _HAS_YF = False


def _data_dir() -> Path:
    """Resolve the data directory in a portable way."""
    env = os.environ.get("STOCK_ALERT_DATA_DIR")
    if env:
        return Path(env)
    here = Path(__file__).resolve().parent
    # Look for a sibling/ancestor `data/` folder (skill bundle or workspace).
    for base in (here, here.parent, here.parent.parent):
        candidate = base / "data"
        if (candidate / "nasdaq_stock_prices.csv").exists():
            return candidate
    return here / "data"


def _local_quote(symbol: str) -> Optional[Dict]:
    """Build a quote dict from the local NASDAQ CSV snapshot."""
    csv_path = _data_dir() / "nasdaq_stock_prices.csv"
    try:
        df = pd.read_csv(csv_path)
    except Exception:
        return None
    df.columns = [c.strip() for c in df.columns]
    sym_col = "company symbol" if "company symbol" in df.columns else df.columns[0]
    row = df[df[sym_col].astype(str).str.upper() == symbol.upper()]
    if row.empty:
        return None
    r = row.iloc[0]
    close = float(r.get("close")) if pd.notna(r.get("close")) else "N/A"
    high = r.get("high")
    low = r.get("low")
    # Approximate intraday change% from (close - midpoint)/midpoint when possible.
    change_percent = "N/A"
    try:
        mid = (float(high) + float(low)) / 2.0
        if mid:
            change_percent = round((float(close) - mid) / mid * 100, 2)
    except Exception:
        pass
    return {
        "symbol": symbol,
        "name": str(r.get("company name", symbol)),
        "current_price": close,
        "currency": "USD",
        "market_cap": "N/A",
        "change_percent": change_percent,
        "source": "local_csv",
    }


def get_stock_price(symbol: str) -> Dict:
    """Get current stock price; falls back to local CSV on any failure."""
    if _HAS_YF:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info or {}
            price = info.get("regularMarketPrice", info.get("currentPrice"))
            if price is not None:
                return {
                    "symbol": symbol,
                    "name": info.get("longName", symbol),
                    "current_price": price,
                    "currency": info.get("currency", "USD"),
                    "market_cap": info.get("marketCap", "N/A"),
                    "change_percent": info.get("regularMarketChangePercent", "N/A"),
                    "source": "yfinance",
                }
        except Exception:
            pass  # fall through to local snapshot
    local = _local_quote(symbol)
    if local is not None:
        return local
    return {"error": f"no data for {symbol} (live fetch failed and no local snapshot)"}


def get_historical_prices(symbol: str, period: str = "1mo") -> pd.DataFrame:
    """Get historical price data for a stock (requires yfinance + network)."""
    if not _HAS_YF:
        raise RuntimeError("yfinance not installed")
    try:
        return yf.Ticker(symbol).history(period=period)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch historical data: {e}")


def get_company_financials(symbol: str) -> Dict:
    """Get key financial metrics for a company (live, best effort)."""
    if not _HAS_YF:
        return {"error": "yfinance not installed"}
    try:
        info = yf.Ticker(symbol).info or {}
        return {
            "symbol": symbol,
            "name": info.get("longName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "forward_pe": info.get("forwardPE", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "beta": info.get("beta", "N/A"),
            "profit_margins": info.get("profitMargins", "N/A"),
            "return_on_equity": info.get("returnOnEquity", "N/A"),
        }
    except Exception as e:
        return {"error": str(e)}


def load_sp500_data() -> pd.DataFrame:
    """Load local S&P 500 financial dataset."""
    return pd.read_csv(_data_dir() / "sp500_financials.csv")


def load_nasdaq_sample_data() -> pd.DataFrame:
    """Load local NASDAQ sample stock dataset."""
    return pd.read_csv(_data_dir() / "nasdaq_stock_prices.csv")
