"""Relay-integrity layer — v2.34.0 (Round-10).

Three problems found by field measurement on 2026-09-21, fixed here:

1. DEAD RELAYS IN THE DEFAULT CHAIN. ``bing_cache`` (cc.bingj.com cache
   endpoint retired by Microsoft), ``yandex_cache`` (HTTP 404 service-wide),
   ``web_light``, ``thingproxy``/``yacdn`` (NXDOMAIN) were listed as
   "field-verified" but failed every probe the same day. Every dead hop costs
   a full ``timeout_seconds`` per blocked host, so pruning them is the
   single biggest speed win available.
2. STALE RELAYS COUNTED AS LIVE COVERAGE. ``r.jina.ai`` serves *cached
   snapshots* (it says so: ``Published Time: ...`` warning) — a six-day-old
   snapshot must not be recorded as a fresh catalogue page.
3. SERIAL FAIL-OVER IS SLOW. The chain waits out each relay in order.
   For hosts with no per-site preference, racing the top-K relays in
   parallel cuts p50 latency from (sum of latencies) to (latency of the
   fastest winner).

Policy this module encodes (non-negotiable): only **public caching /
archiving / link-preview infrastructure** is probed here. The skill never
adds methods that defeat an operator's access control (origin-IP exposure to
bypass a CDN blocklist, TLS/JA3 fingerprint spoofing, paywall circumvention
services, residential-proxy relays — a market currently under active criminal
enforcement: 911 S5 bust 2024, Lumen/Peer2Peer charges 2024, NetNut FBI
seizure 2026-07-02). See docs/RELAY_INTEGRITY_ROUND10.md.

Stdlib only. ``python3 -m src.crawler.relay_integrity --selftest`` runs
offline against a local canned-response server.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Callable, Optional

UA = (
    "Mozilla/5.0 (compatible; iran-chem-db relay-liveness/1.0; "
    "academic procurement research; polite, low-rate)"
)

# ---------------------------------------------------------------------------
# Liveness probes
# ---------------------------------------------------------------------------

CORE_METHODS = ("translate_goog", "jina", "wayback", "commoncrawl", "arquivo_pt")


@dataclass
class Probe:
    method: str                 # name as used in free_access.methods
    url: str
    min_bytes: int = 1024
    must_contain: tuple = ()
    must_not_contain: tuple = ("Sorry, you have been blocked", "Access denied")
    retries: int = 2            # public caches burst-limit; 2 tries before declaring DEAD
    backoff_s: float = 2.5


DEFAULT_PROBES: tuple[Probe, ...] = (
    Probe("translate_goog",
          "https://example-com.translate.goog/?_x_tr_sl=auto&_x_tr_tl=de&_x_tr_hl=en",
          min_bytes=1500, must_contain=("Example Domain",)),
    Probe("bing_cache", "https://cc.bingj.com/cache.aspx?q=example.com", min_bytes=4096),
    Probe("yandex_cache", "https://cc.yandex.com/cache?url=https%3A%2F%2Fexample.com", min_bytes=2048),
    Probe("web_light", "https://googleweblight.com/i?u=https%3A%2F%2Fexample.com", min_bytes=2048),
    Probe("amp_cache", "https://cdn.ampproject.org/c/s/example.com/", min_bytes=200),
    # cors_proxy: engine rotates this fleet; a method is ALIVE if ANY member answers.
    Probe("cors_proxy", "https://api.allorigins.win/get?url=https%3A%2F%2Fexample.com",
          min_bytes=100, must_contain=("Example Domain",)),
    Probe("cors_proxy", "https://corsproxy.io/?https://example.com", min_bytes=1024,
          must_contain=("Example Domain",)),
    Probe("cors_proxy", "https://api.codetabs.com/v1/proxy?quest=https%3A%2F%2Fexample.com",
          min_bytes=1024, must_contain=("Example Domain",)),
    Probe("microlink", "https://api.microlink.io/?url=https%3A%2F%2Fexample.com",
          min_bytes=120, must_contain=('"status":"success"',)),
    Probe("jsonlink", "https://jsonlink.io/api/extract?url=https%3A%2F%2Fexample.com",
          min_bytes=120),
    Probe("jina", "https://r.jina.ai/https://example.com",
          min_bytes=120, must_contain=("Example Domain",)),
    Probe("wayback", "https://web.archive.org/cdx/search/cdx?url=example.com&limit=1&output=json",
          min_bytes=40, must_contain=("urlkey",)),
    Probe("commoncrawl",
          "http://index.commoncrawl.org/CC-MAIN-2025-21-index?url=example.com&output=json&limit=1",
          min_bytes=40, must_contain=("urlkey",)),
    Probe("arquivo_pt", "https://arquivo.pt/wayback/20200101000000/https://example.com/",
          min_bytes=1024, must_contain=("example",)),
    Probe("archivetoday", "https://archive.ph/newest/https://example.com", min_bytes=1024),
)


def http_fetch(url: str, timeout: float = 15.0, cap: int = 262_144) -> dict:
    """GET with size cap; never raises. status=0 means connect/DNS/TLS failure."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(cap)
            return {"status": r.status, "bytes": len(body),
                    "text": body.decode("utf-8", "replace"),
                    "ms": int((time.monotonic() - t0) * 1000)}
    except urllib.error.HTTPError as e:
        try:
            body = e.read(65_536)
        except Exception:  # pragma: no cover
            body = b""
        return {"status": e.code, "bytes": len(body),
                "text": body.decode("utf-8", "replace"),
                "ms": int((time.monotonic() - t0) * 1000)}
    except Exception as e:  # URLError, timeout, DNS …
        return {"status": 0, "bytes": 0, "text": "",
                "error": f"{type(e).__name__}: {e}"[:200],
                "ms": int((time.monotonic() - t0) * 1000)}


