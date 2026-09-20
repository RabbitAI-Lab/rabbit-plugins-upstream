#!/usr/bin/env python3
"""debate.py — multi-agent debate protocol helper (F44, F45).

Builds the round schedule for multiagent debate (Du et al.) or heterogeneous
expert debate (A-HMAD), and computes the consensus + stability from final-round
positions. Stdlib-only, read-only.
"""
import argparse, json, sys

def schedule(agents, rounds, heterogeneous):
    proto = []
    for r in range(1, rounds + 1):
        for ag in agents:
            proto.append({
                "round": r, "agent": ag,
                "prompt_template": ("Round {r}: Here are the other agents' current answers "
                                    "and critiques. Critique flaws (facts, logic, missing cases) "
                                    "and update your answer or defend it." if r > 1
                                    else "Round 1: Answer independently; show reasoning."),
            })
    return {"protocol": proto,
            "roles": agents if not heterogeneous else
                     [f"{a} (specialist: give it a distinct domain/system prompt)" for a in agents],
            "grounding": "Du et al. 2023 (arXiv:2305.14325); A-HMAD reports -18% hallucinations on TruthfulQA"}

def consensus(final_positions):
    if not final_positions:
        return {"error": "no positions provided"}
    norm = {}
    for p in final_positions:
        key = " ".join(sorted(p["answer"].lower().split()))
        norm.setdefault(key, []).append(p["agent"])
    best = max(norm.values(), key=len)
    agree = len(best) / max(1, len(final_positions))
    return {"consensus_agents": best, "agreement": round(agree, 3),
            "n_distinct_positions": len(norm),
            "verdict": ("stable-consensus" if agree >= 0.67 else
                        "contested — do not treat as settled; escalate to L3 verification"),
            "note": "agents correcting each other is the documented value; all-wrong-consensus is possible — verify load-bearing facts regardless"}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("schedule")
    s1.add_argument("--agents", required=True, help='JSON ["a","b","c"]')
    s1.add_argument("--rounds", type=int, default=3)
    s1.add_argument("--heterogeneous", action="store_true")
    s2 = sub.add_parser("consensus")
    s2.add_argument("--positions", required=True,
                    help='JSON [{"agent":"a","answer":"42"},...] (final round)')
    a = ap.parse_args()
    if a.cmd == "schedule":
        print(json.dumps(schedule(json.loads(a.agents), a.rounds, a.heterogeneous), indent=2))
    else:
        print(json.dumps(consensus(json.loads(a.positions)), indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
