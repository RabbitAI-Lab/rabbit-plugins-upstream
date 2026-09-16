#!/usr/bin/env python3
"""judge_panel.py — LLM-judge ensembles with bias controls (F14, F15, F16, F17).

Aggregates multiple judge verdicts: simple majority, minority-veto (robust to
agreeableness bias), or weighted majority voting with per-judge FP/FN weights;
plus a CALM-inspired 12-bias checklist to embed in judge prompts.
Stdlib-only, read-only.
"""
import argparse, json, sys

CHECKLIST = [
    "position bias — judges favor the first/last option; randomize order",
    "style/verbosity bias — longer or prettier answers win; mask formatting",
    "bandwagon bias — claimed popularity shifts judgment; omit opinions",
    "authority bias — attributed 'expert' names shift judgment; blind sources",
    "self-preference bias — judges favor outputs from their own family",
    "length bias — penalize truncation artifacts, not substance",
    "sentiment bias — positive tone inflates quality scores",
    "fabricated-citation bias — fake references sway judgment; verify refs",
    "sycophancy — judge agrees with the asker's implied preference",
    "confirmation bias — judge seeks evidence for the expected verdict",
    "anchor bias — first-seen score anchors later scores; score independently",
    "capability leniency — stronger examinees get lenient scores; calibrate weights",
]

def aggregate(verdicts, mode, fp=None, fn=None):
    passes = [v for v in verdicts if v.get("verdict") == "pass"]
    fails = [v for v in verdicts if v.get("verdict") == "fail"]
    out = {"n_judges": len(verdicts),
           "per_judge": [{"judge": v.get("judge"), "verdict": v.get("verdict")}
                         for v in verdicts]}
    if mode == "majority":
        out["consensus"] = "pass" if len(passes) > len(fails) else "fail"
        out["rationale"] = "simple majority"
    elif mode == "minority-veto":
        out["consensus"] = "fail" if fails else "pass"
        out["rationale"] = ("any single fail vetoes (robust to agreeableness bias — "
                            "validators rarely reject, so majority inflates pass rates)")
    elif mode == "weighted":
        pw = fw = 0.0
        for v in verdicts:
            j = v.get("judge", "?")
            w = 1.0 / ((fp or {}).get(j, 0.05) + (fn or {}).get(j, 0.05) + 1e-9)
            if v.get("verdict") == "pass":
                pw += w
            else:
                fw += w
            out.setdefault("weights", {})[j] = round(w, 2)
        out["consensus"] = "pass" if pw > fw else "fail"
        out["rationale"] = "weighted by inverse estimated FP+FN rates (label-free WMV)"
    else:
        out["error"] = "mode must be majority|minority-veto|weighted"
    out["agreement"] = round(max(len(passes), len(fails)) / max(1, len(verdicts)), 3)
    out["note"] = ("low agreement -> judges disagree; route to stronger evidence (L3) "
                   "instead of trusting the ensemble")
    return out

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("aggregate")
    a1.add_argument("--verdicts", required=True,
                    help='JSON [{"judge":"gpt","verdict":"pass"},...]')
    a1.add_argument("--mode", choices=["majority", "minority-veto", "weighted"],
                    default="majority")
    a1.add_argument("--fp", help='JSON {"judge": fp_rate}')
    a1.add_argument("--fn", help='JSON {"judge": fn_rate}')
    a2 = sub.add_parser("bias-checklist")
    a = ap.parse_args()
    if a.cmd == "bias-checklist":
        print(json.dumps({"n_biases": len(CHECKLIST), "checklist": CHECKLIST,
                          "usage": "embed as constraints in judge prompts; randomize order; mask style"},
                         indent=2))
        return 0
    verdicts = json.loads(a.verdicts)
    fp = json.loads(a.fp) if a.fp else None
    fn = json.loads(a.fn) if a.fn else None
    print(json.dumps(aggregate(verdicts, a.mode, fp, fn), indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
