#!/usr/bin/env python3
"""triage.py — difficulty triage for the inference-expert-agents skill (F1).

Classifies a query trivial/standard/hard and returns a preset deliberation
budget. Stdlib-only, read-only.
"""
import argparse, json, re, sys

HARD = [r"\bprove\b", r"\bderive\b", r"\btheorem\b", r"\boptimi[sz]e\b",
        r"\barchitect\b", r"\bdesign\b.*\bsystem\b", r"\blegal\b", r"\bmedical\b",
        r"\bdiagnos", r"\binvest", r"\bstrategy\b", r"\bcompare\b.*\bvs\b",
        r"\bcausal", r"\bmeta-?analysis\b", r"\bproof\b", r"\bwhy\b.*\?",
        r"\bmulti-?step\b", r"\bplan\b.*\bexecute\b",
        # v2.1.0: puzzle / paradox / planning / clinical-safety / pressure families
        r"\bmonty\s+hall\b", r"\bstay\s+or\s+switch\b", r"\bparadox\b",
        r"\bnewcomb\b", r"\bgrandfather\b", r"\btheseus\b", r"\bsorites\b",
        r"\bliar\b", r"\bunexpected\s+hanging\b",
        r"\bnegligenc[ey]\b", r"\btort\b", r"\bduty\b.*\bcare\b",
        r"\bmens\s+rea\b", r"\bbreach\b.*\bduty\b",
        r"\bfalse[- ]?belief\b", r"\btheory\b.*\bmind\b",
        r"\bsally\b.*\bmarble\b", r"\bmarble\b.*\bbasket\b",
        r"\bodd[- ]one[- ]out\b", r"\bminimum\b.*\bmoves\b",
        r"\bcounterfactual\b", r"\bcrates?\b",
        r"\bplan\b.*\b(steps?|moves?|route)\b",
        r"\bibuprofen\b", r"\bwarfarin\b", r"\bnsaid\b", r"\bdos(e|age|ing)\b",
        r"\bcontraindicat", r"\bagree with me\b", r"\bno hedging\b"]
STANDARD = [r"\bexplain\b", r"\bsummar", r"\bhow\b.*\?", r"\bwhat\b.*\?",
            r"\btranslate\b", r"\bwrite\b", r"\bdraft\b"]
MATH = [r"\d+\s*[\+\-\*/^]", r"\bcalculate\b", r"\bsolve\b", r"\bequation\b",
        r"\bprobability\b", r"\bintegra", r"\bstatistic"]

def triage(text):
    low = text.lower()
    words = len(low.split())
    signals = []
    hard = sum(1 for p in HARD if re.search(p, low))
    std = sum(1 for p in STANDARD if re.search(p, low))
    mathy = sum(1 for p in MATH if re.search(p, low))
    qmarks = text.count("?")
    parts = len(re.split(r"\b(?:and then|also|additionally|plus|;)\b", low))
    if hard: signals.append(f"hard_keywords={hard}")
    if mathy: signals.append(f"math_present={mathy}")
    if parts > 1: signals.append(f"multi_part={parts}")
    if qmarks > 1: signals.append(f"multi_question={qmarks}")
    if words > 150: signals.append(f"long_prompt={words}w")
    score = hard * 2 + mathy + (parts - 1) + max(0, qmarks - 1) + (1 if words > 150 else 0)
    if score >= 2 or hard >= 1:
        d = "hard"
    elif score == 1 or std >= 1 or words > 40:
        d = "standard"
    else:
        d = "trivial"
    presets = {
        "trivial":  {"rung": "L0", "samples": 1, "verification_budget_frac": 0.0,
                     "cost_cap_multiplier": 1, "note": "single fast pass; never escalate"},
        "standard": {"rung": "L1", "samples": 3, "verification_budget_frac": 0.25,
                     "cost_cap_multiplier": 4, "note": "self-consistency on reasoning parts"},
        "hard":     {"rung": "L2", "samples": 5, "verification_budget_frac": 0.33,
                     "cost_cap_multiplier": 10, "note": "decompose+verify; tool-ground load-bearing claims"},
    }[d]
    return {"difficulty": d, "score": score, "signals": signals, "words": words,
            "preset": presets}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text"); ap.add_argument("--text-file")
    a = ap.parse_args()
    if a.text_file:
        text = open(a.text_file, encoding="utf-8", errors="replace").read()
    elif a.text is not None:
        text = a.text
    else:
        print(json.dumps({"error": "provide --text or --text-file"})); return 2
    print(json.dumps(triage(text), indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main())
