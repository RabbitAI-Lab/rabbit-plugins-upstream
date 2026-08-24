#!/usr/bin/env python3
import sys, json
sys.path.insert(0, __import__('os').path.dirname(__file__))
from x402_client import call
data = call("/v1/news")
print(json.dumps(data, indent=2, ensure_ascii=False))
