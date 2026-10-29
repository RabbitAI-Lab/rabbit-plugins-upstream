#!/usr/bin/env python3
"""Public-data-only hosting probe. No trading client, credentials, or mutations."""
import argparse
import asyncio
import hashlib
import json
import math
import os
from pathlib import Path
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
import uuid

from indicators import Bar, k14, signal

ROOT = Path(__file__).resolve().parent
HTTP_HOSTS = {"api.binance.com", "gamma-api.polymarket.com", "clob.polymarket.com"}
BINANCE_WS = "wss://stream.binance.com:9443/ws/btcusdt@trade"
PM_WS = "wss://ws-subscriptions-clob.polymarket.com/ws/market"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("HTTP redirects are disabled")


def public_get(url, params=None):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in HTTP_HOSTS or parsed.username or parsed.password:
        raise ValueError("Unapproved public endpoint")
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "K14-Observer/0.1.0"}, method="GET")
    started = time.monotonic()
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=8) as response:
        payload = response.read(2_000_001)
    if len(payload) > 2_000_000:
        raise ValueError("Public response too large")
    return json.loads(payload), (time.monotonic() - started) * 1000


def completed_bars(rows, window):
    if len(rows) != 14:
        raise ValueError("Exactly 14 completed candles required")
    bars = []
    for i, row in enumerate(rows):
        expected = window - (14 - i) * 900
        if int(row[0]) != expected * 1000 or int(row[6]) != (expected + 900) * 1000 - 1:
            raise ValueError("Candle timestamps do not match closed window")
        bars.append(Bar(expected, float(row[2]), float(row[3]), float(row[4])))
    k14(bars, window)  # Validate order, continuity, finite positive OHLC.
    return bars


def signal_snapshot(get=public_get):
    clock_start = time.monotonic()
    clock, clock_rtt = get("https://api.binance.com/api/v3/time")
    clock_end = time.monotonic()
    server_ms = int(clock["serverTime"])
    anchor = (clock_start + clock_end) / 2
    window = (server_ms // 900000) * 900
    rows, candles_rtt = get("https://api.binance.com/api/v3/klines", {
        "symbol": "BTCUSDT", "interval": "15m", "limit": 14,
        "startTime": (window - 14 * 900) * 1000, "endTime": window * 1000 - 1,
    })
    bars = completed_bars(rows, window)
    thresholds = json.loads((ROOT / "thresholds.json").read_text("utf-8"))
    if thresholds.get("provisional") is not False:
        raise ValueError("Unvalidated thresholds")
    value = k14(bars, window)
    side = signal(value, thresholds, window)
    age = (server_ms + (time.monotonic() - anchor) * 1000) / 1000 - window
    if age >= 900:
        raise ValueError("Window changed while fetching bars")
    report = {"window_start": window, "binance_server_ms": server_ms,
              "clock_rtt_ms": round(clock_rtt, 3), "candles_rtt_ms": round(candles_rtt, 3),
              "window_age_seconds": round(age, 3), "bars": [b.__dict__ for b in bars],
              "k14": value, "signal_candidate": side,
              "entry_time_gate": age < 120, "full_entry_evaluated": False,
              "threshold_month": thresholds["month"], "thresholds_sha256": hashlib.sha256(
                  (ROOT / "thresholds.json").read_bytes()).hexdigest()}
    return report, server_ms, anchor


def discover_market(window, get=public_get):
    slug = f"btc-updown-15m-{window}"
    markets, rtt = get("https://gamma-api.polymarket.com/markets", {"slug": slug})
    candidates = [m for m in markets if m.get("slug") == slug and not m.get("closed")]
    if len(candidates) != 1:
        raise ValueError("Matching active market unavailable")
    market = candidates[0]
    tokens, outcomes = market["clobTokenIds"], market["outcomes"]
    if isinstance(tokens, str): tokens = json.loads(tokens)
    if isinstance(outcomes, str): outcomes = json.loads(outcomes)
    if len(tokens) != 2 or len(set(tokens)) != 2 or set(outcomes) != {"Up", "Down"}:
        raise ValueError("Unexpected binary outcome mapping")
    return {"slug": slug, "tokens": dict(zip(outcomes, tokens)), "lookup_rtt_ms": round(rtt, 3)}


class State:
    def __init__(self, directory):
        directory.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(directory / "probe.sqlite", timeout=5)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.execute("CREATE TABLE IF NOT EXISTS checkpoint (id INTEGER PRIMARY KEY CHECK(id=1), payload TEXT)")
        self.db.commit()
        self.run_id = str(uuid.uuid4())
        self.payload = None

    def begin(self, now):
        self.db.execute("BEGIN IMMEDIATE")
        row = self.db.execute("SELECT payload FROM checkpoint WHERE id=1").fetchone()
        previous = json.loads(row[0]) if row else None
        if previous and previous["status"] == "RUNNING" and previous["lease_until"] > now:
            self.db.rollback()
            raise RuntimeError("OVERLAPPING_RUN_SAME_DATABASE")
        self.payload = {"run_id": self.run_id, "status": "RUNNING", "lease_until": now + 90,
                        "started_at": now, "checkpoints": 0, "orders_submitted": 0}
        self.db.execute("INSERT OR REPLACE INTO checkpoint VALUES(1, ?)", (json.dumps(self.payload),))
        self.db.commit()
        return previous

    def save(self, now, status="RUNNING"):
        self.db.execute("BEGIN IMMEDIATE")
        row = self.db.execute("SELECT payload FROM checkpoint WHERE id=1").fetchone()
        if not row or json.loads(row[0])["run_id"] != self.run_id:
            self.db.rollback()
            raise RuntimeError("LEASE_OWNERSHIP_LOST")
        self.payload.update(status=status, lease_until=now + 90 if status == "RUNNING" else now,
                            checkpoints=self.payload["checkpoints"] + 1)
        self.db.execute("UPDATE checkpoint SET payload=? WHERE id=1", (json.dumps(self.payload),))
        self.db.commit()
        return dict(self.payload)

    def close(self): self.db.close()


def emit(event, **payload):
    print(json.dumps({"event": event, **payload}, ensure_ascii=False, allow_nan=False), flush=True)


async def consume(name, url, tokens, server_ms, anchor, stats, deadline):
    import websockets
    state = stats[name]
    try:
        async with websockets.connect(url, open_timeout=10, close_timeout=2,
                                      max_size=2**20, ping_interval=20, ping_timeout=20) as ws:
            state["connected"] = True
            if name == "polymarket":
                await ws.send(json.dumps({"type": "market", "assets_ids": tokens}))
            while time.monotonic() < deadline:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=min(10, max(.01, deadline-time.monotonic())))
                except asyncio.TimeoutError:
                    if name == "polymarket": await ws.send("PING")
                    continue
                if raw in ("PONG", "PING"):
                    if raw == "PING": await ws.send("PONG")
                    continue
                body = json.loads(raw)
                messages = body if isinstance(body, list) else [body]
                for item in messages:
                    if not isinstance(item, dict): continue
                    state["messages"] += 1
                    state["last_received_mono"] = time.monotonic()
                    stamp = item.get("T") if name == "binance" else item.get("timestamp")
                    if stamp is not None:
                        stamp = float(stamp)
                        lag = server_ms + (time.monotonic()-anchor)*1000 - stamp
                        if math.isfinite(lag):
                            state["last_source_lag_estimate_ms"] = round(lag, 3)
                    if name == "binance": state["last_price"] = item.get("p")
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        state["error"] = type(exc).__name__  # Avoid environment/credential-bearing error strings.
    finally:
        state["connected"] = False


