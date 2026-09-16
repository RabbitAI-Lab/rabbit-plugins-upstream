#!/usr/bin/env python3
"""deep_research.py — deep-research loop planner + source tiering (F27, F28, F29).

plan: builds the plan->search->read->synthesize->verify loop with stopping
rules. tier: classify sources for trust weighting (primary/secondary/tertiary +
paywall/low-quality flags). Stdlib-only, read-only.
"""
import argparse, json, re, sys

STEPS = [
    {"phase": "plan", "do": "decompose the question into sub-questions; declare what evidence would settle each"},
    {"phase": "search", "do": "broad pass; collect candidate sources + URLs"},
    {"phase": "read", "do": "fetch each candidate; extract claims with provenance (quote + locator)"},
    {"phase": "synthesize", "do": "answer per sub-question ONLY from extracted claims; mark conflicts"},
    {"phase": "verify", "do": "cross-check every load-bearing claim across >=2 independent sources; run grounding gate"},
    {"phase": "report", "do": "deliver with confidence per sub-question + explicit unknowns"},
]

TIER_RULES = [
    (r"\.(gov|edu)\.|arxiv\.org|doi\.org|pubmed|nature\.com|science\.org|acm\.org|ieee\.org", "primary",
     "peer-reviewed or official"),
    (r"\.(org)\b|reuters\.com|apnews\.com|bbc\.(com|co\.uk)|\.gov\.uk", "secondary", "reputable institutional"),
    (r"medium\.com|substack\.com|blogspot|wordpress\.com|\.blog|reddit\.com|quora\.com", "tertiary",
     "opinion/UGC — treat as leads only, verify elsewhere"),
    (r"wikipedia\.org", "tertiary", "tertiary summary — use for orientation and its citations, not as evidence"),
]

def classify(url):
    u = url.lower()
    for pat, tier, note in TIER_RULES:
        if re.search(pat, u):
            return {"url": url, "tier": tier, "note": note}
    return {"url": url, "tier": "unknown",
            "note": "unclassified — apply secondary standards; verify before citing"}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("plan")
    s1.add_argument("--question", required=True)
    s1.add_argument("--max-sources", type=int, default=12)
    s1.add_argument("--time-budget-min", type=int, default=30)
    s2 = sub.add_parser("tier")
    s2.add_argument("--urls", required=True, help="JSON array of URLs")
    a = ap.parse_args()
    if a.cmd == "tier":
        tiers = [classify(u) for u in json.loads(a.urls)]
        counts = {}
        for t in tiers:
            counts[t["tier"]] = counts.get(t["tier"], 0) + 1
        print(json.dumps({"sources": tiers, "tier_counts": counts,
                          "policy": "load-bearing claims need >=1 primary or >=2 independent secondary sources"},
                         indent=2))
        return 0
    print(json.dumps({
        "question": a.question, "max_sources": a.max_sources,
        "time_budget_min": a.time_budget_min,
        "loop": STEPS,
        "stopping_rules": [
            "stop search when a sub-question has >=2 independent supporting sources or is declared unknown",
            "stop when time/source budget exhausted — deliver with confidence labels",
            "never loop past budget chasing completeness; diminishing returns"],
        "note": "TTS law: more compute -> better; but verify beats generate — reserve ~1/3 of budget for the verify phase",
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