def classify(probe: Probe, r: dict) -> tuple[str, str]:
    """DEAD = endpoint gone (DNS NXDOMAIN, 4xx, block marker, empty body).
    FLAKY = present but degraded right now (timeouts, 5xx, burst limits) —
    belongs at the tail of the chain behind the circuit breaker, never pruned."""
    if r["status"] == 0:
        err = r.get("error", "connect failure")
        if "timed out" in err.lower() or "timeout" in err.lower():
            return "FLAKY", err
        return "DEAD", err
    for marker in probe.must_not_contain:
        if marker.lower() in r["text"].lower():
            return "DEAD", f"block marker {marker!r}"
    if r["status"] >= 500 or r["status"] == 429:  # 429 = burst limit, not death
        return "FLAKY", f"HTTP {r['status']}"
    if r["status"] >= 400:
        return "DEAD", f"HTTP {r['status']}"
    text_ok = all(needle in r["text"] for needle in probe.must_contain)
    if text_ok and r["bytes"] >= 64:
        return "ALIVE", f"{r['bytes']}B in {r['ms']}ms"
    if r["bytes"] < 64:
        return "DEAD", f"empty body ({r['bytes']}B)"
    if not text_ok:
        missing = [n for n in probe.must_contain if n not in r["text"]]
        return "FLAKY", f"payload missing {missing[0]!r}"
    return "FLAKY", f"only {r['bytes']}B (<{probe.min_bytes}B gate)"


