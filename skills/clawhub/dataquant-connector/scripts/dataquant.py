#!/usr/bin/env python3
"""DataQuant API CLI wrapper.

Commands (each maps 1:1 to a backend endpoint in backend/routers/markets.py):
  kline   GET /{market}/klines/{symbol}        single-symbol daily OHLCV
  batch   GET /{market}/klines                  multi-symbol; symbols= comma list
  detail  GET /{market}/detail/{symbol} | /{market}/detail
  screen  GET /{market}/screen                 filter latest snapshots
  search  GET /{market}/symbols                substring match on symbol CODE (not name)
  macro   GET /macro                           gdp / cpi_ppi / pmi
  quota   GET /quota                           plan + daily quota usage

Parameter names/defaults mirror the backend exactly (see frontend/api-docs.html).
"""
import argparse, json, os, re, sys

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://api.dataquant.trade"


def get_api_key(args_key=None):
    key = args_key or os.environ.get("DATAQUANT_API_KEY", "")
    if not key:
        print("Error: API Key required. Set DATAQUANT_API_KEY env var or pass --api-key.", file=sys.stderr)
        sys.exit(1)
    return key


def _request(endpoint, params=None, api_key=None):
    key = api_key or get_api_key()
    url = f"{BASE_URL}{endpoint}"
    resp = requests.get(url, params=params, headers={"X-API-Key": key}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def cmd_kline(args):
    params = {}
    if args.start: params["start"] = args.start
    if args.end: params["end"] = args.end
    if args.fields: params["fields"] = args.fields
    if args.limit: params["limit"] = args.limit
    if args.offset: params["offset"] = args.offset
    if args.adj: params["adj"] = args.adj
    data = _request(f"/{args.market}/klines/{args.symbol}", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_batch(args):
    params = {"symbols": args.symbols}
    if args.date: params["date"] = args.date
    if args.start: params["start"] = args.start
    if args.end: params["end"] = args.end
    if args.fields: params["fields"] = args.fields
    if args.limit: params["limit"] = args.limit
    if args.offset: params["offset"] = args.offset
    if args.adj: params["adj"] = args.adj
    data = _request(f"/{args.market}/klines", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_detail(args):
    sym_list = [s.strip() for s in args.symbols.split(",") if s.strip()]
    if len(sym_list) == 1:
        params = {}
        if args.fields: params["fields"] = args.fields
        data = _request(f"/{args.market}/detail/{sym_list[0]}", params, args.api_key)
    else:
        params = {"symbols": args.symbols}
        if args.fields: params["fields"] = args.fields
        data = _request(f"/{args.market}/detail", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


# Screen filter whitelist — MUST stay in sync with backend config.DETAIL_FILTERABLE.
# The CLI forwards any --min-<col>/--max-<col>; unknown columns are silently ignored
# by the backend, so keeping this list accurate helps the AI pick valid filters.
SCREEN_FILTERABLE = {
    "pe_ratio", "pe_lyr", "pb_ratio", "dividend_ratio_ttm", "eps_ttm",
    "total_market_cap", "circulating_market_cap", "total_shares", "float_shares",
    "turnover_rate", "volume_ratio", "range_pct",
    "change_percent", "chg_5d", "chg_10d", "chg_20d", "chg_60d", "chg_ytd",
    "close_vs_ma20", "close_vs_52w_high", "ma5", "ma10", "ma20", "ma60",
    "high_52week", "low_52week", "volume", "amount", "open", "high", "low", "close",
}


def cmd_screen(args):
    params = {}
    # Generic min_*/max_* handler — covers all whitelisted filters plus any future additions
    for key, val in vars(args).items():
        if val is None:
            continue
        if key.startswith("min_") or key.startswith("max_"):
            params[key] = val
    if args.sort: params["sort"] = args.sort
    if args.order: params["order"] = args.order
    if args.limit: params["limit"] = args.limit
    if args.offset: params["offset"] = args.offset
    data = _request(f"/{args.market}/screen", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_search(args):
    params = {}
    if args.query: params["search"] = args.query
    if args.limit: params["limit"] = args.limit
    if args.offset: params["offset"] = args.offset
    data = _request(f"/{args.market}/symbols", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_quota(args):
    data = _request("/quota", api_key=args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_macro(args):
    params = {}
    if args.indicator: params["indicator"] = args.indicator
    if args.start: params["start"] = args.start
    if args.end: params["end"] = args.end
    if args.limit: params["limit"] = args.limit
    if args.offset: params["offset"] = args.offset
    data = _request("/macro", params, args.api_key)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="DataQuant API CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("kline", help="Single-symbol K-line")
    p.add_argument("market", choices=["ashare","hkstock","usstock","crypto","indices","etfs"])
    p.add_argument("symbol", help="e.g. sh600519")
    p.add_argument("--start"); p.add_argument("--end"); p.add_argument("--fields")
    p.add_argument("--adj", choices=["bfq","qfq","hfq"], default="bfq",
                   help="复权方式: bfq不复权(默认), qfq前复权, hfq后复权")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_kline)

    p = sub.add_parser("batch", help="Multi-symbol K-line")
    p.add_argument("market", choices=["ashare","hkstock","usstock","crypto","indices","etfs"])
    p.add_argument("symbols", help="Comma-separated")
    p.add_argument("--date", help="指定日期 YYYY-MM-DD（与 start/end 互斥）")
    p.add_argument("--start"); p.add_argument("--end"); p.add_argument("--fields")
    p.add_argument("--adj", choices=["bfq","qfq","hfq"], default="bfq",
                   help="复权方式: bfq不复权(默认), qfq前复权, hfq后复权")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_batch)

    p = sub.add_parser("detail", help="Latest snapshot (single or batch)")
    p.add_argument("market", choices=["ashare","hkstock","usstock","crypto","indices","etfs"])
    p.add_argument("symbols", help="e.g. sh600519 or sh600519,sz000858")
    p.add_argument("--fields", help="Columns, e.g. pe_ratio,pb_ratio,chg_20d")
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_detail)

    p = sub.add_parser("screen", help="Filter latest snapshots by criteria")
    p.add_argument("market", choices=["ashare","hkstock","usstock","crypto","indices","etfs"])
    # Filter: any --min-<col> / --max-<col>, type=float. Whitelist = config.DETAIL_FILTERABLE.
    p.add_argument("--sort", default="change_percent",
                   help="Sort column (default: change_percent). Must be in filter whitelist.")
    p.add_argument("--order", choices=["asc","desc"], default="desc")
    p.add_argument("--limit", type=int, default=50); p.add_argument("--offset", type=int, default=0)
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_screen, _screen_extra=True)

    p = sub.add_parser("search", help="Search symbols by CODE substring (not name)")
    p.add_argument("market", choices=["ashare","hkstock","usstock","crypto","indices","etfs"])
    p.add_argument("query", nargs="?")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("quota", help="Query API quota")
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_quota)

    p = sub.add_parser("macro", help="Macroeconomic data")
    p.add_argument("indicator", nargs="?", choices=["gdp","cpi_ppi","pmi"])
    p.add_argument("--start"); p.add_argument("--end")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--api-key", help="DataQuant API key")
    p.set_defaults(func=cmd_macro)

    args, extra = parser.parse_known_args()
    # Inject dynamic --min-* / --max-* screen filters into args namespace
    if getattr(args, "_screen_extra", False):
        i = 0
        while i < len(extra):
            a = extra[i]
            # Format: --min-xx=val or --max-xx=val
            m = re.match(r'--(min-[a-z0-9_-]+|max-[a-z0-9_-]+)=(.*)', a)
            if m:
                try:
                    setattr(args, m.group(1).replace("-", "_"), float(m.group(2)))
                except ValueError:
                    print(f"Warning: skipping non-numeric value for --{m.group(1)}", file=sys.stderr)
                i += 1
                continue
            # Format: --min-xx val or --max-xx val (space-separated)
            m2 = re.match(r'--(min-[a-z0-9_-]+|max-[a-z0-9_-]+)$', a)
            if m2 and i + 1 < len(extra) and not extra[i + 1].startswith("--"):
                try:
                    setattr(args, m2.group(1).replace("-", "_"), float(extra[i + 1]))
                except ValueError:
                    print(f"Warning: skipping non-numeric value for --{m2.group(1)}", file=sys.stderr)
                i += 2
                continue
            i += 1
    args.func(args)


if __name__ == "__main__":
    main()
