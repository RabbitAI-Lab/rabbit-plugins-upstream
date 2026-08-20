#!/usr/bin/env python3
import argparse, sys, json
sys.path.insert(0, __import__('os').path.dirname(__file__))
from x402_client import call
p = argparse.ArgumentParser()
p.add_argument("--symbol", default="BTCUSD")
a = p.parse_args()
data = call("/v1/bias", {"symbol": a.symbol})
print(json.dumps(data, indent=2, ensure_ascii=False))
