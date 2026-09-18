#!/usr/bin/env python3
"""cove.py — Chain-of-Verification (Dhuliawala et al., ICLR 2024; arXiv:2309.11495).

plan      split a draft answer into claims + emit verification questions
          (take the questions to a FRESH context — factored discipline: the
          answerer must never see the draft, or it re-hallucinates with it)
crosscheck  claims + independently-produced answers -> keep/revise/drop
revise    original answer + verdicts -> revised answer with refuted claims removed

Evidence: hallucinated entities per response 2.95 -> 0.68 (Wikidata lists);
FActScore 55.9 -> 71.4 (longform bios); MultiSpanQA +23% F1.
Stdlib-only, read-only.
"""
import argparse, hashlib, json, re, sys

def tokens(s):
    return set(re.findall(r"[a-z0-9]+", s.lower())) - {
        "the", "a", "an", "of", "in", "on", "to", "and", "or", "is", "are",
        "was", "were", "for", "with", "by", "at", "from", "as", "that", "this"}

def split_facts(text):
    parts = re.split(r"(?<=[.!?;])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.split()) >= 4]

def q_for(claim):
    cid = hashlib.sha1(claim.encode()).hexdigest()[:8]
    return {
        "claim_id": cid,
        "claim": claim,
        "questions": [
            f"Q{cid}-1: Is this claim true: \"{claim}\" Answer exactly YES, NO, or UNSUPPORTED, then one line of justification.",
            f"Q{cid}-2: What primary source would confirm or refute: \"{claim}\"?",
        ],
        "how_to_answer": "Answer from your own knowledge ONLY. Do NOT restate or read any draft answer — this check must stay factored (independent) to work.",
    }

def classify_answer(answer):
    a = answer.lower()
    unv = bool(re.search(r"\b(unsupported|unknown|no evidence|not supported|cannot verify|unsure|uncertain|might|may|maybe|possibly)\b", a))
    yes = bool(re.search(r"\b(yes|true|correct|confirmed|supported)\b", a))
    no = bool(re.search(r"\b(no|false|incorrect|refuted|not true)\b", a))
    if no and not yes and not unv:
        return "refuted"
    if yes and not no and not unv:
        return "supported"
    return "unverified"

# v2.1.2: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("plan")
    p1.add_argument("--answer-file"); p1.add_argument("--text")
    p1.add_argument("--max-claims", type=int, default=12)
    p2 = sub.add_parser("crosscheck")
    p2.add_argument("--answers-file", required=True,
                    help='JSON {"claim_id": "independent answer text", ...} (produced WITHOUT the draft in context)')
    p2.add_argument("--claims-file", required=True, help="JSON array from plan (save its claims array)")
    p3 = sub.add_parser("revise")
    p3.add_argument("--answer-file"); p3.add_argument("--text")
    p3.add_argument("--verdicts-file", required=True, help="crosscheck JSON output")
    a = ap.parse_args()
    if a.cmd == "plan":
        text = open(a.answer_file, encoding="utf-8", errors="replace").read() if a.answer_file else a.text
        if not text:
            print(json.dumps({"error": "provide --text or --answer-file"})); return 2
        claims = (split_facts(text) or [text.strip()])[:a.max_claims]
        items = [q_for(c) for c in claims]
        print(json.dumps({
            "n_claims": len(items),
            "claims": [c for c in claims],
            "verification_items": items,
            "protocol": ("answer every question in a FRESH context that contains ONLY the questions "
                         "(never the draft) — joint verification re-imports the draft's hallucinations"),
        }, indent=2)); return 0
    if a.cmd == "crosscheck":
        answers = json.load(open(a.answers_file, encoding="utf-8"))
        claims = json.load(open(a.claims_file, encoding="utf-8"))
        claims = claims["claims"] if isinstance(claims, dict) else claims
        rows = []
        for c in claims:
            cid = hashlib.sha1(c.encode()).hexdigest()[:8]
            ans = answers.get(cid) or answers.get(c) or ""
            if not ans:
                rows.append({"claim_id": cid, "claim": c[:140], "verdict": "unverified",
                             "reason": "no independent answer provided"})
                continue
            A, C = tokens(ans), tokens(c)
            overlap = len(A & C) / max(1, len(C))
            v = classify_answer(ans)
            if v == "supported" and overlap < 0.15:
                v = "unverified"; reason = "affirmation with near-zero substantive overlap"
            else:
                reason = ""
            rows.append({"claim_id": cid, "claim": c[:140], "verdict": v,
                         "answer_excerpt": ans[:160], "claim_token_overlap": round(overlap, 2),
                         **({"reason": reason} if reason else {})})
        n_ref = sum(1 for r in rows if r["verdict"] == "refuted")
        n_unv = sum(1 for r in rows if r["verdict"] == "unverified")
        print(json.dumps({
            "claims": rows, "n_claims": len(rows), "n_refuted": n_ref, "n_unverified": n_unv,
            "decision": ("revise" if n_ref or n_unv else "keep"),
            "next": "run `revise` with these verdicts, then grounding_gate on the result",
        }, indent=2)); return 0
    text = open(a.answer_file, encoding="utf-8", errors="replace").read() if a.answer_file else a.text
    verd = json.load(open(a.verdicts_file, encoding="utf-8"))
    if not text:
        print(json.dumps({"error": "provide --text or --answer-file"})); return 2
    bad = {r["claim"] for r in verd.get("claims", []) if r["verdict"] == "refuted"}
    unv = {r["claim"] for r in verd.get("claims", []) if r["verdict"] == "unverified"}
    kept, flags = [], []
    for s in split_facts(text):
        hit_bad = next((b for b in bad if b[:60] in s or s[:60] in b), None)
        hit_unv = next((b for b in unv if b[:60] in s or s[:60] in b), None)
        if hit_bad:
            flags.append({"action": "dropped", "sentence": s[:140]})
        elif hit_unv:
            kept.append(s + " [unverified]")
            flags.append({"action": "flagged", "sentence": s[:140]})
        else:
            kept.append(s)
    print(json.dumps({
        "revised_answer": " ".join(kept),
        "dropped": sum(1 for f in flags if f["action"] == "dropped"),
        "flagged": sum(1 for f in flags if f["action"] == "flagged"),
        "changes": flags,
        "note": "refuted claims removed, unverified claims labeled; re-run grounding_gate before delivery",
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
