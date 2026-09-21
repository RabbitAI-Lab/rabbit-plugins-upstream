#!/usr/bin/env python3
"""cascade.py — cost-aware model cascade/router planner (F22, F23, F25).

FrugalGPT/RouteLLM-style: given candidate models (name, relative cost, quality
estimate) and a query's confidence/quality need, produce the cheapest cascade
that meets the target, plus expected savings vs always-large; optionally a
speculative draft-verify pairing. Stdlib-only, read-only.
"""
import argparse, json, sys

def plan_cascade(models, target_quality, confidence):
    ms = sorted(models, key=lambda m: m["cost"])
    plan, expected_cost, esc = [], 0.0, 1.0  # esc = P(reaching this step)
    for m in ms:
        expected_cost += esc * m["cost"]
        plan.append({"step": len(plan) + 1, "model": m["name"], "cost": m["cost"],
                     "enter_if": f"previous step confidence < {round(confidence, 2)} or quality below target",
                     "stop_if": f"answer confidence >= {round(confidence, 2)} and est quality >= {target_quality}"})
        if m["quality"] >= target_quality:
            break
        esc *= (1 - confidence)  # P(escalate past this model)
    baseline = max(m["cost"] for m in models) if models else 0
    return {"cascade": plan, "expected_cost_units": round(expected_cost, 4),
            "always_large_cost_units": baseline,
            "expected_savings_pct": round(100 * (1 - expected_cost / baseline), 1) if baseline else None,
            "rule": "verify answers from cheap models with the grounding gate before delivery (quality floor)"}

def speculative_pair(models):
    ms = sorted(models, key=lambda m: m["cost"])
    if len(ms) < 2:
        return None
    return {"draft_model": ms[0]["name"], "verify_model": ms[-1]["name"],
            "pattern": "draft K tokens cheaply, verify with large model in one pass",
            "expected_speedup": "2-3x (Leviathan et al., ICML 2023) at identical output distribution"}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True,
                    help='JSON [{"name":"small","cost":0.05,"quality":0.8},...]')
    ap.add_argument("--target-quality", type=float, default=0.9)
    ap.add_argument("--confidence", type=float, default=0.85,
                    help="confidence that the query is easy enough for cheaper tiers")
    ap.add_argument("--with-speculative", action="store_true")
    a = ap.parse_args()
    models = json.loads(a.models)
    if not models:
        print(json.dumps({"error": "no models"})); return 2
    out = plan_cascade(models, a.target_quality, a.confidence)
    if a.with_speculative:
        out["speculative_pair"] = speculative_pair(models)
    print(json.dumps(out, indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main())
