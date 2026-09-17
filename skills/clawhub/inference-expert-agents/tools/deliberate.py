#!/usr/bin/env python3
"""deliberate.py — escalation-ladder planner for inference-expert-agents (F2-F6).

Turns a difficulty triage + budget into an executable rung-by-rung plan with
adaptive budgets, early-exit thresholds, budget forcing, and over/under-thinking
audit fields. Stdlib-only, read-only.
"""
import argparse, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from triage import triage
except Exception:
    def triage(t):
        return {"preset": {"rung": "L1", "samples": 3, "verification_budget_frac": 0.25}}

RUNGS = {
    "L0": "single fast pass",
    "L1": "self-consistency (N sampled chains, majority vote)",
    "L2": "claim decomposition + self-check",
    "L3": "tool-grounded verification (search / code execution)",
    "L4": "draft-verify generate-critique loop with rubric",
}

def plan(difficulty, budget_tokens, wall_cap_s=None, cost_cap_usd=None,
         force_final_at=None, conf_exit=0.90, abort_floor=0.20):
    presets = {
        "trivial":  {"rung": "L0", "samples": 1, "verification_budget_frac": 0.0},
        "standard": {"rung": "L1", "samples": 3, "verification_budget_frac": 0.25},
        "hard":     {"rung": "L2", "samples": 5, "verification_budget_frac": 0.33},
    }
    p = presets.get(difficulty, presets["standard"])
    order = ["L0", "L1", "L2", "L3", "L4"]
    start = order.index(p["rung"])
    per_rung_frac = [0.0, 0.20, 0.25, 0.33, 0.22]
    steps, used = [], 0
    for r in order[start:]:
        frac = per_rung_frac[order.index(r)]
        btok = int(budget_tokens * frac) or int(budget_tokens * 0.2)
        used += btok
        steps.append({
            "rung": r, "pattern": RUNGS[r],
            "token_budget": btok,
            "enter_if": ("confidence < %.2f at previous rung" % conf_exit) if r != "L0" else "always",
            "stop_if": ("confidence >= %.2f (early exit) or rung budget exhausted" % conf_exit),
            "abort_if": ("confidence <= %.2f after 50%% of rung budget — likely unsolvable/ill-posed; consider abstention" % abort_floor) if r in ("L1", "L2", "L3") else None,
        })
    if force_final_at:
        steps.append({"rung": "FORCE", "pattern": "budget forcing: emit Final Answer now",
                      "token_budget": 0, "enter_if": "total tokens >= %d" % force_final_at,
                      "stop_if": None, "abort_if": None})
    return {
        "difficulty": difficulty,
        "budget": {"total_tokens": budget_tokens, "wall_cap_s": wall_cap_s,
                   "cost_cap_usd": cost_cap_usd, "force_final_at_tokens": force_final_at},
        "adaptive": True,
        "early_exit": {"confidence_upper": conf_exit,
                       "unsolvable_abort_floor": abort_floor},
        "reserved_verification_frac": p["verification_budget_frac"],
        "samples_n": p["samples"],
        "audit": {"overthinking_flag": "trivial/standard plans must not include L3+",
                  "underthinking_flag": "hard plans must include L2 or L3",
                  "metric_hint": "track overthinking-AUC / underthinking-accuracy (OptimalThinkingBench-style)"},
        "plan": steps,
    }

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--difficulty", choices=["trivial", "standard", "hard"], required=True)
    ap.add_argument("--budget-tokens", type=int, default=2000)
    ap.add_argument("--wall-cap-s", type=float, default=None)
    ap.add_argument("--cost-cap-usd", type=float, default=None)
    ap.add_argument("--force-final-at", type=int, default=None,
                    help="budget forcing: force Final Answer at this token count (F5)")
    ap.add_argument("--conf-exit", type=float, default=0.90)
    ap.add_argument("--abort-floor", type=float, default=0.20)
    a = ap.parse_args()
    print(json.dumps(plan(a.difficulty, a.budget_tokens, a.wall_cap_s,
                          a.cost_cap_usd, a.force_final_at, a.conf_exit,
                          a.abort_floor), indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
