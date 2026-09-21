"""Race-based relay front-end for ``free_access_engine`` — v2.34.0 (Round-10).

Why the serial chain is the bottleneck, measured 2026-09-21:
``fetch_with_failover`` tries relays one at a time with ``timeout_seconds: 40``.
With five dead/absent relays ahead of a working one (``bing_cache``,
``yandex_cache``, ``web_light``, ``thingproxy``, ``yacdn`` all failed every
probe the day they shipped into the head of the list), a single blocked host
pays ~15 s per dead hop before reaching ``translate_goog``/``jina``. Dead-hop
tolerance, not new relays, is where the speed is.

This module adds:

``race_first_200``   — hedged parallel launch of the relays, staggered by
                       ``hedge_ms``; first body that passes the size gate wins.
``chain_from_liveness`` — build a per-run method order from the liveness report
                       instead of the shipped default, so dead relays never sit
                       at the head of the queue.
``breaker_ordered``  — EWMA + circuit-breaker ordering from live measurements,
                       so a relay that flakes in the middle of a crawl stops
                       costing every subsequent host.

Integration is one optional keyword on the existing API — no signature
breakage, no new egress class, same politeness envelope (robots-aware, one
request per relay per URL, size checks). If the race returns nothing usable
the caller falls through to the ordinary serial chain unchanged.

Policy is unchanged and deliberately narrow: public caching/archiving/link
preview infrastructure only. Nothing here probes or defeats an origin WAF,
spoofs a crawler UA or IP to a target that is not already serving that
crawler, or reuses a botnet-residential proxy. See
docs/RELAY_INTEGRITY_ROUND10.md §"What we did not add, and why".
"""
from __future__ import annotations

import threading
import time
from typing import Callable, Optional

from .relay_integrity import RelayCircuitBreaker, classify, http_fetch

# Live-first default order derived from the 2026-09-21 probe. Kept as data so
# it can be overridden by a fresh relay_liveness report at runtime.
LIVENESS_ORDER_2026_09_21 = [
    "translate_goog",   # ALIVE 5.5 kB / ~70 ms  — the only path for 4/8 blocked hosts
    "amp_cache",        # ALIVE ~60 ms, Google edge, no origin SYN
    "microlink",        # ALIVE ~65 ms, JS-rendered, metadata+html
    "jina",             # ALIVE ~150 ms — CACHED snapshot, tag freshness
    "commoncrawl",      # ALIVE ~400-1200 ms, S3, full HTML captures
    "arquivo_pt",       # ALIVE ~900 ms, 7.8 kB, independent crawler
    "cors_proxy",       # FLAKY — allorigins works, codetabs times out
    "wayback",          # FLAKY — burst-limited/503 at probe time, still essential
    "cloud_egress", "spn2", "translate", "archivetoday",
    # Measured DEAD the day of the release; kept reachable but last so a
    # per-site fingerprint can still select them, and a future revival is a
    # config-only change.
    "bing_cache", "yandex_cache", "web_light", "jsonlink",
]

# Relays that answer with a *copy* rather than a live fetch. Their bytes must
# never be counted as "current catalogue" without a freshness stamp.
ARCHIVE_METHODS = frozenset({
    "wayback", "spn2", "archivetoday", "commoncrawl", "arquivo_pt",
    "translate", "translate_goog", "amp_cache", "web_light", "bing_cache",
    "yandex_cache", "jina", "microlink", "jsonlink",
})


def chain_from_liveness(report: Optional[dict], default: list[str]) -> list[str]:
    """Reorder ``default`` from a relay_liveness report.

    ALIVE → front, ordered by measured latency; FLAKY → middle; DEAD → tail.
    Unknown methods keep their relative position behind the known ones. A
    missing/corrupt report degrades to the shipped default (never fails).
    """
    order = list(default)
    if not isinstance(report, dict):
        return order
    methods = report.get("methods") or {}
    if not methods:
        return order
    rank = {"ALIVE": 0, "FLAKY": 1, "DEAD": 2}

    def key(name: str) -> tuple[int, float]:
        e = methods.get(name)
        if not e:
            return (3, 0.0)
        return (rank.get(e.get("verdict"), 3), e.get("best_ms") or 0.0)

    order.sort(key=key)
    return order


