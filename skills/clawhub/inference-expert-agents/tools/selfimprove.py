#!/usr/bin/env python3
"""selfimprove.py — mechanical self-improvement loop (v2.1). TextGrad-flavored:
failures -> proposed amendments -> golden-set gate -> adopt/reject, plus
multi-armed-bandit ranking of the skill's learned rules (Reflexion/ExpeL-style).

record  --db M (--rule-id ID | --rule TEXT) --outcome win|loss
rank    --db M [--top N]         Wilson lower-bound ranking of rules
prune   --db M [--min-n 5] [--below 0.5]   delete consistently-lossy rules
propose --failures-file F        emit the amendment-drafting prompt (an LLM
                                 running this skill drafts the amendments)
adopt   --memory-db M --eval-db E --baseline-run N --candidate-run N2 [--min-delta 0.02]
                                 adopt/reject an amendment from measured pass-rate delta
status  --db M

State = the memory_kit db (rules carry id/wins/losses) + eval_regression runs.
Safety: amendments never auto-adopt on vibes — only on a measured golden-set
delta; every decision is logged; below-floor pass rates freeze adoption.
"""
import argparse, hashlib, json, math, os, random, sys, time

Z = 1.96

def load(db, default):
    try:
        with open(db, encoding="utf-8") as f:
            d = json.load(f)
        try:
            import stat as _stat
            st = os.stat(db)
            if st.st_mode & 0o177:
                os.chmod(db, 0o600)
        except Exception:
            pass
        if not isinstance(d, dict):
            raise ValueError("state db is not a JSON object")
        return d
    except FileNotFoundError:
        return json.loads(json.dumps(default))
    except Exception as e:
        raise ValueError(f"state file {db} is corrupt/unreadable (left untouched): {e}")

def save(db, d):
    os.makedirs(os.path.dirname(db) or ".", exist_ok=True)
    tmp = f"{db}.tmp-{os.getpid()}"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(d, f)
    os.replace(tmp, db)

def wilson(w, n):
    if n == 0:
        return 0.0
    p = w / n
    denom = 1 + Z * Z / n
    centre = p + Z * Z / (2 * n)
    rad = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return (centre - rad) / denom

def find_rule(rules, rid=None, text=None):
    for r in rules:
        if rid and r.get("id") == rid:
            return r
        if text and r.get("text", "")[:80] == text[:80]:
            return r
    return None

