#!/usr/bin/env python3
"""Simmer prediction-market heartbeat + opportunity scanner.

Logs portfolio state, expiring positions, high-volume markets, and flags
stale-priced candidates for review.

SCANNER IS LOG-ONLY. It places no trades. See scan_stale_priced() for why the
platform's own recommended_side is not used.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
LOG_DIR = WORKSPACE / "logs"
BASE_URL = "https://www.simmer.markets/api/sdk"

# Credentials have moved between locations before; first hit wins.
CREDS_CANDIDATES = [
    Path("/root/.simmer/credentials.json"),
    Path("/root/.openclaw/.simmer/credentials.json"),
    WORKSPACE / ".simmer/credentials.json",
]

# Stale-pricing screen. The edge with an actual track record (see
# memory/projects/simmer.md): the outside world has settled an outcome and the
# Simmer price has not caught up. external_price_yes is Polymarket's price.
EXTERNAL_SETTLED_LOW = 0.02   # external at/below this => crowd says NO
EXTERNAL_SETTLED_HIGH = 0.98  # external at/above this => crowd says YES
LOCAL_UNDECIDED_BAND = (0.05, 0.95)  # simmer price still meaningfully uncertain
MIN_GAP = 0.10  # ignore slivers

ECHO_STDOUT = False  # cron redirects stdout to this same log; avoid double lines


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{ts}] {msg}"
    if ECHO_STDOUT:
        print(line)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_DIR / "simmer-heartbeat.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def creds_path():
    for p in CREDS_CANDIDATES:
        if p.exists():
            return p
    return None


def api_request(method, path, body=None):
    cpath = creds_path()
    if cpath is None:
        raise RuntimeError(
            "simmer credentials not found in: "
            + ", ".join(str(p) for p in CREDS_CANDIDATES)
        )
    with open(cpath, "r", encoding="utf-8") as f:
        creds = json.load(f)
    api_key = creds.get("api_key") or creds.get("apiKey")
    if not api_key:
        raise RuntimeError(f"simmer api_key missing from {cpath}")

    url = f"{BASE_URL}{path}"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="ignore")
        try:
            err = json.loads(raw)
        except Exception:
            err = {"raw": raw}
        return {"error": err, "http_status": e.code}
    except Exception as e:
        return {"error": str(e)}


def scan_stale_priced(opportunities, held_ids):
    """Flag markets where the external crowd has settled but Simmer has not.

    Deliberately ignores the endpoint's own opportunity_score and
    recommended_side. As of 17/07/2026 opportunity_score is the constant 50.0 on
    every row, divergence does not reconcile with the adjacent price fields, and
    recommended_side was inverted on both markets whose real-world outcome was
    known (Muchova/Noskova and Borges/Dimitrov). Side is derived here from
    external_price_yes instead.
    """
    out = []
    for o in opportunities:
        if o.get("id") in held_ids:
            continue
        ext = o.get("external_price_yes")
        cur = o.get("current_probability")
        if ext is None or cur is None:
            continue
        if not (LOCAL_UNDECIDED_BAND[0] <= cur <= LOCAL_UNDECIDED_BAND[1]):
            continue
        if ext <= EXTERNAL_SETTLED_LOW:
            side, gap = "no", cur - ext
        elif ext >= EXTERNAL_SETTLED_HIGH:
            side, gap = "yes", ext - cur
        else:
            continue
        if gap < MIN_GAP:
            continue
        out.append({**o, "_side": side, "_gap": gap})
    out.sort(key=lambda x: x["_gap"], reverse=True)
    return out


def main():
    log("Simmer heartbeat starting")

    try:
        me = api_request("GET", "/agents/me")
    except RuntimeError as e:
        log(f"FATAL: {e}")
        return
    if me.get("error"):
        log(f"Failed to fetch agent: {me['error']}")
        return

    log(
        f"Balance: ${float(me['balance']):,.2f} SIM | "
        f"Total PnL: ${float(me['total_pnl']):,.2f} ({me['total_pnl_percent']}%) | "
        f"Trades: {me['trades_count']} | Win/Loss: {me['win_count']}/{me['loss_count']}"
    )

    positions = api_request("GET", "/positions")
    if positions.get("error"):
        log(f"Failed to fetch positions: {positions['error']}")
        return

    active = positions.get("positions", [])
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    expiring_soon = [p for p in active if str(p.get("resolves_at", "")).startswith(today)]
    log(f"Active positions: {len(active)} | Expiring today: {len(expiring_soon)}")
    for p in expiring_soon:
        log(
            f"  EXPIRING: {p['question'][:60]} | "
            f"side={'YES' if p['shares_yes'] else 'NO'} | "
            f"value=${float(p['current_value']):,.2f} | "
            f"pnl=${float(p['pnl']):,.2f}"
        )

    markets = api_request("GET", "/markets?limit=20&sort=volume_24h")
    if markets.get("error"):
        log(f"Failed to fetch markets: {markets['error']}")
    else:
        log("Top markets by 24h volume:")
        for m in markets.get("markets", [])[:5]:
            log(
                f"  {m['question'][:55]} | price:{m['current_price']:.3f} | "
                f"vol24h:${m.get('volume_24h',0)/1e6:.1f}M | ends:{str(m.get('resolves_at','?'))[:10]}"
            )

    opps = api_request("GET", "/markets/opportunities")
    if opps.get("error"):
        log(f"Failed to fetch opportunities: {opps['error']}")
    else:
        held = {p.get("market_id") for p in active}
        candidates = scan_stale_priced(opps.get("opportunities", []), held)
        log(f"REVIEW: {len(candidates)} stale-priced candidate(s) [log-only, no trades placed]")
        for c in candidates:
            log(
                f"  CANDIDATE: {c['question'][:55]} | suggest={c['_side'].upper()} | "
                f"simmer:{c['current_probability']:.3f} vs external:{c['external_price_yes']:.4f} | "
                f"gap:{c['_gap']:.3f} | ends:{str(c.get('resolves_at','?'))[:16]}"
            )

    log("Simmer heartbeat finished")


if __name__ == "__main__":
    main()
