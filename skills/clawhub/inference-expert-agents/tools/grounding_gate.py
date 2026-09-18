#!/usr/bin/env python3
"""grounding_gate.py — sentence-level citation validation (F10, F11, F7).

CiteGuard-RAG-style runtime gate: every cited sentence is checked against its
cited evidence (lexical containment >= --lex or char-trigram cosine >= --sem,
defaults 0.10/0.40). Uncited factual-looking sentences are flagged. Emits
machine-readable per-sentence verdicts and an accept/regenerate/refuse decision.
Stdlib-only, read-only.
"""
import argparse, json, re, sys

CITE = re.compile(r"\[(\d+)\]|\(ref\.?\s*(\d+)\)|\[evidence:? ?(\d+)\]", re.I)

MIN_SENTENCE_WORDS = 4


def sentences(text):
    """Sentences long enough to audit. Callers must also read `skipped()` — a
    short claim that never reaches the gate must not silently vanish from the
    totals, or the answer looks cleaner than it was checked."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text)
            if len(s.split()) >= MIN_SENTENCE_WORDS]


def skipped(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text)
            if 0 < len(s.split()) < MIN_SENTENCE_WORDS]


# v3.0.0 — a real factual/filler classifier. The old pattern was
#   bool(re.search(r"\d|['\"]|[^.!? ]{3,}", s))
# whose third alternative matches ANY run of 3+ non-space characters, i.e. any
# ordinary word, so the disjunction was true for essentially every sentence and
# the "opinion_or_fill" branch was unreachable. A classifier that can only ever
# return one class is not a classifier.
FACTUAL_RE = re.compile(
    r"\d"                                            # numbers, dates, quantities
    r"|['\"\u201c\u201d\u2018\u2019]"                # quotations
    r"|\b(?:is|are|was|were|has|have|had|states?|reports?|shows?|found|"
    r"causes?|leads? to|consists? of|equals?|measures?|contains?)\b"
    r"|(?:\b[A-Z][a-z]{2,}\b.*){2}"                  # >=2 proper-noun-shaped tokens
)
OPINION_RE = re.compile(
    r"^\s*(?:i|we|you|one)\s+(?:think|believe|feel|suspect|guess|imagine|wonder)\b"
    r"|\b(?:in my (?:view|opinion)|it seems|arguably|one might say|"
    r"feel free|hope this helps|let me know)\b", re.I)


def is_factual(s):
    return bool(FACTUAL_RE.search(s)) and not OPINION_RE.search(s) and len(s.split()) >= 6

def toks(s):
    return set(re.findall(r"[a-z0-9]+", s.lower())) - {
        "the", "a", "an", "of", "in", "on", "to", "and", "or", "is", "are",
        "was", "were", "for", "with", "by", "at", "from", "as", "that", "this"}

def trigrams(s):
    s = re.sub(r"\s+", " ", s.lower())
    return {s[i:i + 3] for i in range(max(0, len(s) - 2))}

def tri_cos(a, b):
    A, B = trigrams(a), trigrams(b)
    return len(A & B) / (len(A) * len(B)) ** 0.5 if A and B else 0.0

def rouge_l(hyp, ref):
    """ROUGE-L recall: LCS over whitespace tokens (capped at 200 for speed)."""
    H, R = hyp.lower().split()[:200], ref.lower().split()[:200]
    if not H or not R:
        return 0.0
    prev = [0] * (len(R) + 1)
    for h in H:
        cur = [0]
        for j, r in enumerate(R, 1):
            cur.append(prev[j - 1] + 1 if h == r else max(prev[j], cur[-1]))
        prev = cur
    return prev[-1] / len(R)

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors, fail


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--answer-file"); ap.add_argument("--text")
    ap.add_argument("--evidence-file", required=True,
                    help='JSON: {"1": "evidence text", "2": "..."} (evidence you retrieved)')
    ap.add_argument("--lex", type=float, default=0.10)
    ap.add_argument("--sem", type=float, default=0.40)
    a = ap.parse_args()
    # v3.0.0 — a gate that cannot fail is not a gate. The old code accepted any
    # float, so `--lex 0 --sem 0` (or a negative) made EVERY cited sentence
    # "grounded" no matter how unrelated the evidence was. Verified before the
    # fix: "Aspirin cures cancer in mice [1]" against evidence about rainfall in
    # Chile returned verdict=grounded, decision=accept. That is verification
    # theatre, and it is the exact failure mode this skill exists to refuse.
    for name, val in (("--lex", a.lex), ("--sem", a.sem)):
        if not (0.0 < val <= 1.0):
            return fail(f"{name} must be in (0, 1], got {val}",
                        hint="defaults are --lex 0.10 --sem 0.40; a threshold of 0 "
                             "makes the gate unable to fail, which is not verification")
    text = open(a.answer_file, encoding="utf-8", errors="replace").read() if a.answer_file else a.text
    ev = json.load(open(a.evidence_file, encoding="utf-8"))
    ev = {str(k): v for k, v in ev.items()}
    if not text:
        print(json.dumps({"error": "provide --text or --answer-file"})); return 2
    verdicts = []
    for s in sentences(text):
        m = CITE.search(s)
        if m:
            refs = []
            for mm in CITE.finditer(s):
                r = next(g for g in mm.groups() if g)
                if r not in refs:
                    refs.append(r)
            best = None
            for ref in refs:
                evidence = ev.get(ref, "")
                if not evidence:
                    continue
                S, E = toks(s), toks(evidence)
                lex = len(S & E) / len(S) if S else 0.0
                tri = tri_cos(s, evidence)
                rl = rouge_l(s, evidence)
                cand = {"lex": lex, "tri": tri, "rl": rl, "ok": lex >= a.lex or tri >= a.sem}
                if best is None or (cand["ok"] and not best["ok"]) or \
                   (cand["ok"] == best["ok"] and (cand["tri"], cand["rl"]) > (best["tri"], best["rl"])):
                    best = dict(cand, ref=ref)
            if best is None:
                verdicts.append({"sentence": s[:140], "verdict": "unsupported",
                                 "reason": f"citations {refs} not in evidence set" if refs else "no citation parsed"})
                continue
            verdicts.append({"sentence": s[:140], "verdict": "grounded" if best["ok"] else "unsupported",
                             "citation": best["ref"], "n_citations": len(refs),
                             "lex_containment": round(best["lex"], 3),
                             "trigram_cos": round(best["tri"], 3),
                             "rouge_l_recall": round(best["rl"], 3),
                             "thresholds": {"lex": a.lex, "sem": a.sem}})
        else:
            verdicts.append({"sentence": s[:140],
                             "verdict": "uncited" if is_factual(s) else "opinion_or_fill",
                             "reason": "factual-looking sentence without citation"})
    short = skipped(text)
    bad = [v for v in verdicts if v["verdict"] == "unsupported"]
    uncited = [v for v in verdicts if v["verdict"] == "uncited"]
    decision = ("refuse" if bad else "regenerate" if uncited else "accept")
    print(json.dumps({
        "n_sentences": len(verdicts),
        "n_audited": len(verdicts) + len(short), "n_grounded": sum(1 for v in verdicts if v["verdict"] == "grounded"),
        "n_unsupported": len(bad), "n_uncited_factual": len(uncited),
        "n_skipped_short": len(short),
        "skipped_short": [x[:140] for x in short],
        "claim_verdicts": verdicts,
        "decision": decision,
        "action": {"accept": "deliver as-is",
                   "regenerate": "add citations to uncited factual sentences or remove them, then re-gate",
                   "refuse": "cited sentence(s) not supported by their evidence — rewrite or drop; never deliver"}[decision],
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
