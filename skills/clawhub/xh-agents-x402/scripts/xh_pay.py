#!/usr/bin/env python3
"""xh_pay.py — pembayar x402 minimal untuk katalog XH Agents (dipakai skill ClawHub + MCP server).

Dua mode:
  quote  : baca 402 challenge sebuah resource, laporkan harga/jaringan/payTo. TIDAK butuh kunci.
  pay    : bayar resource itu (USDC di Base) lalu kembalikan isi produk + bukti settlement.

Aturan keselamatan yang dipaksakan kode ini:
  * kunci pembayar hanya dibaca dari env XH_PAYER_KEY atau file XH_PAYER_KEY_FILE (mode 600) —
    tidak pernah dicetak, tidak pernah ditulis ulang ke disk.
  * ada PLAFON harga (--max, default $0.10): kalau challenge meminta lebih, pembayaran DIBATALKAN.
  * cetak alamat pembayar + saldo USDC sebelum membayar, supaya tidak ada pembayaran buta.

Contoh:
  python3 xh_pay.py quote https://xhagents.xyz/api/x402-trust
  python3 xh_pay.py pay https://xhagents.xyz/api/x402-trust --body '{"url":"https://example.com"}'
  python3 xh_pay.py catalogue
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

UA = "xh-pay/1.0 (+https://xhagents.xyz)"
DEFAULT_MAX = 0.10
USDC_BASE = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
NETWORK = "eip155:8453"


def _key() -> str | None:
    k = os.environ.get("XH_PAYER_KEY")
    if k:
        return k.strip()
    path = os.environ.get("XH_PAYER_KEY_FILE")
    if path and os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#"):
                return line.split("=")[-1].strip().strip('"').strip("'")
    return None


def _signer(key: str):
    from eth_account import Account
    from x402.mechanisms.evm.signers import EthAccountSigner
    acct = Account.from_key(key)
    return acct, EthAccountSigner(acct)


def usdc_balance(addr: str) -> float | None:
    data = "0x70a08231" + addr[2:].rjust(64, "0")
    for rpc in ("https://1rpc.io/base", "https://base.drpc.org", "https://mainnet.base.org"):
        try:
            body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "eth_call",
                               "params": [{"to": USDC_BASE, "data": data}, "latest"]}).encode()
            req = urllib.request.Request(rpc, data=body, headers={"User-Agent": "Mozilla/5.0",
                                                                  "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                res = json.loads(r.read().decode()).get("result")
            if isinstance(res, str) and res.startswith("0x"):
                return int(res, 16) / 1e6
        except Exception:  # noqa: BLE001
            continue
    return None


def _get(obj, key, default=None):
    """Ambil field dari dict ATAU objek pydantic (SDK x402 mengembalikan objek)."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _dict(obj) -> dict:
    """Normalisasi objek pydantic / dict menjadi dict biasa."""
    if obj is None:
        return {}
    for attr in ("model_dump", "dict"):
        fn = getattr(obj, attr, None)
        if callable(fn):
            try:
                return fn()
            except Exception:  # noqa: BLE001
                pass
    return obj if isinstance(obj, dict) else {}


def describe(required) -> dict:
    """Ringkas challenge: harga, jaringan, payTo, aset, skema."""
    out = {"price_usdc": None, "network": None, "payTo": None, "asset": None, "scheme": None,
           "resource": None}
    root = _dict(required)
    _res = root.get("resource")
    if _res is not None:
        out["resource"] = str(_dict(_res).get("url") or _res)
    accepts = root.get("accepts") or []
    a = (_dict(accepts[0]) if accepts else root)
    amt = a.get("maxAmountRequired") or a.get("amount")
    try:
        out["price_usdc"] = round(int(amt) / 1e6, 6) if amt else None
    except Exception:  # noqa: BLE001
        out["price_usdc"] = None
    for f in ("network", "payTo", "asset", "scheme"):
        v = a.get(f)
        out[f] = str(v) if v is not None else None
    out["asset_name"] = _dict(a.get("extra")).get("name")
    return out


