#!/usr/bin/env python3
"""
inference_scorecard.py — rubric scorer for the inference-expert-agents skill.

Grades an agent answer against the skill's inference-expert rubric and emits
JSON. Dependency-free, read-only (writes nothing), sandbox-safe.

Usage:
  python3 inference_scorecard.py --text-file answer.md --difficulty hard
  python3 inference_scorecard.py --text "..." --difficulty trivial
Exit codes: 0 = scored; 2 = usage error.
"""
import argparse
import json
import re
import sys

HEDGES = ["possibly", "likely", "may", "might", "could", "approximately",
          "around", "estimate", "roughly", "i think", "uncertain"]
ABSTAIN = ["i don't know", "i do not know", "could not verify", "cannot verify",
           "cannot confirm", "not determinable", "unable to verify",
           "no reliable data", "no reliable source", "uncertain", "unsure",
           "unclear", "might be wrong", "may be wrong", "might be incorrect",
           "may be incorrect"]
# Whole-phrase match (case-insensitive): avoids substring false positives
# such as "uncertain" inside "uncertainty".
_ABSTAIN_RE = re.compile(r'\b(?:' + '|'.join(re.escape(p) for p in ABSTAIN) + r')\b',
                         flags=re.IGNORECASE)
VERIF = ["verified", "confirmed", "primary source", "doi", "pmid", "arxiv",
         "according to", "retrieved", "checked", "grounded", "per the source",
         "citation", "reference"]
MARKERS = ["[uncertain", "[verified", "[unverified", "confidence:", "±"]

def split_claims(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.strip().split()) >= 6]

def score(text, difficulty):
    low = text.lower()
    words = len(low.split())
    claims = split_claims(text)
    n = max(1, len(claims))
    factual = [c for c in claims if re.search(r"\d|said|reported|study|paper|"
               r"according|research|percent|%", c, re.I)]
    hedges = sum(1 for h in HEDGES if h in low)
    abstains = _ABSTAIN_RE.findall(low)
    verifs = sum(1 for v in VERIF if v in low)
    marks = sum(1 for m in MARKERS if m in low)
    digits = len(re.findall(r"\d+(?:\.\d+)?", text))

    d = {
        "words": words,
        "claims_detected": len(claims),
        "factual_claims": len(factual),
        "numeric_claims": digits,
        "verification_evidence_hits": verifs,
        "uncertainty_markers": marks + hedges,
        "abstention_language": len(abstains),
    }
    # Verification coverage: verif evidence relative to factual claim load
    load = max(1, len(factual) + min(digits, 10) // 2)
    d["verification_coverage"] = round(min(1.0, verifs / load), 2)
    # FActScore-flavored (F7): share of atomic factual claims carrying support
    d["atomic_claim_support"] = round(min(1.0, verifs / max(1, len(factual))), 2) if factual else 1.0
    # Uncertainty calibration: some marking is good; a wall of hedges is not
    d["uncertainty_calibration"] = round(min(1.0, (marks * 2 + hedges) / max(3, len(factual) * 0.8)), 2)
    d["abstention_present"] = 1 if abstains else 0

    # Escalation match: hard tasks must show verification, trivial must not overdo
    if difficulty == "hard":
        d["escalation_match"] = 1 if (verifs >= 1 or abstains) else 0
    elif difficulty == "trivial":
        d["escalation_match"] = 1 if (verifs == 0 and words < 400) else 0
    else:
        d["escalation_match"] = 1 if (verifs + marks) <= max(2, len(factual)) else 0

    dims = [d["verification_coverage"], d["uncertainty_calibration"],
            d["escalation_match"]]
    d["overall"] = round(sum(dims) / len(dims), 2)
    lowest = ["verification_coverage", "uncertainty_calibration",
              "escalation_match"][dims.index(min(dims))]
    d["weakest_dimension"] = lowest
    d["advice"] = {
        "verification_coverage": "Add primary-source checks for factual/numeric claims (L2/L3).",
        "uncertainty_calibration": "Mark uncertainty explicitly or trim unjustified hedging.",
        "escalation_match": "Mismatch between difficulty and inference effort — re-triage.",
        "atomic_claim_support": "FActScore-style: too many atomic factual claims lack per-claim support — decompose and verify each (grounding_gate).",
    }[lowest]
    return d

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text")
    ap.add_argument("--text-file")
    ap.add_argument("--difficulty", choices=["trivial", "standard", "hard"],
                    default="standard")
    a = ap.parse_args()
    if a.text_file:
        try:
            with open(a.text_file, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError as e:
            print(json.dumps({"error": str(e)}))
            return 2
    elif a.text is not None:
        text = a.text
    else:
        print(json.dumps({"error": "provide --text or --text-file"}))
        return 2
    print(json.dumps({"difficulty": a.difficulty,
                      "rubric": score(text, a.difficulty)}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
