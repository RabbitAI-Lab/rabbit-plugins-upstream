#!/usr/bin/env python3
"""theatre.py — detect VERIFICATION THEATRE in a verification result.

Trust contract rule 4: "a check that cannot fail is not verification". Every
other tool here performs a check; this one audits whether the check you just ran
was actually capable of failing. It reads the JSON output of a verify tool and
looks for the structural signatures of a no-op gate.

Signatures it knows (each one was either found in this skill or is the direct
inverse of a guarantee this skill makes):

  grounding_gate
    * thresholds at or below zero, so every sentence passes
    * zero sentences audited while the decision is "accept"
    * a "grounded" verdict carrying zero lexical AND zero trigram overlap
    * short sentences skipped, never audited, while the decision is "accept"
  selfcheck
    * measurable=false (fewer than 2 samples) — the score is undefined
  answer_certificate
    * a valid certificate whose claims are still "unverified"
  cove
    * every claim "supported" with zero verification questions answered
  judge_panel
    * fewer than 3 judges (the skill requires >=3 to aggregate)
    * all judges returned an identical verdict AND identical text (not independent)
  generic
    * a decision field with no measurement behind it (no counters at all)

OUTPUT: {"tool":..., "theatre_risk": "none|low|medium|high", "findings": [...],
         "verdict": "..."} — findings carry the exact field that proved it.
EXIT: 0 ran · 2 bad input. Use --fail-on high to make a pipeline stop.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from _common import clean_errors, fail  # noqa: E402

RANK = {"none": 0, "low": 1, "medium": 2, "high": 3}


def _f(tool, sev, why, field=None):
    d = {"severity": sev, "why": why}
    if field:
        d["field"] = field
    d["tool"] = tool
    return d


def check_grounding_gate(d):
    out = []
    th = d.get("thresholds") or {}
    lex, sem = th.get("lex"), th.get("sem")
    if lex is not None and sem is not None and (lex <= 0 or sem <= 0):
        out.append(_f("grounding_gate", "high",
                      f"thresholds lex={lex} sem={sem} cannot fail: every cited "
                      "sentence passes regardless of its evidence", "thresholds"))
    n = d.get("n_sentences")
    if n == 0 and d.get("decision") == "accept":
        out.append(_f("grounding_gate", "high",
                      "decision=accept with zero sentences audited — nothing was checked",
                      "n_sentences"))
    for v in d.get("claim_verdicts") or []:
        if v.get("verdict") == "grounded" and not v.get("lex_containment") \
                and not v.get("trigram_cos"):
            out.append(_f("grounding_gate", "high",
                          "verdict=grounded with zero lexical and zero trigram overlap",
                          "claim_verdicts"))
            break
    if d.get("n_skipped_short") and d.get("decision") == "accept":
        out.append(_f("grounding_gate", "medium",
                      f"{d['n_skipped_short']} short sentence(s) were never audited but "
                      "the decision is accept", "n_skipped_short"))
    return out


def check_selfcheck(d):
    if d.get("measurable") is False or (d.get("n_samples") or 0) < 2:
        return [_f("selfcheck", "high",
                   f"n_samples={d.get('n_samples')}: self-consistency is undefined below 2 "
                   "samples, so any hallucination score here is invented", "n_samples")]
    return []


def check_answer_certificate(d):
    out = []
    claims = d.get("claims") or []
    unv = [c for c in claims if str(c.get("verdict", "")).lower() == "unverified"]
    valid = d.get("valid")
    if valid and unv:
        out.append(_f("answer_certificate", "medium",
                      f"certificate valid=true while {len(unv)} claim(s) are still "
                      "unverified — a certificate certifies the checking, not the truth",
                      "valid"))
    if claims and all(str(c.get("verdict", "")).lower() == "supported" for c in claims) \
            and not any(c.get("evidence") for c in claims):
        out.append(_f("answer_certificate", "high",
                      "every claim 'supported' but no claim carries evidence", "claims"))
    return out


def check_cove(d):
    claims = d.get("claims") or d.get("per_claim") or []
    qs = d.get("questions_answered", d.get("n_answers"))
    if claims and qs == 0:
        return [_f("cove", "high",
                   "all claims resolved with zero verification questions answered — "
                   "factored checking never happened", "questions_answered")]
    return []


def check_judge_panel(d):
    out = []
    judges = d.get("judges") or d.get("votes") or []
    if judges and len(judges) < 3:
        out.append(_f("judge_panel", "medium",
                      f"{len(judges)} judge(s); the skill requires >=3 before aggregating",
                      "judges"))
    verdicts = [str(j.get("verdict", j)) if isinstance(j, dict) else str(j) for j in judges]
    texts = [str(j.get("text", "")) for j in judges if isinstance(j, dict)]
    if len(verdicts) > 1 and len(set(verdicts)) == 1 and texts and len(set(texts)) == 1:
        out.append(_f("judge_panel", "medium",
                      "all judges returned an identical verdict and identical text — they "
                      "are not independent, so the ensemble adds no information", "judges"))
    return out


CHECKERS = {
    "grounding_gate": check_grounding_gate,
    "selfcheck": check_selfcheck,
    "answer_certificate": check_answer_certificate,
    "cove": check_cove,
    "judge_panel": check_judge_panel,
}


def generic(d):
    """A decision with no measurement behind it."""
    out = []
    if "decision" in d or "verdict" in d:
        counters = [k for k in d if k.startswith("n_")]
        measured = [k for k in d if isinstance(d[k], (int, float)) and not isinstance(d[k], bool)]
        if not counters and not measured:
            out.append(_f("generic", "medium",
                          "a decision was emitted with no numeric measurement or counter "
                          "behind it", "decision"))
    return out


@clean_errors
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Audit a verification result for checks that cannot fail.")
    ap.add_argument("--result-file", help="JSON output of a verify tool")
    ap.add_argument("--json", help="the same, inline")
    ap.add_argument("--tool", choices=sorted(CHECKERS),
                    help="force the checker (default: infer from the payload)")
    ap.add_argument("--fail-on", choices=["low", "medium", "high"], default=None,
                    help="exit 2 when theatre_risk is at least this severe")
    a = ap.parse_args()

    if a.result_file:
        if not os.path.exists(a.result_file):
            return fail(f"no such file: {a.result_file}")
        raw = open(a.result_file, encoding="utf-8", errors="replace").read()
    elif a.json:
        raw = a.json
    else:
        return fail("provide --result-file or --json")
    try:
        d = json.loads(raw)
    except json.JSONDecodeError as e:
        return fail(f"result is not valid JSON: {e}",
                    hint="pass the stdout of a verify tool, e.g. "
                         "grounding_gate.py ... | theatre.py --json \"$(...)\"")
    if not isinstance(d, dict):
        return fail("result must be a JSON object")
    if "error" in d and len(d) <= 2:
        return fail("you passed a tool ERROR object, not a result",
                    hint=f"upstream said: {d.get('error')}")

    tool = a.tool
    if not tool:
        keys = set(d)
        if "claim_verdicts" in keys or "n_grounded" in keys:
            tool = "grounding_gate"
        elif "hallucination_score" in keys or "n_samples" in keys:
            tool = "selfcheck"
        elif "per_claim" in keys or "verification_questions" in keys:
            tool = "cove"
        elif "judges" in keys or "votes" in keys:
            tool = "judge_panel"
        elif "claims" in keys:
            tool = "answer_certificate"

    findings = list(generic(d))
    if tool:
        findings += CHECKERS[tool](d)

    risk = max((f["severity"] for f in findings), key=lambda s: RANK[s], default="none")
    verdict = {
        "none": "no theatre signature found — this check could fail, so it counted",
        "low": "minor gap; the check ran but part of the input escaped it",
        "medium": "part of this check was inert — do not treat its verdict as clean",
        "high": "this check could not have failed; its verdict is meaningless, re-run it "
                "with settings that can fail",
    }[risk]
    out = {"tool": tool or "unknown", "theatre_risk": risk,
           "n_findings": len(findings), "findings": findings, "verdict": verdict}
    print(json.dumps(out, indent=2))
    if a.fail_on and RANK[risk] >= RANK[a.fail_on]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
