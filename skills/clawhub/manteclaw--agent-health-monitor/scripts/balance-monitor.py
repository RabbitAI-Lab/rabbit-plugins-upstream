#!/usr/bin/env python3
"""
Balance Monitor
===============
Alert when a monitored wallet is low on gas.
Can be run as a cron job every 10 minutes.

Usage:
    python3 balance-monitor.py --alert-threshold 0.005
"""

import os
import sys
import argparse
import urllib.parse
from datetime import datetime
from web3 import Web3

# SECURITY (v1.0.1): the Alchemy key goes in the RPC URL path (Alchemy's
# design). It is URL-quoted so reserved characters cannot alter the path,
# and it is scrubbed out of any error text before printing — error strings
# from web3 can echo the request URL.
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY", "")

def _redact(text: str) -> str:
    return text.replace(ALCHEMY_API_KEY, "***") if ALCHEMY_API_KEY else text

W3 = Web3(Web3.HTTPProvider(
    f"https://base-mainnet.g.alchemy.com/v2/{urllib.parse.quote(ALCHEMY_API_KEY, safe='')}"
))

def _env_float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except (TypeError, ValueError):
        print(f"  ⚠️  Invalid {name} value; using default {default}")
        return default

THRESHOLD_ETH = _env_float("GAS_ALERT_THRESHOLD", 0.005)

def _checksum(addr: str) -> str:
    """Validate a configured wallet address; invalid ones are skipped, not fatal."""
    if not addr:
        return ""
    try:
        return Web3.to_checksum_address(addr)
    except Exception:
        print(f"  ⚠️  Invalid wallet address configured, skipping: {addr[:10]}...")
        return ""

WALLETS = {
    "Executor": _checksum(os.getenv("EXECUTOR_ADDRESS", "")),
    # Unconfigured extra wallets are skipped (empty default), not read as
    # the zero address: 0x000...000 is a valid address with a 0 balance,
    # so the old zero-address default reported two phantom LOW wallets
    # on every run with default config (v1.0.3 fix).
    "Bankr Primary": _checksum(os.getenv("WALLET_ADDRESS_1", "")),
    "Additional Wallet": _checksum(os.getenv("WALLET_ADDRESS_2", "")),
}

def check_balance(name: str, addr: str, threshold: float):
    if not addr:
        return True
    try:
        bal = W3.eth.get_balance(addr)
        bal_eth = float(W3.from_wei(bal, "ether"))
        status = "✅" if bal_eth >= threshold else "🔴 LOW"
        print(f"  {status} {name:20s} {addr[:10]}... {bal_eth:.6f} ETH")
        return bal_eth >= threshold
    except Exception as e:
        print(f"  ❌ {name:20s} {addr[:10]}... error: {_redact(str(e))[:80]}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=float, default=THRESHOLD_ETH, help="ETH threshold")
    args = parser.parse_args()

    print(f"⛽ Balance Monitor | {datetime.utcnow().isoformat()}")
    print(f"   Alert threshold: {args.threshold:.4f} ETH")
    print("─" * 55)

    all_ok = True
    for name, addr in WALLETS.items():
        if not check_balance(name, addr, args.threshold):
            all_ok = False

    print("─" * 55)
    if not all_ok:
        print("🔴 One or more wallets are low on gas!")
        sys.exit(1)
    print("✅ All wallets have sufficient gas.")
    sys.exit(0)
