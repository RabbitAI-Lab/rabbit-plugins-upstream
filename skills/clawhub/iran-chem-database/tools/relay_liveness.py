#!/usr/bin/env python3
"""Relay liveness harness — run BEFORE any crawl, and nightly via celery beat.

    python3 tools/relay_liveness.py --live            # probe the public fleet
    python3 tools/relay_liveness.py --selftest        # offline sanity
    python3 tools/relay_liveness.py --live --write-config   # prune config.yaml

Why this exists: v2.33.0 shipped five relay methods whose endpoints were dead
the same week (Bing cache retired by Microsoft, Yandex caches 404,
thingproxy/yacdn NXDOMAIN, Web Light 404). A dead hop in the serial fail-over
chain costs ``free_access.timeout_seconds`` for EVERY blocked host before the
working relay is reached — pruning is worth more than any new relay. Exit 2 if
a CORE relay (translate_goog/jina/wayback/commoncrawl/arquivo_pt) is dead so
CI/beat can alert.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.crawler.relay_integrity import run_liveness_suite  # noqa: E402

CONFIG = ROOT / "config.yaml"
STATE = ROOT / "data" / "relay_liveness.json"
METHODS_RE = re.compile(r'(methods:\s*)\[[^\]]*\]')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--write-config", action="store_true",
                    help="rewrite free_access.methods to the measured ALIVE chain "
                         "(dead relays appended last, still opt-in per-site)")
    ns = ap.parse_args()

    if ns.selftest:
        from src.crawler.relay_integrity import _selftest
        return _selftest()

    if not ns.live:
        ap.print_help()
        return 1

    rep = run_liveness_suite(timeout=ns.timeout)
    rep["config_methods_before"] = None
    if CONFIG.exists():
        m = METHODS_RE.search(CONFIG.read_text())
        rep["config_methods_before"] = m.group(0) if m else None

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(rep, indent=1))

    width = max(len(k) for k in rep["methods"])
    for name, e in sorted(rep["methods"].items(), key=lambda kv: kv[1]["verdict"] != "ALIVE"):
        print(f"  {name:<{width}}  {e['verdict']:<6} {e['detail']}")
    print(f"\nsuggested default chain: {', '.join(rep['suggested_chain']) or '(NONE ALIVE)'}")
    print(f"prune from default:        {', '.join(rep['prune_from_default_chain']) or '-'}")

    if ns.write_config and rep["suggested_chain"]:
        # Method names actually implemented in src/crawler/free_access_engine.py.
        engine_methods = ["translate_goog", "bing_cache", "yandex_cache", "amp_cache",
                          "cors_proxy", "microlink", "jina", "wayback", "commoncrawl",
                          "arquivo_pt", "cloud_egress", "spn2", "translate", "archivetoday"]
        alive = [m for m in rep["suggested_chain"] if m in engine_methods]
        demote = [m for m in ("microlink", "cors_proxy") if m in alive]
        alive = [m for m in alive if m not in demote]
        # unprobed here: side-effecting (spn2) or env-dependent (cloud_egress); keep, late
        unprobed = ["cloud_egress", "spn2", "translate"]
        head = alive + demote + unprobed
        order = head + [m for m in engine_methods if m not in head]
        text = CONFIG.read_text()
        stamp = time.strftime("%Y-%m-%d")
        new_line = ('methods: ["' + '", "'.join(order) + f'"]  '
                    f"# v2.34.0 liveness-pruned {stamp}; dead relays last, opt-in only")
        text2 = METHODS_RE.sub(lambda m: new_line, text, count=1)
        if text2 == text:
            print("config.yaml: methods line not found — not modified", file=sys.stderr)
        else:
            CONFIG.write_text(text2)
            print(f"config.yaml rewritten -> {', '.join(order)}")

    from src.crawler.relay_integrity import CORE_METHODS
    core = [(m, rep["methods"].get(m, {}).get("verdict")) for m in CORE_METHODS]
    core_flaky = [m for m, v in core if v == "FLAKY"]
    core_dead = [m for m, v in core if v == "DEAD"]
    if core_flaky:
        print(f"note: core relays degraded (kept, breaker-paced): {', '.join(core_flaky)}",
              file=sys.stderr)
    if core_dead:
        print(f"ALERT core relays dead: {', '.join(core_dead)}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