def challenge(url: str, method: str = "GET", body: dict | None = None):
    """Request tanpa bayar. Kembalikan (status, objek PaymentRequired|None, header mentah, body)."""
    from x402.http import decode_payment_required_header
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method.upper(),
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, None, None, r.read(4000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        raw = e.read(4000).decode("utf-8", "replace")
        hdr = e.headers.get("PAYMENT-REQUIRED") or e.headers.get("payment-required")
        obj = None
        if hdr:
            try:
                obj = decode_payment_required_header(hdr)
            except Exception:  # noqa: BLE001
                try:
                    obj = json.loads(base64.b64decode(hdr + "=" * (-len(hdr) % 4)).decode())
                except Exception:  # noqa: BLE001
                    obj = None
        if obj is None and raw.strip().startswith("{"):
            try:
                obj = json.loads(raw)
            except Exception:  # noqa: BLE001
                obj = None
        return e.code, obj, hdr, raw


def catalogue() -> list[dict]:
    req = urllib.request.Request("https://xhagents.xyz/openapi.json", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        doc = json.loads(r.read().decode())
    rows = []
    for path, methods in (doc.get("paths") or {}).items():
        for m, spec in methods.items():
            if m.lower() not in ("get", "post") or not isinstance(spec, dict) or not spec.get("security"):
                continue
            rows.append({"path": path, "method": m.upper(),
                         "summary": (spec.get("summary") or spec.get("description") or "")[:120]})
    return sorted(rows, key=lambda r: r["path"])


def pay(url: str, method: str = "POST", body: dict | None = None, max_price: float = DEFAULT_MAX,
        show: int = 1500) -> dict:
    """Bayar resource dan kembalikan isi produk + bukti settlement."""
    key = _key()
    if not key:
        return {"ok": False, "error": "tidak ada kunci pembayar (set XH_PAYER_KEY atau XH_PAYER_KEY_FILE)"}
    from x402.client import x402ClientSync
    from x402.http import (x402HTTPClientSync, decode_payment_response_header,
                           encode_payment_signature_header)
    from x402.mechanisms.evm.exact import register_exact_evm_client

    acct, signer = _signer(key)
    status, required, _hdr, raw = challenge(url, method, body)
    if status != 402 or required is None:
        return {"ok": status == 200, "status": status, "payer": acct.address,
                "note": "tidak ada challenge 402 yang bisa dibaca", "body": raw[:show]}
    info = describe(required)
    if info["price_usdc"] is None or info["price_usdc"] > max_price:
        return {"ok": False, "payer": acct.address,
                "error": f"harga {info['price_usdc']} di atas plafon {max_price} — dibatalkan", "quote": info}

    inner = x402ClientSync()
    register_exact_evm_client(inner, signer, [NETWORK])
    hc = x402HTTPClientSync(inner)
    payload = hc.create_payment_payload(required)
    sig = encode_payment_signature_header(payload)

    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method.upper(),
                                 headers={"X-PAYMENT": sig, "PAYMENT-SIGNATURE": sig, "User-Agent": UA,
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            txt = r.read(20000).decode("utf-8", "replace")
            proof = r.headers.get("PAYMENT-RESPONSE") or r.headers.get("payment-response")
            settled = None
            if proof:
                try:
                    settled = decode_payment_response_header(proof)
                except Exception:  # noqa: BLE001
                    settled = {"_raw": proof[:200]}
            return {"ok": True, "status": r.status, "payer": acct.address, "quote": info,
                    "settlement": settled, "body": txt[:show]}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "payer": acct.address, "quote": info,
                "error": e.read(400).decode("utf-8", "replace")}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["quote", "pay", "catalogue", "whoami"])
    ap.add_argument("url", nargs="?")
    ap.add_argument("--method", default=None)
    ap.add_argument("--body", default=None, help="JSON body untuk POST")
    ap.add_argument("--max", type=float, default=DEFAULT_MAX, help="plafon harga USDC")
    ap.add_argument("--show", type=int, default=1500)
    a = ap.parse_args()

    if a.action == "catalogue":
        for r in catalogue():
            print(f'  {r["method"]:<4} {r["path"]:<34} {r["summary"]}')
        return
    if a.action == "whoami":
        k = _key()
        if not k:
            print("tidak ada kunci pembayar di env/file")
            return
        acct, _ = _signer(k)
        print("alamat pembayar:", acct.address, "| saldo USDC:", usdc_balance(acct.address))
        return
    if not a.url:
        print("butuh URL", file=sys.stderr)
        sys.exit(2)
    method = (a.method or ("POST" if a.body else "GET")).upper()
    body = json.loads(a.body) if a.body else None
    if a.action == "quote":
        status, required, hdr, raw = challenge(a.url, method, body)
        print(f"HTTP {status}")
        print(json.dumps(describe(required) if required is not None else
                         {"_note": "tidak ada PAYMENT-REQUIRED", "_body": raw[:200]}, indent=1))
        return
    out = pay(a.url, method, body, a.max, a.show)
    print(json.dumps(out, indent=1)[:6000])


if __name__ == "__main__":
    main()
