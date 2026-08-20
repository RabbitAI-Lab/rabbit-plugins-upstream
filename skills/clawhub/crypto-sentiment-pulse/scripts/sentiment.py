#!/usr/bin/env python3
"""Crypto sentiment — Fear & Greed via x402 pay-per-call.

⚠️ OPMÆRKSOMHED: dette script laver et BETALT eksternt API-kald (x402, USDC).
Det koster penge pr. kald — kør kun når du bevidst vil hente sentiment.
"""
import sys, json
sys.path.insert(0, __import__('os').path.dirname(__file__))
from x402_client import call

# 🔔 Tydelig disclosure: betalt kald (SkillSpector-fix 20/8)
print("⚠️ Udfører BETALT x402-kald (/v1/sentiment) — der trækkes på din nøgle.")
data = call("/v1/sentiment")
print(json.dumps(data, indent=2, ensure_ascii=False))
