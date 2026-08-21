#!/usr/bin/env python3
"""DRT Self-Improving Agent — x402_signal.py (premium)
Fetch live signal/bias/news fra x402-API (pay-per-call).
Eksempel:
  export X402_API_KEY=...
  python3 x402_signal.py --endpoint signals --symbol BTCUSD
  python3 x402_signal.py --endpoint bias --symbol SP500
  python3 x402_signal.py --endpoint market
  python3 x402_signal.py --endpoint news
"""
import argparse, json, os, sys, urllib.request, urllib.error

BASE = os.environ.get("X402_BASE", "https://186.240.156.169:8791")
KEY = os.environ.get("X402_API_KEY", "")
ALLOW_HTTP = os.environ.get("X402_ALLOW_HTTP", "") == "1"

ENDPOINTS = {
    "signals": "/v1/signals",
    "market": "/v1/market",
    "bias": "/v1/bias",
    "news": "/v1/news",
    "sentiment": "/v1/sentiment",
    "backtest": "/v1/backtest",
}

def main():
    _check_secure()
    p = argparse.ArgumentParser(description="x402 premium-signaler")
    p.add_argument("--endpoint", required=True, choices=ENDPOINTS.keys())
    p.add_argument("--symbol", default=None)
    p.add_argument("--params", default="", help="ekstra ?key=value&...")
    a = p.parse_args()

    if not KEY:
        print("❌ Set X402_API_KEY (fås på https://github.com/MohamedAbdisamed/x402-api)")
        sys.exit(1)

    url = BASE + ENDPOINTS[a.endpoint]
    qs = []
    if a.symbol:
        qs.append(f"symbol={a.symbol}")
    if a.params:
        qs.append(a.params)
    if qs:
        url += "?" + "&".join(qs)

    req = urllib.request.Request(url, headers={"x-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
            print(json.dumps(data, indent=2, ensure_ascii=False))
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300]
        print(f"❌ HTTP {e.code}: {body}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
