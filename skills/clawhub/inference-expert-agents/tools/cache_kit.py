#!/usr/bin/env python3
"""cache_kit.py — prompt/answer caching with TTL + LRU (F24).

Exact-key + semantic (token-Jaccard) lookup, TTL expiry, LRU eviction, and hit
statistics. All state lives in ONE JSON db whose path you pass via --db
(pass --db PATH explicitly; nothing is written without it). GPTCache-flavored.
"""
import argparse, json, os, sys, time


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
        return {"entries": [], "stats": {"hits": 0, "misses": 0}}
    _ensure_perm(db)
    try:
        d = json.load(open(db, encoding="utf-8"))
        if not isinstance(d, dict):
            raise ValueError("state db is not a JSON object")
        return d
    except FileNotFoundError:
        return {"entries": [], "stats": {"hits": 0, "misses": 0}}
    except Exception as e:
        raise ValueError(f"state file {db} is corrupt/unreadable (left untouched): {e}")

def save(db, d):
    os.makedirs(os.path.dirname(db) or ".", exist_ok=True)
    _dump_json(db, d)

def toks(s):
    return set(s.lower().split()) - {"the", "a", "an", "of", "and", "to", "in"}

def jac(a, b):
    A, B = toks(a), toks(b)
    return len(A & B) / len(A | B) if A | B else 0.0

def prune(d, ttl, cap, now):
    d["entries"] = [e for e in d["entries"] if now - e["ts"] < ttl]
    d["entries"].sort(key=lambda e: -e["ts"])
    d["entries"] = d["entries"][:cap]

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["put", "get", "stats"])
    ap.add_argument("--db", default=None,
                    help="JSON state file; state is strictly opt-in — nothing is written or read without it")
    ap.add_argument("--prompt"); ap.add_argument("--answer")
    ap.add_argument("--threshold", type=float, default=0.85)
    ap.add_argument("--ttl", type=int, default=86400)
    ap.add_argument("--cap", type=int, default=256)
    a = ap.parse_args()
    d = load(a.db); now = time.time()
    if getattr(a, "db", None) is None:
        print(json.dumps({"error": "no --db given — persistent state is opt-in; "
                                  "pass --db PATH to enable it",
                          "state": "none"}))
        return 2
    prune(d, a.ttl, a.cap, now)
    if a.cmd == "stats":
        print(json.dumps(d["stats"], indent=2)); return 0
    if not a.prompt:
        print(json.dumps({"error": "--prompt required"})); return 2
    if a.cmd == "put":
        if not a.answer:
            print(json.dumps({"error": "--answer required for put"})); return 2
        d["entries"].insert(0, {"prompt": a.prompt, "answer": a.answer, "ts": now})
        d["entries"] = d["entries"][:a.cap]
        save(a.db, d)
        print(json.dumps({"cached": True, "entries": len(d["entries"])})); return 0
    best, sim = None, 0.0
    for e in d["entries"]:
        s = 1.0 if e["prompt"] == a.prompt else jac(e["prompt"], a.prompt)
        if s > sim:
            best, sim = e, s
    if best and sim >= a.threshold:
        d["stats"]["hits"] += 1; save(a.db, d)
        print(json.dumps({"hit": True, "similarity": round(sim, 3),
                          "age_s": int(now - best["ts"]),
                          "answer": best["answer"],
                          "warning": "semantic hit — confirm the answer is still valid for the paraphrased prompt"} if sim < 1.0
                         else {"hit": True, "similarity": 1.0,
                               "age_s": int(now - best["ts"]), "answer": best["answer"]},
                         indent=2))
    else:
        d["stats"]["misses"] += 1; save(a.db, d)
        print(json.dumps({"hit": False, "best_similarity": round(sim, 3)}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
