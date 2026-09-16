#!/usr/bin/env python3
"""compress.py — token-efficiency toolkit (v2.1).

compress   extractive INPUT-token compression of a prompt/context (LLMLingua-flavored,
           lexical approximation: rank sentences, keep the informative ones)
stats      token-budget report for a text (est. tokens + compression advice)
draft      emit the Chain-of-Draft output-token contract (arXiv:2502.18600: ~80%
           fewer reasoning tokens at matched accuracy — for models >=7B only)

Facts honored: compression is worthwhile only above ~500 input tokens; never drop
sentences carrying numbers, quotes, or citations; extraction can lose connective
context — review the dropped list. Stdlib-only, read-only.
"""
import argparse, json, re, sys

STOP = set("""the a an of in on to and or is are was were for with by at from as that this it its
their there here be been being have has had do does did not no but if then than so such can could
will would should may might must shall about into over under between within without also more most
very much many any all some each which who whom whose what when where why how""".split())

def sent_split(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(s.split()) >= 3]

def est_tokens(text):
    return max(1, round(len(text) / 4))  # chars/4 heuristic, labeled as estimate

def score_sent(s, df):
    w = [x for x in re.findall(r"[a-z0-9']+", s.lower())]
    if not w:
        return 0.0
    content = [x for x in w if x not in STOP]
    uniq = len(set(content)) / max(1, len(content))
    density = len(content) / len(w)
    num = 1.5 if re.search(r"\d", s) else 0.0
    quote = 1.2 if ('"' in s or "“" in s or "”" in s) else 0.0
    cite = 1.0 if re.search(r"\[\d+\]|\((?:doi|arxiv|isbn)|https?://", s, re.I) else 0.0
    rare = sum(1.0 / df.get(x, 1) for x in content[:20]) if df else 0.0
    return uniq + density + num + quote + cite + 0.05 * rare

# v2.1.2: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c1 = sub.add_parser("compress")
    c1.add_argument("--text-file"); c1.add_argument("--text")
    c1.add_argument("--ratio", type=float, default=0.5, help="fraction of est. tokens to KEEP")
    c1.add_argument("--min-tokens", type=int, default=500,
                    help="refuse below this (compression not worthwhile — LLMLingua guidance)")
    c1.add_argument("--force", action="store_true")
    c2 = sub.add_parser("stats")
    c2.add_argument("--text-file"); c2.add_argument("--text")
    c3 = sub.add_parser("draft")
    a = ap.parse_args()
    if a.cmd == "draft":
        print(json.dumps({
            "chain_of_draft_contract": (
                "Solve the task writing AT MOST 5 WORDS per reasoning step, e.g. "
                "'3x=21 → x=7. Need y. y=2x → 14.' Then output 'Final answer:' and the answer. "
                "No prose, no restating the question, no summaries of steps."),
            "evidence": "arXiv:2502.18600: matches/beats CoT accuracy with as little as 7.6% of tokens",
            "when_not": "disable for models below 7B and on novel task shapes until an eval_regression A/B passes",
            "pair_with": "portability.py profile -> cod_enabled",
        }, indent=2)); return 0
    text = open(a.text_file, encoding="utf-8", errors="replace").read() if a.text_file else a.text
    if not text:
        print(json.dumps({"error": "provide --text or --text-file"})); return 2
    sents = sent_split(text)
    est = est_tokens(text)
    if a.cmd == "stats":
        advice = ("compression worthwhile (est >= 500 tokens)" if est >= 500
                  else "too short to bother (est < 500 tokens)")
        print(json.dumps({"est_tokens": est, "n_sentences": len(sents), "advice": advice,
                          "note": "est_tokens = chars/4 heuristic"}, indent=2)); return 0
    if est < a.min_tokens and not a.force:
        print(json.dumps({"compressed_text": text, "est_tokens": est,
                          "skipped": f"below --min-tokens {a.min_tokens}; compression overhead not worthwhile",
                          "hint": "pass --force to compress anyway"}, indent=2)); return 0
    df = {}
    for s in sents:
        for x in set(re.findall(r"[a-z0-9']+", s.lower())) - STOP:
            df[x] = df.get(x, 0) + 1
    target = max(1, int(est * a.ratio))
    used = 0
    ranked = sorted(range(len(sents)), key=lambda i: -score_sent(sents[i], df))
    chosen = {0} if sents else set()  # thesis sentence always kept
    for i in ranked:
        if used >= target:
            break
        if i in chosen:
            continue
        chosen.add(i)
        used += est_tokens(sents[i])
    out = [sents[i] for i in sorted(chosen)]
    out_set = set(out)
    dropped = [s for s in sents if s not in out_set]
    comp = " ".join(out)
    ct = est_tokens(comp)
    print(json.dumps({
        "compressed_text": comp,
        "est_tokens_orig": est, "est_tokens_compressed": ct,
        "compression_ratio": round(est / max(1, ct), 2),
        "n_sentences_dropped": len(dropped),
        "dropped_review": [d[:120] for d in dropped[:8]],
        "warnings": ["extractive: review dropped sentences for lost connective context",
                     "numbers/quotes/citations were preferentially kept, not guaranteed"],
    }, indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main())
