#!/usr/bin/env python3
"""memory_kit.py — agent memory: episodic reflections, rules-of-thumb, skill
library, deliberate forgetting (F30-F34). Reflexion/ExpeL/Voyager-flavored.

All state lives in ONE JSON db passed via --db (strictly opt-in — never the
user's home). Search is token-overlap scoring; eviction is explicit.
"""
import argparse, json, os, sys, time

KINDS = ("reflection", "rule", "skill")


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

def toks(s):
    # crude prefix stemming so verify/verifying, dois/doi, citations/citing match
    stops = {"the", "a", "an", "of", "and", "to", "in", "is", "was"}
    return {w[:5] for w in s.lower().split() if w not in stops}

def score(q, text):
    Q, T = toks(q), toks(text)
    return len(Q & T) / max(1, len(Q))

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["add", "search", "forget", "stats"])
    ap.add_argument("--db", default=None,
                    help="JSON state file; state is strictly opt-in — nothing is written or read without it")
    ap.add_argument("--kind", default="reflection",
                    help="reflection | rule | skill")
    ap.add_argument("--text", help="reflection: task|failure|lesson · rule: the rule · skill: description")
    ap.add_argument("--name", help="skill name (add --kind skill)")
    ap.add_argument("--query")
    ap.add_argument("--older-than-days", type=float, default=None)
    ap.add_argument("--cap", type=int, default=100, help="max entries per kind")
    ap.add_argument("--top", type=int, default=5)
    a = ap.parse_args()
    d = load(a.db)
    if getattr(a, "db", None) is None:
        print(json.dumps({"error": "no --db given — persistent state is opt-in; "
                                  "pass --db PATH to enable it",
                          "state": "none"}))
        return 2
    for k in KINDS:
        d.setdefault(k, [])
    now = time.time()
    if a.cmd == "add":
        if not a.text:
            print(json.dumps({"error": "--text required"})); return 2
        import hashlib
        entry = {"text": a.text, "ts": now,
                 "id": hashlib.sha1(a.text.encode()).hexdigest()[:8]}
        if a.kind == "skill":
            entry["name"] = a.name or (a.text.split(":")[0][:40] if ":" in a.text else a.text[:40])
        d[a.kind].insert(0, entry)
        d[a.kind] = d[a.kind][:a.cap]  # deliberate cap = deliberate forgetting
        save(a.db, d)
        print(json.dumps({"added": a.kind, "total": len(d[a.kind])})); return 0
    if a.cmd == "search":
        if not a.query:
            print(json.dumps({"error": "--query required"})); return 2
        hits = []
        for k in KINDS:
            for e in d.get(k, []):
                s = score(a.query, e["text"] + " " + e.get("name", ""))
                if s > 0:
                    hits.append({"kind": k, "id": e.get("id"), "score": round(s, 3),
                                 "age_days": round((now - e["ts"]) / 86400, 2),
                                 "name": e.get("name"), "text": e["text"][:300]})
        hits.sort(key=lambda h: -h["score"])
        print(json.dumps({"results": hits[:a.top]}, indent=2)); return 0
    if a.cmd == "forget":
        removed = 0
        for k in KINDS:
            keep = []
            for e in d.get(k, []):
                old = a.older_than_days is not None and (now - e["ts"]) > a.older_than_days * 86400
                if old:
                    removed += 1
                else:
                    keep.append(e)
            d[k] = keep
        save(a.db, d)
        print(json.dumps({"forgot": removed,
                          "note": "deliberate forgetting — accidental forgetting is the failure mode"}))
        return 0
    print(json.dumps({k: len(d.get(k, [])) for k in KINDS}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
