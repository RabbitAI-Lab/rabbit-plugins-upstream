#!/usr/bin/env python3
"""x402 API template — Northcap (simplified).

⚠️ SECURITY (SkillSpector fix 20/8):
- Purchase only issues keys AFTER ON-CHAIN verification of the txHash
  (PAYMENT_RPC_URL, default: Base mainnet RPC). No verification = no key.
- If the RPC is unreachable, purchases are DENIED (secure-by-default).
TODO: replace YOUR /v1/... endpoints with your own data.
"""
import json, os, hmac, hashlib
from datetime import datetime, timezone
from pathlib import Path
from fastapi import FastAPI, Header, HTTPException, Query
import urllib.request

WALLET = "0x0000000000000000000000000000000000000000"  # TODO: your wallet
PRICE_PER_CALL = 0.005
PRICE_PER_MONTH = 25.0
KEYS_FILE = Path(__file__).parent / "api_keys.json"    # gitignore this!

# On-chain verification (Base mainnet RPC as default — no key without confirmed payment)
PAYMENT_RPC_URL = os.environ.get("PAYMENT_RPC_URL", "https://mainnet.base.org")
PAYMENT_CHAIN_ID = int(os.environ.get("PAYMENT_CHAIN_ID", "8453"))

app = FastAPI(title="My x402 API", version="1.0.1")


def load_keys():
    if KEYS_FILE.exists(): return json.loads(KEYS_FILE.read_text())
    return {}


def _rpc_call(method, params):
    """JSON-RPC call against PAYMENT_RPC_URL. Returns result or None."""
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(
        PAYMENT_RPC_URL, data=body,
        headers={"Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            return data.get("result")
    except Exception:
        return None


def verify_payment_onchain(tx_hash: str, expected_usd: float) -> tuple[bool, str]:
    """Verify that txHash is a real, confirmed payment to WALLET.

    Returns (ok, message). Secure-by-default: errors/unreachable RPC = not ok.
    """
    tx = _rpc_call("eth_getTransactionByHash", [tx_hash])
    if not tx:
        return False, "Transaction not found on chain"
    # Must go TO our wallet
    to = (tx.get("to") or "").lower()
    if to != WALLET.lower():
        return False, "Transaction does not go to the API owner's wallet"
    # Amount: value is in wei → convert to ETH/USDC (simplified; for USDC
    # check the Transfer event on the token contract via
    # eth_getTransactionReceipt + logs instead). Here we accept ETH value as minimum.
    try:
        value_eth = int(tx.get("value") or "0x0", 16) / 1e18
    except Exception:
        value_eth = 0.0
    if value_eth < expected_usd:  # simplified 1 ETH ≈ 1 USD check → replace with token logic
        return False, f"Amount too small ({value_eth:.6f} < {expected_usd})"
    receipt = _rpc_call("eth_getTransactionReceipt", [tx_hash])
    if not receipt or int(receipt.get("status") or "0x0", 16) != 1:
        return False, "Transaction is not confirmed (status != success)"
    return True, "Payment verified on-chain"


@app.get("/.well-known/x402")
@app.get("/x402-manifest")
def manifest():
    return {
        "name": "My API",
        "description": "Describe your service",
        "provider": {"name": "Your name", "wallet": WALLET, "chains": ["base"]},
        "payment": {"currency": "USDC", "networks": ["base"],
                    "pricePerCall": PRICE_PER_CALL, "pricePerMonth": PRICE_PER_MONTH,
                    "methods": ["onchain-usdc"]},
        "endpoints": {"signals": {"path": "/v1/signals", "method": "GET", "auth": "api-key"}},
    }


@app.post("/v1/purchase")
def purchase(req: dict):
    tx_hash = (req.get("txHash") or "").strip()
    amount = float(req.get("amountUsd") or 0)
    if not tx_hash.startswith("0x") or len(tx_hash) < 20:
        raise HTTPException(400, "Invalid txHash")
    if amount < PRICE_PER_CALL:
        raise HTTPException(400, f"Minimum ${PRICE_PER_CALL}")
    # 🔒 CRITICAL FIX (20/8): verify the payment ON-CHAIN before issuing a key.
    ok, msg = verify_payment_onchain(tx_hash, amount)
    if not ok:
        raise HTTPException(402, f"Payment could not be verified: {msg}")
    key = hmac.new(b"secret-salt", tx_hash.encode(), hashlib.sha256).hexdigest()[:24]
    keys = load_keys()
    keys[key] = {"tx": tx_hash, "amount": amount,
                 "kind": "monthly" if amount >= PRICE_PER_MONTH else "per-call",
                 "created": datetime.now(timezone.utc).isoformat(), "calls": 0}
    KEYS_FILE.write_text(json.dumps(keys, indent=2))
    return {"apiKey": key, "kind": "monthly" if amount >= PRICE_PER_MONTH else "per-call",
            "status": "verified"}


def _auth(x_api_key: str):
    keys = load_keys()
    k = keys.get(x_api_key or "")
    if not k: raise HTTPException(401, "Missing/invalid key")
    if k["kind"] == "per-call" and k["calls"] >= 1:
        raise HTTPException(402, "Call usage exhausted — buy more")
    k["calls"] += 1
    KEYS_FILE.write_text(json.dumps(keys, indent=2))
    return k


@app.get("/v1/signals")
def signals(x_api_key: str = Header(None), symbol: str = Query(None)):
    _auth(x_api_key)
    return {"provider": "My API", "symbol": symbol,
            "data": "YOUR DATA HERE"}  # TODO: your data
