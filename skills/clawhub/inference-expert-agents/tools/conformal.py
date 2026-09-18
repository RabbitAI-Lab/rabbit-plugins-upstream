#!/usr/bin/env python3
"""conformal.py — calibrated abstention & risk control (F18, F19, F20, F21).

CIC/CP-flavored finite-sample calibration: converts an uncertainty score into
an accept/abstain threshold whose accepted-error rate has a Hoeffding upper
bound below the target risk alpha. Also: coverage-risk curve, escalation gate
(UCCI-style), and per-answer gate decisions. Stdlib-only, read-only.
"""
import argparse, json, math, sys

def ub(err, n, delta):
    return err + math.sqrt(math.log(1 / delta) / (2 * max(1, n)))

def calibrate(labels, alpha, delta):
    # accepted = u <= t (lower uncertainty = more confident). Choose the LARGEST
    # threshold whose high-probability upper bound on accepted-error <= alpha.
    us = sorted({l["u"] for l in labels})
    best = None
    for t in us:
        acc = [l for l in labels if l["u"] <= t]
        n = len(acc)
        err = sum(1 for l in acc if not l["correct"]) / n if n else 1.0
        b = ub(err, n, delta)
        if b <= alpha:
            best = (t, err, b, n)
    if best is None:
        return {"threshold": None, "note": "no threshold achieves risk<=alpha; abstain-by-default"}
    t, err, b, n = best
    return {"threshold": t, "accepted_n": n, "coverage": round(n / len(labels), 3),
            "empirical_error": round(err, 4), "hoeffding_ub": round(b, 4),
            "alpha": alpha, "delta": delta}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors, fail


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c1 = sub.add_parser("calibrate")
    c1.add_argument("--labels-file", required=True, help='JSON array [{"u":0.2,"correct":true},...] (u=uncertainty, lower=confident)')
    c1.add_argument("--alpha", type=float, default=0.10)
    c1.add_argument("--delta", type=float, default=0.05)
    c2 = sub.add_parser("curve")
    c2.add_argument("--labels-file", required=True)
    c2.add_argument("--delta", type=float, default=0.05)
    c3 = sub.add_parser("gate")
    c3.add_argument("--threshold", type=float, required=True)
    c3.add_argument("--u", type=float, required=True, help="uncertainty of the current answer")
    c3.add_argument("--escalate-above", type=float, default=None,
                    help="UCCI-style: escalate to stronger model/verifier when u in (threshold, escalate_above]")
    a = ap.parse_args()

    # v3.0.0 — validate the risk parameters and the label schema. Before this,
    # `--delta 0` reached math.log(1/0) and `--alpha 5` "calibrated" against a
    # target risk above 1 (meaningless), and a labels file with the wrong shape
    # surfaced as a bare "TypeError: list indices must be integers, not str"
    # with no hint about the schema the flag documents.
    for name, val in (("--alpha", getattr(a, "alpha", None)), ("--delta", getattr(a, "delta", None))):
        if val is not None and not (0.0 < val < 1.0):
            return fail(f"{name} must be in (0, 1), got {val}",
                        hint="--alpha is the target accepted-error rate (default 0.10); "
                             "--delta is the failure probability of the bound (default 0.05)")
    if a.cmd == "gate":
        if a.escalate_above is not None and a.escalate_above <= a.threshold:
            return fail(f"--escalate-above ({a.escalate_above}) must exceed --threshold "
                        f"({a.threshold}), or the escalation band is empty and unreachable",
                        hint="escalation covers u in (threshold, escalate_above]")
        accept = a.u <= a.threshold
        out = {"u": a.u, "threshold": a.threshold,
               "decision": "accept" if accept else "abstain"}
        if a.escalate_above and not accept and a.u <= a.escalate_above:
            out["decision"] = "escalate"
            out["note"] = "uncertainty above accept threshold but below escalation ceiling — try stronger rung/model before abstaining"
        print(json.dumps(out, indent=2)); return 0
    labels = json.load(open(a.labels_file, encoding="utf-8"))
    if not isinstance(labels, list) or not labels:
        return fail("--labels-file must be a non-empty JSON array",
                    hint='one object per past answer: [{"u": 0.2, "correct": true}, ...] '
                         "(u = uncertainty, lower = more confident)")
    bad = [i for i, l in enumerate(labels)
           if not isinstance(l, dict) or "u" not in l or "correct" not in l]
    if bad:
        return fail(f"{len(bad)} label row(s) are missing 'u' or 'correct' "
                    f"(first at index {bad[0]})",
                    hint='required shape: {"u": <float 0..1>, "correct": <bool>}')
    if a.cmd == "calibrate":
        print(json.dumps(calibrate(labels, a.alpha, a.delta), indent=2)); return 0
    pts = []
    for t in sorted({l["u"] for l in labels}):
        acc = [l for l in labels if l["u"] <= t]
        n = len(acc)
        err = sum(1 for l in acc if not l["correct"]) / n if n else 1.0
        pts.append({"threshold": t, "coverage": round(n / len(labels), 3),
                    "risk": round(err, 4), "ub": round(ub(err, n, a.delta), 4)})
    print(json.dumps({"coverage_risk_curve": pts}, indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main())