def run_liveness_suite(probes: tuple[Probe, ...] = DEFAULT_PROBES,
                       timeout: float = 15.0, workers: int = 6,
                       fetcher: Optional[Callable[[str, float], dict]] = None) -> dict:
    """Probe every relay endpoint once; roll up to per-method verdicts.

    A method is ALIVE when any of its probes is ALIVE (fastest one wins);
    FLAKY when some probe answers but fails a payload gate; DEAD otherwise.
    """
    fetcher = fetcher or http_fetch

    def probe_with_retry(pr: Probe) -> tuple[Probe, dict]:
        last: dict = {}
        for attempt in range(max(1, pr.retries)):
            last = fetcher(pr.url, timeout)
            verdict, _ = classify(pr, last)
            if verdict != "DEAD":
                break
            if attempt + 1 < max(1, pr.retries):
                time.sleep(pr.backoff_s * (attempt + 1))
        return pr, last

    with ThreadPoolExecutor(max_workers=workers) as pool:
        rows = list(pool.map(probe_with_retry, probes))

    per: dict[str, dict] = {}
    for probe, r in rows:
        verdict, detail = classify(probe, r)
        entry = per.setdefault(probe.method, {"verdict": "DEAD", "probes": [], "best_ms": None,
                                              "detail": ""})
        entry["probes"].append({"url": probe.url, "verdict": verdict, "detail": detail,
                                "status": r["status"], "ms": r.get("ms")})
        rank = {"ALIVE": 2, "FLAKY": 1, "DEAD": 0}
        if rank[verdict] >= rank[entry["verdict"]] and (
                rank[verdict] > rank[entry["verdict"]] or not entry["detail"]):
            entry["verdict"], entry["detail"] = verdict, detail
        if verdict == "ALIVE":
            ms = r.get("ms") or 10**9
            if entry["best_ms"] is None or ms < entry["best_ms"]:
                entry["best_ms"] = ms

    alive = sorted((m for m, e in per.items() if e["verdict"] == "ALIVE"),
                   key=lambda m: per[m]["best_ms"] or 10**9)
    flaky = sorted((m for m, e in per.items() if e["verdict"] == "FLAKY"),
                   key=lambda m: per[m]["best_ms"] or 10**9)
    return {
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "methods": per,
        "suggested_chain": alive + flaky,
        "alive": alive,
        "flaky_tail": flaky,
        "prune_from_default_chain": sorted(m for m, e in per.items()
                                           if e["verdict"] == "DEAD"
                                           and m not in ("jsonlink",)),
    }


# ---------------------------------------------------------------------------
# Circuit breaker + per-host EWMA latency (self-maintaining chain order)
# ---------------------------------------------------------------------------

class RelayCircuitBreaker:
    """Skip relays that failed N times in a row until a cooldown passes.

    Prevents every crawl from re-paying the timeout of a dead relay before
    reaching the working one (the exact pathology measured on 2026-09-21:
    five dead relays in front of ``jina`` = 5 x timeout_seconds wasted per
    blocked host).
    """

    def __init__(self, threshold: int = 3, cooldown_s: float = 3600.0,
                 ewma_alpha: float = 0.3):
        self.threshold, self.cooldown_s, self.alpha = threshold, cooldown_s, ewma_alpha
        self._lock = threading.Lock()
        self._fails: dict[str, int] = {}
        self._opened_at: dict[str, float] = {}
        self.ewma_ms: dict[str, float] = {}

    def allow(self, name: str, now: Optional[float] = None) -> bool:
        """Whether to probe this relay again. Once opened, only ONE call per
        cooldown window is let through (half-open); a failure re-opens it."""
        now = now if now is not None else time.monotonic()
        with self._lock:
            if self._fails.get(name, 0) < self.threshold:
                return True
            opened = self._opened_at.get(name, 0.0)
            if now - opened >= self.cooldown_s:
                self._opened_at[name] = now  # consume the half-open probe
                return True
            return False

    def record(self, name: str, ok: bool, ms: Optional[float] = None,
               now: Optional[float] = None) -> None:
        now = now if now is not None else time.monotonic()
        with self._lock:
            if ok:
                self._fails[name] = 0
                self._opened_at.pop(name, None)
                if ms is not None:
                    prev = self.ewma_ms.get(name)
                    self.ewma_ms[name] = ms if prev is None else (
                        self.alpha * ms + (1 - self.alpha) * prev)
            else:
                self._fails[name] = self._fails.get(name, 0) + 1
                if self._fails[name] == self.threshold:
                    self._opened_at[name] = now

    def ordered_relays(self, names: list[str]) -> list[str]:
        """Default chain order = last measured speed, breakers respected."""
        allowed = [n for n in names if self.allow(n)]
        skipped = [n for n in names if n not in allowed]
        return sorted(allowed, key=lambda n: self.ewma_ms.get(n, 10**9)) + skipped


# ---------------------------------------------------------------------------
# Hedged race: first relay to return a gate-passing body wins
# ---------------------------------------------------------------------------