def feed_summary(stats):
    now = time.monotonic()
    return {name: {**{k: v for k, v in row.items() if k != "last_received_mono"},
                   "last_receive_age_seconds": round(now-row["last_received_mono"], 3)
                   if row.get("last_received_mono") else None} for name, row in stats.items()}


async def observe(args):
    began = time.monotonic()
    report, server_ms, anchor = await asyncio.to_thread(signal_snapshot)
    clock = lambda: server_ms / 1000 + time.monotonic() - anchor
    state = State(Path(args.state_dir))
    started = False
    tasks = []
    stats = {name: {"messages": 0, "connected": False} for name in ("binance", "polymarket")}
    status = "ERROR"
    try:
        previous = state.begin(clock())
        started = True
        emit("run_start", run_id=state.run_id, requested_seconds=args.seconds,
             previous_run=previous, scope="public_observation", orders_submitted=0)
        emit("signal_snapshot", **report)
        tokens = []
        try:
            market = await asyncio.to_thread(discover_market, report["window_start"])
            tokens = list(market["tokens"].values())
            emit("market_snapshot", **market)
        except Exception as exc:
            stats["polymarket"]["error"] = "MARKET_DISCOVERY_" + type(exc).__name__
        deadline = time.monotonic() + args.seconds
        tasks.append(asyncio.create_task(consume("binance", BINANCE_WS, [], server_ms, anchor, stats, deadline)))
        if tokens:
            tasks.append(asyncio.create_task(consume("polymarket", PM_WS, tokens, server_ms, anchor, stats, deadline)))
        while time.monotonic() < deadline:
            emit("checkpoint", **state.save(clock()), feeds=feed_summary(stats))
            await asyncio.sleep(min(15, max(0, deadline-time.monotonic())))
        await asyncio.gather(*tasks)
        summaries = feed_summary(stats)
        healthy = all(v["messages"] > 0 and not v.get("error") and
                      v["last_receive_age_seconds"] is not None and
                      v["last_receive_age_seconds"] < 5 for v in summaries.values())
        status = "COMPLETED" if healthy else "DEGRADED"
        state.save(clock(), status)
        emit("run_end", run_id=state.run_id, status=status, elapsed_seconds=round(time.monotonic()-began, 3),
             ws_summary=summaries, feeds_fresh_at_end=healthy,
             orders_submitted=0, hosting_verified=False)
        print("AUTOMATON_REPORT: " + json.dumps({"signals": int(report["signal_candidate"] is not None),
              "trades_attempted": 0, "trades_executed": 0, "amount_usd": 0,
              "status": status, "run_id": state.run_id}), flush=True)
        return 0 if status == "COMPLETED" else 2
    finally:
        for task in tasks: task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        if started and status == "ERROR": state.save(clock(), "ERROR")
        state.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=int, default=os.environ.get("K14_PROBE_SECONDS", "900"))
    parser.add_argument("--state-dir", default=os.environ.get("K14_STATE_DIR", str(ROOT / "state")))
    args = parser.parse_args()
    if not 1 <= args.seconds <= 1800: parser.error("seconds must be between 1 and 1800")
    try:
        return asyncio.run(observe(args))
    except Exception as exc:
        emit("probe_failed", error_type=type(exc).__name__, orders_submitted=0)
        return 2


if __name__ == "__main__":
    sys.exit(main())
