#!/usr/bin/env python3
"""Crypto sentiment — Fear & Greed via the x402 pay-per-call API.

⚠️ PAID API call: each run costs money (x402, USDC on Ethereum) and sends
your API key to the API. Run only when you consciously want sentiment data.
"""
import sys, json
sys.path.insert(0, __import__('os').path.dirname(__file__))
from x402_client import call

# 🔔 Explicit runtime disclosure before the paid call (SkillSpector fix 20/8)
print("⚠️ Executing PAID x402 call (/v1/sentiment) — charged to your key.")
data = call("/v1/sentiment")
print(json.dumps(data, indent=2, ensure_ascii=False))