def race_relays(fetchers: list[tuple[str, Callable[[], dict]]],
                size_gate: int = 1200, hedge_ms: float = 1200.0,
                per_relay_timeout: float = 30.0) -> dict:
    """Staggered parallel race over ``[(name, zero_arg_callable)]``.

    Launch relay #1, then #2 after ``hedge_ms``, then #3 … First result with
    ``bytes >= size_gate`` and no ``error`` wins. Staggering bounds origin
    pressure: at any instant only the relays launched so far are in flight.
    Each candidate gets ``per_relay_timeout``; after that its thread is
    abandoned (daemon threads; late losers only write into the discarded
    winner dict — mirror saves are idempotent, no cleanup needed).
    Fail-open: if nothing passes the gate, return an ``error`` + ``partial``
    list so callers keep their existing chain semantics.
    """
    winner: dict = {}
    claim = threading.Lock()
    state = {"done": False}

    def done_() -> bool:
        with claim:
            return state["done"]

    def run(name: str, fn: Callable[[], dict], started: float) -> None:
        if done_():
            return
        try:
            res = fn() or {}
        except Exception as e:  # relays are hostile; record and move on
            res = {"error": f"{type(e).__name__}: {e}"[:200], "bytes": 0}
        res = dict(res)
        res.setdefault("method", name)
        with claim:
            if (not state["done"] and int(res.get("bytes") or 0) >= size_gate
                    and not res.get("error")):
                state["done"] = True
                winner.update(res)

    threads: list[tuple[str, threading.Thread, float]] = []
    for i, (name, fn) in enumerate(fetchers):
        if i:
            time.sleep(min(hedge_ms, 30_000.0) / 1000.0)
            if done_():
                break
        t0 = time.monotonic()
        th = threading.Thread(target=run, args=(name, fn, t0), daemon=True)
        th.start()
        threads.append((name, th, t0))

    partial: list[str] = []
    for name, th, t0 in threads:
        if done_():
            break
        remaining = per_relay_timeout - (time.monotonic() - t0)
        th.join(timeout=max(0.0, remaining))
        if th.is_alive():
            partial.append(f"{name}: timeout >{per_relay_timeout}s (abandoned)")

    result = dict(winner) if winner else {
        "error": "no relay passed the size gate", "bytes": 0, "partial": partial}
    return result


# ---------------------------------------------------------------------------
# Freshness provenance — a cached snapshot is never "live coverage"
# ---------------------------------------------------------------------------

_PUBLISHED = re.compile(r"Published Time:\s*([A-Za-z]{3}, \d{2} [A-Za-z]{3} \d{4})", re.I)


def tag_freshness(text: str, method: str, today_utc: Optional[time.struct_time] = None) -> dict:
    """Return {freshness, snapshot_date, method}.

    jina: response carries a self-declared ``Published Time: Tue, 15 Sep 2026``
    cache warning — parse it. wayback/archivetoday/arquivo/commoncrawl: by
    definition archived. translate_goog/amp/bing/yandex caches: archived too
    (translate.goog re-fetches live for ``.ir`` only opportunistically).
    Everything else defaults to ``live`` but is still stamped.
    """
    today_utc = today_utc or time.gmtime()
    if method == "jina":
        m = _PUBLISHED.search(text or "")
        if m:
            try:
                parsed = time.strptime(m.group(1), "%a, %d %b %Y")
                if time.mktime(parsed) < time.mktime(today_utc) - 86_400:
                    return {"freshness": "cached", "method": method,
                            "snapshot_date": time.strftime("%Y-%m-%d", parsed)}
            except ValueError:
                pass
        return {"freshness": "live", "method": method}
    if method in {"wayback", "spn2", "archivetoday", "commoncrawl", "arquivo_pt",
                  "translate", "translate_goog", "amp_cache", "web_light"}:
        return {"freshness": "relay_or_archive", "method": method}
    return {"freshness": "live", "method": method}


# ---------------------------------------------------------------------------
# Selftest (offline, deterministic)
# ---------------------------------------------------------------------------

