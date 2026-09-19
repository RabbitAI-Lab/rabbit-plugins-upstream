#!/usr/bin/env python3
"""eval_regression.py — golden-set regression gates + baseline comparison +
continuous-eval cron + annotation queue + runs ledger (F39, F40, F47).

Golden sets are declared per project as JSON lists:
  [{"q": "...", "a_expect": "exact or substring", "mode": "exact|contains",
    "max_uncertainty": 0.4, "tags": ["smoke","math"]}]
The runner evaluates harness outputs against them, enforces pass-rate gates,
compares two runs (baseline vs candidate), and maintains a runs ledger +
annotation queue of failing cases. Stdlib-only; state in opt-in --db (0600).
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
        return {"runs": [], "queue": []}
    _ensure_perm(db)
    try:
        d = json.load(open(db, encoding="utf-8"))
        if not isinstance(d, dict):
            raise ValueError("state db is not a JSON object")
        d.setdefault("runs", []); d.setdefault("queue", [])
        return d
    except FileNotFoundError:
        return {"runs": [], "queue": []}
    except Exception as e:
        raise ValueError(f"state file {db} is corrupt/unreadable (left untouched): {e}")

def save(db, d):
    os.makedirs(os.path.dirname(db) or ".", exist_ok=True)
    _dump_json(db, d)

def case_ok(case, got, uncertainty=None):
    exp, mode = case["a_expect"], case.get("mode", "contains")
    if mode == "exact":
        ok = str(got).strip() == str(exp).strip()
    else:
        ok = str(exp).lower() in str(got).lower()
    u_ok = uncertainty is None or uncertainty <= case.get("max_uncertainty", 1.0)
    return ok and u_ok

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "compare", "ledger", "queue", "schedule"])
    ap.add_argument("--db", default=None,
                    help="JSON state file; state is strictly opt-in — nothing is written or read without it")
    ap.add_argument("--golden", help="JSON array of golden cases")
    ap.add_argument("--outputs", help='JSON array of answers, same order as golden')
    ap.add_argument("--uncertainties", help='JSON array of uncertainty floats (optional)')
    ap.add_argument("--gate", type=float, default=0.9, help="min pass rate")
    ap.add_argument("--baseline", type=int, help="run id to compare against")
    ap.add_argument("--candidate", type=int, help="run id (default: latest)")
    ap.add_argument("--tags", help="comma tags to filter golden cases")
    ap.add_argument("--cron", help='cron expr, e.g. "0 */6 * * *"')
    a = ap.parse_args()
    if a.cmd == "schedule":
        print(json.dumps({"recommended_cron": a.cron or "0 */6 * * *",
                          "command": "eval_regression.py run --golden GOLDEN.json --outputs OUTS.json --gate 0.9",
                          "note": "schedule evals on every prompt/pipeline change; treat like CI"}))
        return 0
    d = load(a.db)
    if getattr(a, "db", None) is None:
        print(json.dumps({"error": "no --db given — persistent state is opt-in; "
                                  "pass --db PATH to enable it",
                          "state": "none"}))
        return 2
    if a.cmd == "run":
        def _load_arg(v, name):
            try:
                if os.path.exists(v):
                    with open(v, encoding="utf-8") as f:
                        return json.load(f)
                return json.loads(v)
            except Exception as e:
                print(json.dumps({"error": f"--{name} is neither a readable file nor valid JSON: {e}"}))
                return None
        golden = _load_arg(a.golden, "golden")
        outs = _load_arg(a.outputs, "outputs")
        if golden is None or outs is None:
            return 2
        unc = None
        if a.uncertainties:
            unc = _load_arg(a.uncertainties, "uncertainties")
            if unc is None or not isinstance(unc, list):
                if unc is None:
                    return 2
                print(json.dumps({"error": "--uncertainties must be a JSON array of floats"})); return 2
        if len(golden) != len(outs):
            print(json.dumps({"error": "golden/outputs length mismatch"})); return 2
        bad = [i for i, c in enumerate(golden)
               if not isinstance(c, dict) or "q" not in c or "a_expect" not in c]
        if bad:
            print(json.dumps({"error": f"golden cases at indexes {bad[:5]} lack 'q'/'a_expect' fields",
                              "expected_shape": '{"q": str, "a_expect": str, "mode": "exact|contains"}'}))
            return 2
        unc = unc if unc is not None else [None] * len(golden)
        tags = set(a.tags.split(",")) if a.tags else None
        results = []
        for c, o, u in zip(golden, outs, unc):
            if tags and not set(c.get("tags", [])) & tags:
                continue
            ok = case_ok(c, o, u)
            results.append({"q": c["q"][:120], "pass": ok,
                            "expected": str(c["a_expect"])[:120]})
            if not ok:
                d["queue"].append({"ts": time.time(), "q": c["q"],
                                   "expected": c["a_expect"], "got": str(o)[:500],
                                   "resolved": False})
        pr = sum(1 for r in results if r["pass"]) / max(1, len(results))
        rid = len(d["runs"]) + 1
        d["runs"].append({"id": rid, "ts": time.time(), "pass_rate": round(pr, 4),
                          "n": len(results), "gate": a.gate,
                          "verdict": "pass" if pr >= a.gate else "FAIL"})
        save(a.db, d)
        print(json.dumps({"run_id": rid, "pass_rate": round(pr, 4), "gate": a.gate,
                          "verdict": "pass" if pr >= a.gate else "FAIL — block promotion",
                          "failures": [r for r in results if not r["pass"]],
                          "queued_for_annotation": len(d["queue"])}, indent=2))
        return 0
    if a.cmd == "compare":
        base = next((r for r in d["runs"] if r["id"] == a.baseline), None)
        cand = next((r for r in d["runs"] if r["id"] == (a.candidate or (d["runs"][-1]["id"] if d["runs"] else None))), None)
        if not base or not cand:
            print(json.dumps({"error": "run ids not found"})); return 2
        delta = round(cand["pass_rate"] - base["pass_rate"], 4)
        print(json.dumps({"baseline": base["id"], "candidate": cand["id"],
                          "delta_pass_rate": delta,
                          "verdict": "no-regression" if delta >= 0 else "REGRESSION — block promotion"}))
        return 0
    if a.cmd == "ledger":
        print(json.dumps(d["runs"][-20:], indent=2)); return 0
    if a.cmd == "queue":
        open_q = [q for q in d["queue"] if not q.get("resolved")]
        for i, q in enumerate(open_q):
            q["queue_id"] = i
        print(json.dumps({"open": len(open_q), "items": open_q[:50]}, indent=2)); return 0
    print(json.dumps({"recommended_cron": a.cron or "0 */6 * * *",
                      "command": "eval_regression.py run --golden GOLDEN.json --outputs OUTS.json --gate 0.9",
                      "note": "schedule evals on every prompt/pipeline change; treat like CI"}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
