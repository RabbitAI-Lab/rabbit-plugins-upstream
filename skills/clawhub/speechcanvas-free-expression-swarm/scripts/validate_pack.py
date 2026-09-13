#!/usr/bin/env python3
"""validate_pack.py — structural check of a prompt pack against the skill contract
(schema/prompt_pack.schema.json), implemented with the stdlib so it runs anywhere.

exit 0 = valid · exit 1 = invalid (JSON report on stdout)
Usage: python3 scripts/validate_pack.py pack.json [--final]
--final additionally requires guardian_status == PASS (a deliverable pack).
"""
import argparse
import json
import sys

REQUIRED = ["subject", "motif", "lighting", "lens", "setting", "gesture",
            "constraints", "safety_tags", "iteration", "guardian_status",
            "critic_notes", "deception_theme"]
TEXT_FIELDS = ["subject", "motif", "lighting", "lens", "setting", "gesture"]
SAFETY_TAGS = {"lawful", "consent-aware", "non-deceptive", "free-expression", "symbolic-atmosphere"}
REQUIRED_TAGS = {"lawful", "consent-aware", "non-deceptive", "free-expression"}
REQUIRED_CONSTRAINTS = [
    "no real names or likenesses",
    "no official seals",
    "no readable instructions or documents",
    "no real public figures",
    "no private persons as targets",
    "no fake evidence or fabricated events",
]


def check(pack, final=False):
    errs = []
    if not isinstance(pack, dict):
        return ["pack is not a JSON object"]
    for k in REQUIRED:
        if k not in pack:
            errs.append(f"missing required field: {k}")
    for k in TEXT_FIELDS:
        v = pack.get(k)
        if isinstance(v, str) and len(v) > 200:
            errs.append(f"{k} exceeds 200 chars ({len(v)})")
        elif v is not None and not isinstance(v, str):
            errs.append(f"{k} must be a string")
    c = pack.get("constraints")
    if not isinstance(c, list) or not c:
        errs.append("constraints must be a non-empty array")
    else:
        lc = [str(x).lower().strip().rstrip(".") for x in c]
        for req in REQUIRED_CONSTRAINTS:
            if req not in lc:
                errs.append(f"constraints missing safety fence: '{req}'")
    t = pack.get("safety_tags")
    if not isinstance(t, list) or not t:
        errs.append("safety_tags must be a non-empty array")
    else:
        unknown = [x for x in t if x not in SAFETY_TAGS]
        if unknown:
            errs.append(f"safety_tags unknown values: {unknown}")
        missing = REQUIRED_TAGS - set(t)
        if missing:
            errs.append(f"safety_tags missing required: {sorted(missing)}")
    it = pack.get("iteration")
    if it is not None and (not isinstance(it, int) or isinstance(it, bool) or not 1 <= it <= 3):
        errs.append("iteration must be an integer 1-3")
    g = pack.get("guardian_status")
    if g is not None and g not in ("PASS", "FAIL"):
        errs.append("guardian_status must be PASS or FAIL")
    if final and g != "PASS":
        errs.append("final/deliverable pack must have guardian_status == PASS")
    cn = pack.get("critic_notes")
    if isinstance(cn, str) and len(cn) > 500:
        errs.append(f"critic_notes exceeds 500 chars ({len(cn)})")
    d = pack.get("deception_theme")
    if d is not None and not isinstance(d, bool):
        errs.append("deception_theme must be a boolean")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--final", action="store_true")
    args = ap.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            pack = json.load(fh)
    except Exception as e:
        print(json.dumps({"valid": False, "errors": [f"cannot read/parse: {e}"]}, indent=1))
        sys.exit(1)
    errs = check(pack, final=args.final)
    print(json.dumps({"valid": not errs, "errors": errs,
                      "schema": "schema/prompt_pack.schema.json"}, indent=1))
    sys.exit(0 if not errs else 1)


if __name__ == "__main__":
    main()