def _selftest() -> int:
    failures: list[str] = []

    def check(cond: bool, label: str) -> None:
        if not cond:
            failures.append(label)

    # --- classify against canned results -----------------------------------
    p = Probe("x", "http://x", min_bytes=1000, must_contain=("needle",))
    check(classify(p, {"status": 0, "bytes": 0, "text": "", "error": "boom", "ms": 1})
          == ("DEAD", "boom"), "classify: connect failure -> DEAD")
    check(classify(p, {"status": 0, "bytes": 0, "text": "",
                       "error": "TimeoutError: read operation timed out", "ms": 1})[0] == "FLAKY",
          "classify: timeout -> FLAKY (kept, paced)")
    check(classify(p, {"status": 403, "bytes": 5000, "text": "nope", "ms": 1})[0] == "DEAD",
          "classify: HTTP 403 -> DEAD")
    check(classify(p, {"status": 200, "bytes": 10, "text": "", "ms": 1})[0] == "DEAD",
          "classify: tiny body -> DEAD")
    check(classify(p, {"status": 200, "bytes": 1200, "text": "nothing relevant", "ms": 1})[0] == "FLAKY",
          "classify: missing marker -> FLAKY")
    check(classify(p, {"status": 200, "bytes": 1200, "text": "Sorry, You Have Been Blocked", "ms": 1})[0] == "DEAD",
          "classify: block marker -> DEAD")
    check(classify(p, {"status": 200, "bytes": 1200, "text": "a needle b", "ms": 1})[0] == "ALIVE",
          "classify: good body -> ALIVE")

    # --- suite roll-up with a fake fetcher ----------------------------------
    fake = {
        "http://a/1": {"status": 200, "bytes": 2000, "text": "needle A", "ms": 120},
        "http://a/2": {"status": 0, "bytes": 0, "text": "", "error": "conn", "ms": 15000},
        "http://b/1": {"status": 500, "bytes": 0, "text": "", "ms": 50},
        "http://c/1": {"status": 404, "bytes": 0, "text": "", "ms": 50},
    }
    suite = run_liveness_suite(
        probes=(Probe("alpha", "http://a/1", must_contain=("needle",), backoff_s=0),
                Probe("alpha", "http://a/2", must_contain=("needle",), backoff_s=0),
                Probe("beta", "http://b/1", backoff_s=0),
                Probe("gamma", "http://c/1", backoff_s=0)),
        fetcher=lambda u, t: fake[u])
    check(suite["methods"]["alpha"]["verdict"] == "ALIVE", "rollup: one live probe -> ALIVE")
    check(suite["methods"]["beta"]["verdict"] == "FLAKY", "rollup: 5xx -> FLAKY (not pruned)")
    check(suite["methods"]["gamma"]["verdict"] == "DEAD", "rollup: 4xx -> DEAD")
    check(suite["suggested_chain"] == ["alpha", "beta"], "chain: ALIVE then FLAKY tail")
    check(suite["prune_from_default_chain"] == ["gamma"], "prune list only DEAD methods")

    # --- circuit breaker ------------------------------------------------------
    br = RelayCircuitBreaker(threshold=3, cooldown_s=0.5)
    t = 1000.0
    for _ in range(3):
        br.record("dead_relay", ok=False, now=t)
    check(br.allow("dead_relay", now=t + 1e-3) is False, "breaker opens after threshold")
    check(br.allow("dead_relay", now=t + 0.49) is False, "breaker stays open within cooldown")
    check(br.allow("dead_relay", now=t + 0.50) is True, "breaker half-opens after cooldown")
    check(br.allow("dead_relay", now=t + 0.50) is False, "half-open probe is single-shot")
    br.record("dead_relay", ok=True, ms=300.0, now=t + 0.51)
    check(br.allow("dead_relay", now=t + 0.52) is True, "breaker closes on success")
    check(abs(br.ewma_ms["dead_relay"] - 300.0) < 1e-6, "EWMA seeded by first sample")
    br.record("slow_relay", ok=True, ms=900.0)
    br.record("fast_relay", ok=True, ms=100.0)
    check(br.ordered_relays(["slow_relay", "fast_relay", "unseen"])
          == ["fast_relay", "slow_relay", "unseen"], "EWMA ordering with unseen last")

    # --- classify against a REAL HTTP server (exercises http_fetch + timeout) --
    import http.server
    import threading as _th
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/ok":
                body = b"needle " + b"x" * 2000
                self.send_response(200)
            else:
                body = b"nope"
                self.send_response(503)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def log_message(self, *a):  # silence
            pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    port = srv.server_address[1]
    _th.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"
    try:
        r_ok = http_fetch(base + "/ok", timeout=5)
        check(classify(Probe("t", base + "/ok", must_contain=("needle",)), r_ok)[0] == "ALIVE",
              "http_fetch+classify: 200 with marker -> ALIVE")
        r_err = http_fetch(base + "/bad", timeout=5)
        check(r_err["status"] == 503, "http_fetch: HTTPError status captured")
        r_dns = http_fetch("http://127.0.0.1:1/x", timeout=3)
        check(r_dns["status"] == 0 and r_dns.get("error"), "http_fetch: connect failure -> status 0")
    finally:
        srv.shutdown()

    # --- race ------------------------------------------------------------------
    def slow(): time.sleep(0.35); return {"bytes": 5000, "text": "slow but ok"}
    def fast(): return {"bytes": 5000, "text": "fast wins"}
    def tiny(): return {"bytes": 10, "error": None, "text": "too small — must NOT win"}
    res = race_relays([("fast", fast), ("slow", slow), ("tiny", tiny)],
                      size_gate=1200, hedge_ms=0, per_relay_timeout=5)
    check(res.get("method") == "fast", f"race picks fastest gate-passing relay (got {res.get('method')})")
    bad = race_relays([("tiny", tiny)], size_gate=1200, hedge_ms=0, per_relay_timeout=5)
    check("error" in bad, "race fails open with error when nothing passes the gate")
    hang = race_relays([("hang", lambda: time.sleep(30))], size_gate=1200,
                       hedge_ms=0, per_relay_timeout=0.5)
    check("error" in hang and hang.get("partial"), "race bounds a hanging relay by per_relay_timeout")

    # --- freshness tagging ------------------------------------------------------
    jina_cached = "Warning: snapshot\nPublished Time: Tue, 15 Sep 2026 23:41:26 GMT\nbody"
    tag = tag_freshness(jina_cached, "jina", today_utc=time.strptime("2026-09-21", "%Y-%m-%d"))
    check(tag["freshness"] == "cached" and tag["snapshot_date"] == "2026-09-15",
          "jina cached snapshot flagged with parsed date")
    check(tag_freshness("fresh today", "jina")["freshness"] == "live", "jina no-marker -> live")
    check(tag_freshness("x", "wayback")["freshness"] == "relay_or_archive",
          "wayback tagged relay_or_archive")

    if failures:
        print("SELFTEST FAIL")
        for f in failures:
            print("  -", f)
        return 1
    print("SELFTEST PASS (classify, rollup, breaker, race, freshness)")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true", help="offline deterministic tests")
    ap.add_argument("--live", action="store_true", help="probe real relay endpoints")
    ap.add_argument("--json", metavar="PATH", help="write suite JSON report")
    ap.add_argument("--timeout", type=float, default=15.0)
    ns = ap.parse_args(argv)
    if ns.selftest:
        return _selftest()
    if ns.live:
        rep = run_liveness_suite(timeout=ns.timeout)
        for name, e in sorted(rep["methods"].items()):
            print(f"{name:16s} {e['verdict']:6s} {e['detail']}")
        print("suggested_chain:", ", ".join(rep["suggested_chain"]))
        print("prune:", ", ".join(rep["prune_from_default_chain"]) or "-")
        if ns.json:
            with open(ns.json, "w") as fh:
                json.dump(rep, fh, indent=1)
        core = [(m, rep["methods"].get(m, {}).get("verdict")) for m in CORE_METHODS]
        core_dead = [m for m, v in core if v == "DEAD"]
        core_flaky = [m for m, v in core if v == "FLAKY"]
        if core_flaky:
            print("core relays degraded (kept, breaker will pace them):",
                  ", ".join(core_flaky), file=sys.stderr)
        if core_dead:
            print("CORE RELAYS DEAD:", ", ".join(core_dead), file=sys.stderr)
            return 2
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
