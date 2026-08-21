#!/usr/bin/env python3
"""x402 pay-per-call client — secure HTTPS connection.

Security:
- Default BASE is HTTPS. The API key is spending-capable (pays per call),
  so it is NEVER sent over plain HTTP unless X402_ALLOW_HTTP=1 is explicitly set.
- X402_BASE can be overridden (e.g. https://api.your-server.dk:8791).
"""
import json
import os
import sys
import ssl
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("X402_BASE", "https://show-zum-anyway-sanyo.trycloudflare.com")
KEY = os.environ.get("X402_API_KEY", "")
ALLOW_HTTP = os.environ.get("X402_ALLOW_HTTP", "") == "1"
_CA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "northcap-ca.pem")


def _ctx():
    if "https://show-zum-anyway-sanyo.trycloudflare.com" in BASE or "localhost" in BASE:
        return ssl.create_default_context(cafile=_CA)
    return ssl.create_default_context()


def call(endpoint, params=None, method="GET"):
    if not KEY:
        print("ERROR: Set X402_API_KEY (get it at https://github.com/MohamedAbdisamed/x402-api)")
        sys.exit(1)
    if BASE.startswith("http://") and not ALLOW_HTTP:
        print("ERROR: X402_BASE uses HTTP, but the API key is spending-capable.")
        print("   Use HTTPS (X402_BASE=https://...), or set X402_ALLOW_HTTP=1 consciously.")
        sys.exit(1)
    url = BASE.rstrip("/") + endpoint
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"x-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=20, context=_ctx()) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code}: {e.read().decode()[:200]}")
        sys.exit(1)
