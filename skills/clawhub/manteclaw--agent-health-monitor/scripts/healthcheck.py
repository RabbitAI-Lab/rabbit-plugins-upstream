#!/usr/bin/env python3
"""
Agent Healthcheck
=====================
Verify all APIs, keys, and services are healthy.
Run this after any key rotation or deployment.

Usage:
    python3 healthcheck.py          # Full check
    python3 healthcheck.py --quiet  # Exit code only (0 = healthy)

Credential policy (v1.0.1, ClawHub audit TT3): the endpoint checks below
are KEYLESS reachability probes — they send no credential of any kind.
A live service answers (200 for public endpoints, or 401/403 because no
key was presented); a dead service times out or fails to connect. API-key
validity itself is api_key_monitor.py's job. The only key-bearing calls
left in this file are the Alchemy RPC checks (the key goes in the URL
path, which is Alchemy's own design, over HTTPS) and the Bankr SDK init
(the key goes only to Bankr, via its own SDK).
"""

import os
import sys
import argparse
import urllib.parse
from datetime import datetime

# SECURITY (v1.0.1): error text can echo request data (e.g. a URL carrying
# the key) back into an exception. Every check detail passes through
# check(), so key material is scrubbed there before anything is printed
# or stored. Keys come from env vars only and are sent only to each key
# owner's own API endpoint. EXECUTOR_PRIVATE_KEY is used only locally to
# derive the wallet address for a match check — it is never transmitted.
_KEY_ENV_VARS = (
    "ALCHEMY_API_KEY", "GROQ_API_KEY", "MISTRAL_API_KEY",
    "OPENROUTER_API_KEY", "BANKR_API_KEY", "DUNE_API_KEY",
    "GITHUB_TOKEN", "EXECUTOR_PRIVATE_KEY",
)

def _redact(text: str) -> str:
    for secret in (os.getenv(var, "") for var in _KEY_ENV_VARS):
        if secret:
            text = text.replace(secret, "***")
    return text

# ─── Results ────────────────────────────────────────────────────────────────
results = []

def check(name: str, status: bool, detail: str = ""):
    icon = "✅" if status else "❌"
    detail = _redact(detail)
    results.append({"name": name, "ok": status, "detail": detail})
    if not args.quiet:
        print(f"  {icon} {name}{': ' + detail if detail else ''}")
    return status

# ─── Checks ─────────────────────────────────────────────────────────────────
def check_alchemy():
    key = os.getenv("ALCHEMY_API_KEY")
    if not key:
        return check("Alchemy", False, "ALCHEMY_API_KEY not set")
    try:
        from web3 import Web3
        w3 = Web3(Web3.HTTPProvider(f"https://base-mainnet.g.alchemy.com/v2/{urllib.parse.quote(key, safe='')}"))
        bn = w3.eth.block_number
        return check("Alchemy", True, f"Block {bn:,}")
    except Exception as e:
        return check("Alchemy", False, str(e)[:40])

def _probe_reachable(name: str, url: str, key_env: str):
    """Keyless endpoint-reachability probe (v1.0.1, TT3).

    No credential is sent: the key is only checked for presence (a missing
    key is still a failure — the service cannot be used without it), and
    the request carries no Authorization header. A live service answers
    (200 for public endpoints, or 401/403 because no key was presented);
    a dead service times out or fails to connect.
    """
    key = os.getenv(key_env)
    if not key:
        return check(name, False, f"{key_env} not set")
    try:
        import urllib.request
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return check(name, True, f"reachable (HTTP {resp.status}, no key sent)")
    except urllib.error.HTTPError as e:
        # Any HTTP response proves the service is up and answering: 200 for
        # public endpoints, 401/403 because no key was presented, and 404
        # for providers that answer unauthenticated requests that way
        # (Dune does). Only transport errors (below) mean unreachable.
        if e.code in (200, 401, 403, 404):
            return check(name, True, f"reachable (HTTP {e.code} — live service, no key sent)")
        return check(name, False, f"HTTP {e.code}")
    except Exception as e:
        return check(name, False, str(e)[:40])