# v2.1.2: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r1 = sub.add_parser("record")
    r1.add_argument("--db", required=True)
    r1.add_argument("--rule-id"); r1.add_argument("--rule")
    r1.add_argument("--outcome", choices=["win", "loss"], required=True)
    r2 = sub.add_parser("rank")
    r2.add_argument("--db", required=True)
    r2.add_argument("--top", type=int, default=10)
    r2.add_argument("--method", choices=["wilson", "thompson"], default="wilson")
    r2.add_argument("--seed", type=int, default=None, help="RNG seed (reproducible thompson draws)")
    r3 = sub.add_parser("prune")
    r3.add_argument("--db", required=True)
    r3.add_argument("--min-n", type=int, default=5)
    r3.add_argument("--below", type=float, default=0.5)
    r4 = sub.add_parser("propose")
    r4.add_argument("--failures-file", required=True, help="JSON list of failure records")
    r5 = sub.add_parser("adopt")
    r5.add_argument("--memory-db", required=True)
    r5.add_argument("--eval-db", required=True, help="eval_regression.py db")
    r5.add_argument("--baseline-run", type=int, required=True)
    r5.add_argument("--candidate-run", type=int, required=True)
    r5.add_argument("--min-delta", type=float, default=0.02)
    r6 = sub.add_parser("status")
    r6.add_argument("--db", required=True)
    a = ap.parse_args()
    if getattr(a, "db", None):
        mem = load(a.db, {"reflection": [], "rule": [], "skill": [], "audit": []})
    elif a.cmd == "adopt":
        mem = load(a.memory_db, {"reflection": [], "rule": [], "skill": [], "audit": []})
    else:
        mem = {}
    if a.cmd == "status":
        rules = mem.get("rule", [])
        print(json.dumps({"rules": len(rules), "audits": len(mem.get("audit", [])),
                          "with_outcomes": sum(1 for r in rules if r.get("wins") or r.get("losses"))},
                         indent=2)); return 0
    if a.cmd == "record":
        r = find_rule(mem.get("rule", []), a.rule_id, a.rule)
        if r is None:
            if not a.rule:
                print(json.dumps({"error": "unknown --rule-id; pass --rule TEXT to create"})); return 2
            r = {"text": a.rule, "ts": time.time(),
                 "id": hashlib.sha1(a.rule.encode()).hexdigest()[:8]}
            mem.setdefault("rule", []).insert(0, r)
        r["wins"] = r.get("wins", 0) + (1 if a.outcome == "win" else 0)
        r["losses"] = r.get("losses", 0) + (1 if a.outcome == "loss" else 0)
        save(a.db, mem)
        print(json.dumps({"recorded": a.outcome, "rule_id": r["id"],
                          "wins": r["wins"], "losses": r["losses"]})); return 0
    if a.cmd == "rank":
        rng = random.Random(a.seed)
        rows = []
        for r in mem.get("rule", []):
            w, l = r.get("wins", 0), r.get("losses", 0)
            rows.append({"id": r.get("id"), "text": r["text"][:100],
                         "wins": w, "losses": l,
                         "win_rate": round(w / (w + l), 3) if w + l else None,
                         "wilson_lb": round(wilson(w, w + l), 3),
                         "thompson_sample": round(rng.betavariate(w + 1, l + 1), 3)})
        if a.method == "thompson":
            rows.sort(key=lambda x: -x["thompson_sample"])
            note = "thompson: one posterior sample per rule — re-run for exploration, fix --seed for stability"
        else:
            rows.sort(key=lambda x: -x["wilson_lb"])
            note = "untested rules sort at wilson_lb 0 — surface them, don't trust them"
        print(json.dumps({"ranking": rows[:a.top], "method": a.method, "note": note},
                         indent=2)); return 0
    if a.cmd == "prune":
        keep, dropped = [], []
        for r in mem.get("rule", []):
            n = r.get("wins", 0) + r.get("losses", 0)
            wr = r.get("wins", 0) / n if n else None
            if n >= a.min_n and wr is not None and wr < a.below:
                dropped.append({"id": r.get("id"), "text": r["text"][:80], "n": n,
                                "win_rate": round(wr, 2)})
            else:
                keep.append(r)
        mem["rule"] = keep
        mem.setdefault("audit", []).insert(0, {"ts": time.time(), "action": "prune",
                                               "dropped": dropped})
        save(a.db, mem)
        print(json.dumps({"pruned": len(dropped), "kept": len(keep), "details": dropped,
                          "audit": "logged to db.audit"}, indent=2)); return 0
    if a.cmd == "propose":
        fails = json.load(open(a.failures_file, encoding="utf-8"))
        lines = []
        for f in fails[:10]:
            if isinstance(f, dict):
                lines.append(f"- q: {str(f.get('q'))[:140]} | expected: {str(f.get('expected'))[:80]} | got: {str(f.get('got'))[:80]}")
            else:
                lines.append(f"- {str(f)[:160]}")
        print(json.dumps({
            "amendment_prompt": (
                "You are improving an inference skill's rules. FAILURES:\n" + "\n".join(lines) +
                "\n\nPropose AT MOST 3 amendments to the skill's rules/doctrine that would have "
                "prevented these failures. Output a JSON array: "
                '[{"amends":"<rule text to change or \'new rule\'>",'
                '"new_text":"<replacement rule, <=25 words>",'
                '"rationale":"<=15 words"}]. No prose outside the JSON.'),
            "textgrad_basis": "textual feedback as gradient (arXiv:2406.07496) — but adoption is GATED, see adopt",
            "next": "run evals with the amended rules, then selfimprove.py adopt",
        }, indent=2)); return 0
    ev = load(a.eval_db, {"runs": [], "queue": [], "adoptions": []})
    base = next((r for r in ev.get("runs", []) if r.get("id") == a.baseline_run), None)
    cand = next((r for r in ev.get("runs", []) if r.get("id") == a.candidate_run), None)
    if not base or not cand:
        print(json.dumps({"error": "run ids not found in eval db"})); return 2
    delta = round(cand["pass_rate"] - base["pass_rate"], 4)
    decision = "ADOPT" if delta >= a.min_delta else "REJECT"
    frozen = cand["pass_rate"] < 0.5
    if frozen:
        decision = "FREEZE (candidate pass rate below 0.5 — fix basics before self-modifying)"
    ev.setdefault("adoptions", []).insert(0, {
        "ts": time.time(), "baseline": a.baseline_run, "candidate": a.candidate_run,
        "delta": delta, "decision": decision})
    mem.setdefault("audit", []).insert(0, {"ts": time.time(), "action": "adopt-" + decision.split()[0],
                                           "delta": delta})
    save(a.eval_db, ev); save(a.memory_db, mem)
    print(json.dumps({"decision": decision, "delta_pass_rate": delta,
                      "min_delta": a.min_delta,
                      "logged": ["eval_db.adoptions", "memory_db.audit"]}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
