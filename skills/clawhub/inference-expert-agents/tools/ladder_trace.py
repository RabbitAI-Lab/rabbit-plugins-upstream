#!/usr/bin/env python3
"""ladder_trace.py — run-tree tracing + cost telemetry + failure taxonomy
(F26, F41, F43). LangSmith-lite: record each ladder step (rung, event, tokens,
cost, status, failure class), then summarize per-rung costs and the failure
taxonomy. State: one JSON db passed via --db (strictly opt-in, 0600)."""
import argparse, json, os, sys, time, uuid

CLASSES = ("prompt", "tool", "retrieval", "orchestration", "verification", "none")


def _ensure_perm(db):
    """Best-effort: state files must be owner-only (0600)."""
    try:
        if os.stat(db).st_mode & 0o777 != 0o600:
            os.chmod(db, 0o600)
    except OSError:
        pass

def _dump_json(db, obj):
    """Atomic JSON state write (tmp + os.replace), 0600 from creation."""
    os.makedirs(os.path.dirname(db) or ".", exist_ok=True)
    tmp = f"{db}.tmp-{os.getpid()}"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f)
    except BaseException:
        try:
            os.close(fd)
        except OSError:
            pass
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.replace(tmp, db)
    _ensure_perm(db)

def load(db):
    if db is None:
        return {}
    _ensure_perm(db)
    try:
        d = json.load(open(db, encoding="utf-8"))
        if not isinstance(d, dict):
            raise ValueError("state db is not a JSON object")
        return d
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise ValueError(f"state file {db} is corrupt/unreadable (left untouched): {e}")

def save(db, d):
    os.makedirs(os.path.dirname(db) or ".", exist_ok=True)
    _dump_json(db, d)

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["start", "step", "show", "summary"])
    ap.add_argument("--db", default=None,
                    help="JSON state file; state is strictly opt-in — nothing is written or read without it")
    ap.add_argument("--trace")
    ap.add_argument("--rung", choices=["L0", "L1", "L2", "L3", "L4", "FORCE"])
    ap.add_argument("--event")
    ap.add_argument("--tokens", type=int, default=0)
    ap.add_argument("--cost-usd", type=float, default=0.0)
    ap.add_argument("--latency-s", type=float, default=0.0)
    ap.add_argument("--cache", choices=["hit", "miss", "n/a"], default="n/a")
    ap.add_argument("--status", choices=["ok", "fail"], default="ok")
    ap.add_argument("--failure-class", choices=CLASSES, default="none")
    a = ap.parse_args()
    d = load(a.db)
    if getattr(a, "db", None) is None:
        print(json.dumps({"error": "no --db given — persistent state is opt-in; "
                                  "pass --db PATH to enable it",
                          "state": "none"}))
        return 2
    if a.cmd == "start":
        tid = uuid.uuid4().hex[:12]
        d[tid] = {"steps": [], "started": time.time()}
        save(a.db, d)
        print(json.dumps({"trace_id": tid})); return 0
    if not a.trace or a.trace not in d:
        print(json.dumps({"error": "unknown --trace (start one first)"})); return 2
    t = d[a.trace]
    if a.cmd == "step":
        if not a.rung or not a.event:
            print(json.dumps({"error": "--rung and --event required"})); return 2
        t["steps"].append({"rung": a.rung, "event": a.event[:300], "tokens": a.tokens,
                           "cost_usd": a.cost_usd, "latency_s": a.latency_s,
                           "cache": a.cache, "status": a.status,
                           "failure_class": a.failure_class, "ts": time.time()})
        save(a.db, d)
        print(json.dumps({"recorded": True, "steps": len(t["steps"])})); return 0
    if a.cmd == "show":
        print(json.dumps({"trace_id": a.trace, "steps": t["steps"]}, indent=2)); return 0
    per_rung, tax, cost = {}, {}, 0.0
    for s in t["steps"]:
        r = per_rung.setdefault(s["rung"], {"steps": 0, "tokens": 0, "cost_usd": 0.0})
        r["steps"] += 1; r["tokens"] += s["tokens"]; r["cost_usd"] += s["cost_usd"]
        cost += s["cost_usd"]
        if s["status"] == "fail":
            fc = s["failure_class"] if s["failure_class"] != "none" else "unclassified"
            tax[fc] = tax.get(fc, 0) + 1
    print(json.dumps({
        "trace_id": a.trace, "n_steps": len(t["steps"]),
        "per_rung": {k: {**v, "cost_usd": round(v["cost_usd"], 6)} for k, v in per_rung.items()},
        "total_cost_usd": round(cost, 6),
        "failure_taxonomy": tax,
        "hint": "highest-cost rung with least quality gain is your triage bug; failure classes show where verification pays",
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
