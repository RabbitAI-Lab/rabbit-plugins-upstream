#!/usr/bin/env python3
"""x402 pay-per-call klient — sikker HTTPS-forbindelse.

🔒 SIKKERHED (SkillSpector-fix 20/8):
- API-nøglen er penge-kapacabel (betaler per kald) — sendes KUN over HTTPS.
- X402_BASE kan overskrives (fx https://api.din-server.dk:8791).
- HTTP kræver eksplicit X402_ALLOW_HTTP=1 (bevidst opt-in, kun lokalt/sikkert net).
"""
import json, os, sys, urllib.request, urllib.error, urllib.parse

BASE = os.environ.get("X402_BASE", "https://186.240.156.169:8791")
KEY = os.environ.get("X402_API_KEY", "")
ALLOW_HTTP = os.environ.get("X402_ALLOW_HTTP", "") == "1"


def call(endpoint, params=None, method="GET"):
    if not KEY:
        print("❌ Sæt X402_API_KEY (https://github.com/MohamedAbdisamed/x402-api)"); sys.exit(1)
    if BASE.startswith("http://") and not ALLOW_HTTP:
        print("❌ Sikkerhed: X402_BASE bruger HTTP, men API-nøglen er penge-kapacabel.")
        print("   Brug HTTPS (X402_BASE=https://...), eller sæt X402_ALLOW_HTTP=1 bevidst.")
        sys.exit(1)
    url = BASE.rstrip("/") + endpoint
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {KEY}"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {e.read().decode()[:200]}"); sys.exit(1)
