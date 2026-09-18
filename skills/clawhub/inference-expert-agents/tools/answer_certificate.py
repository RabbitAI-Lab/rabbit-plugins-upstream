#!/usr/bin/env python3
"""answer_certificate.py — machine-checkable answer certificates (F46).

A certificate binds an answer to its verification evidence: every load-bearing
claim, its check method, verdict, and provenance. assemble builds the skeleton;
validate checks completeness and internal consistency before delivery.
Stdlib-only, read-only.
"""
import argparse, json, sys

REQ = ["answer", "claims"]
CLAIM_REQ = ["claim", "method", "verdict", "evidence"]
METHODS = ("self-consistency", "tool-execution", "retrieval-citation",
           "judge-consensus", "calculator", "authority-source")

def validate(cert):
    errs = []
    for k in REQ:
        if k not in cert:
            errs.append(f"missing top-level field '{k}'")
    for i, c in enumerate(cert.get("claims", [])):
        for k in CLAIM_REQ:
            if k not in c:
                errs.append(f"claims[{i}]: missing '{k}'")
        if c.get("method") not in METHODS:
            errs.append(f"claims[{i}]: method must be one of {METHODS}")
        if c.get("verdict") not in ("supported", "refuted", "unverified"):
            errs.append(f"claims[{i}]: verdict must be supported|refuted|unverified")
        if c.get("verdict") == "refuted":
            errs.append(f"claims[{i}]: refuted claim present — answer must be revised or abstained")
    unv = [i for i, c in enumerate(cert.get("claims", [])) if c.get("verdict") == "unverified"]
    ok = not errs
    return {"ok": ok, "errors": errs,
            "unverified_claims": unv,
            "verdict": ("certified" if ok and not unv else
                        "conditionally-certified" if ok else "invalid")}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("assemble")
    s1.add_argument("--answer", required=True)
    s1.add_argument("--claims", required=True,
                    help='JSON [{"claim":"...","method":"retrieval-citation","verdict":"supported","evidence":"[1] p3"},...]')
    s2 = sub.add_parser("validate")
    s2.add_argument("--cert", required=True, help="certificate JSON (file path or inline)")
    a = ap.parse_args()
    if a.cmd == "assemble":
        claims = json.loads(a.claims)
        cert = {"answer": a.answer, "claims": claims,
                "policy": "every load-bearing claim needs a check method and evidence"}
        v = validate(cert)
        print(json.dumps({"certificate": cert, "validation": v}, indent=2))
        return 0
    raw = a.cert
    try:
        cert = json.load(open(raw, encoding="utf-8"))
    except Exception:
        cert = json.loads(raw)
    print(json.dumps(validate(cert), indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