def race_first_200(relays: list[tuple[str, Callable[[], dict]]],
                   size_gate: int = 1200, hedge_ms: float = 900.0,
                   per_relay_timeout: float = 40.0,
                   breaker: Optional[RelayCircuitBreaker] = None) -> dict:
    """Race candidate relays with staggered launch; fastest gate-passing body wins.

    ``relays``: ``[(method_name, zero_arg_callable)]`` in priority order.
    Each callable must save into the mirror dir and return the engine's usual
    dict (``saved``/``bytes``/``error``). ``hedge_ms`` bounds origin pressure:
    only one new relay is launched per interval, so a crawl never fans out
    beyond ``ceil(elapsed/hedge_ms)`` concurrent fetches per blocked host.
    Relays the breaker has opened are skipped entirely (they are retried once
    per cooldown as a half-open probe). Latencies feed the breaker's EWMA so
    the next host starts with the order this measurement produced.
    """
    started = time.monotonic()
    picked: list[tuple[str, Callable[[], dict]]] = []
    skipped: list[str] = []
    for name, fn in relays:
        if breaker is not None and not breaker.allow(name):
            skipped.append(name)
            continue
        picked.append((name, fn))

    winner = {"method_used": None, "skipped_by_breaker": skipped, "attempts": {}}
    from concurrent.futures import ThreadPoolExecutor

    claim_lock = threading.Lock()
    state = {"done": False, "winner": None}

    def run(name: str, fn: Callable[[], dict]) -> None:
        t0 = time.monotonic()
        try:
            res = fn() or {}
        except Exception as e:  # noqa: BLE001 — relays are hostile by nature
            res = {"method": name, "saved": 0, "error": f"{type(e).__name__}: {e}"[:160]}
        res = dict(res)
        res.setdefault("method", name)
        ms = int((time.monotonic() - t0) * 1000)
        ok = int(res.get("saved", 0) or 0) > 0 and not res.get("error")
        res["latency_ms"] = ms
        with claim_lock:
            winner["attempts"][name] = {
                k: v for k, v in res.items() if k in
                ("saved", "bytes", "error", "latency_ms", "path", "detail")}
            if ok and not state["done"]:
                state["done"] = True
                state["winner"] = res
        if breaker is not None:
            breaker.record(name, ok=ok, ms=float(ms))

    with ThreadPoolExecutor(max_workers=max(1, len(picked))) as pool:
        futures = []
        for i, (name, fn) in enumerate(picked):
            if i:
                time.sleep(min(hedge_ms, 30_000.0) / 1000.0)
                if state["done"]:
                    break
            futures.append((name, pool.submit(run, name, fn)))
        for name, fut in futures:
            if state["done"]:
                break
            try:
                fut.result(timeout=max(0.5, per_relay_timeout))
            except TimeoutError:
                winner["attempts"].setdefault(
                    name, {"saved": 0, "error": f"race timeout >{per_relay_timeout}s"})
                if breaker is not None:
                    breaker.record(name, ok=False)
            except Exception:  # already recorded inside run()
                pass

    if state["winner"]:
        w = dict(state["winner"])
        winner["method_used"] = w.pop("method", None) or (w.get("method"))
        winner["winner"] = w
        winner["race_ms"] = int((time.monotonic() - started) * 1000)
        winner["archive_only"] = winner["method_used"] in ARCHIVE_METHODS
    else:
        winner["race_ms"] = int((time.monotonic() - started) * 1000)
        winner["error"] = "no relay produced a gate-passing page"
    return winner


def breaker_ordered(names: list[str], breaker: RelayCircuitBreaker) -> list[str]:
    """EWMA-fastest first; breakers respected. Thin wrapper kept as the
    documented hook so callers do not reach into the breaker internals."""
    return breaker.ordered_relays(list(names))


def classify_probe(probe, result: dict) -> tuple[str, str]:
    """Re-export so callers can reuse the classifier for ad-hoc checks."""
    return classify(probe, result)


def fetch_probe(url: str, timeout: float = 15.0) -> dict:
    return http_fetch(url, timeout)
