#!/usr/bin/env python3
import argparse, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from x402_client import call
p = argparse.ArgumentParser()
p.add_argument("--symbol", default=None); p.add_argument("--limit", type=int, default=50)
a = p.parse_args()
data = call("/v1/market", {"symbol": a.symbol, "limit": a.limit} if a.symbol else {"limit": a.limit})
import json; print(json.dumps(data, indent=2, ensure_ascii=False))