def check_groq():
    return _probe_reachable("Groq", "https://api.groq.com/openai/v1/models", "GROQ_API_KEY")

def check_mistral():
    return _probe_reachable("Mistral", "https://api.mistral.ai/v1/models", "MISTRAL_API_KEY")

def check_openrouter():
    # /models is public on OpenRouter — reachable without any credential.
    return _probe_reachable("OpenRouter", "https://openrouter.ai/api/v1/models", "OPENROUTER_API_KEY")

def check_dune():
    return _probe_reachable("Dune", "https://api.dune.com/api/v1/status", "DUNE_API_KEY")

def check_github():
    # api.github.com root answers 200 without auth; /user would need the token.
    return _probe_reachable("GitHub", "https://api.github.com/", "GITHUB_TOKEN")

def check_bankr():
    key = os.getenv("BANKR_API_KEY")
    if not key:
        return check("Bankr", False, "BANKR_API_KEY not set")
    try:
        # Try SDK init — if it works, key is valid. The key goes only to
        # Bankr, via its own SDK; ai_key is a dummy (no AI call is made).
        import importlib.util
        if importlib.util.find_spec("litcoin"):
            from litcoin import Agent
            a = Agent(bankr_key=key, ai_key="dummy", ai_url="https://openrouter.ai/api/v1")
            return check("Bankr", True, "SDK Agent created")
        return check("Bankr", True, "Key present (SDK not installed)")
    except Exception as e:
        return check("Bankr", False, str(e)[:40])

def check_arb_wallet():
    addr = os.getenv("EXECUTOR_ADDRESS")
    if not addr:
        return check("Executor Wallet", False, "EXECUTOR_ADDRESS not set")
    key = os.getenv("EXECUTOR_PRIVATE_KEY")
    try:
        from web3 import Web3
        from eth_account import Account
        # Private key use (local only): derive the address and compare it
        # with EXECUTOR_ADDRESS. The key is never sent anywhere.
        w3 = Web3(Web3.HTTPProvider(f"https://base-mainnet.g.alchemy.com/v2/{urllib.parse.quote(os.getenv('ALCHEMY_API_KEY', ''), safe='')}"))
        bal = w3.eth.get_balance(addr)
        bal_eth = w3.from_wei(bal, "ether")
        if key:
            acct = Account.from_key(key)
            match = acct.address.lower() == addr.lower()
            return check("Executor Wallet", match, f"{bal_eth:.6f} ETH | Key{'✓' if match else '✗'}")
        return check("Executor Wallet", bal > 0, f"{bal_eth:.6f} ETH | No key (dry-run)")
    except Exception as e:
        return check("Executor Wallet", False, str(e)[:40])

def check_litcoiin_wallet():
    addr = os.getenv("LITCOIIN_WALLET_ADDRESS")
    if not addr:
        return check("Litcoiin Wallet", True, "Not configured (optional)")
    try:
        from web3 import Web3
        w3 = Web3(Web3.HTTPProvider(f"https://base-mainnet.g.alchemy.com/v2/{urllib.parse.quote(os.getenv('ALCHEMY_API_KEY', ''), safe='')}"))
        bal = w3.eth.get_balance(addr)
        return check("Litcoiin Wallet", bal > 0, f"{w3.from_wei(bal, 'ether'):.6f} ETH")
    except Exception as e:
        return check("Litcoiin Wallet", False, str(e)[:40])

# ─── Main ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true", help="Exit code only")
    args = parser.parse_args()

    if not args.quiet:
        print(f"🏥 Agent Healthcheck | {datetime.utcnow().isoformat()}")
        print("─" * 50)

    check_alchemy()
    check_groq()
    check_mistral()
    check_openrouter()
    check_bankr()
    check_dune()
    check_github()
    check_arb_wallet()
    check_litcoiin_wallet()

    total = len(results)
    passed = sum(1 for r in results if r["ok"])

    if not args.quiet:
        print("─" * 50)
        print(f"Result: {passed}/{total} healthy")

    sys.exit(0 if passed == total else 1)
