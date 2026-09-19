#!/usr/bin/env python3
"""selfcheck.py — sampling-based hallucination scoring (F8, F9).

SelfCheckGPT/FactSelfCheck-style: score a claim's facts against N sampled
responses from the same model (samples must be produced by the agent's model).
Also computes a semantic-entropy-lite cluster entropy (Farquhar et al., Nature
2024 flavor) over the samples. Stdlib-only, read-only.

v3.0.0 — two correctness fixes for wrong answers (not crashes):

1. SENTENCE-LEVEL MATCHING. Self-consistency compares a fact against the
   sentence(s) that restate it, not against the entire sampled response. The old
   `jac(fact, whole_sample)` divides by the union with a whole response, so a
   correct fact quoted verbatim inside a longer answer scored LOW overlap and was
   reported as a possible hallucination. Measured before the fix: a fact stated
   verbatim and correctly in all 3 samples scored hallucination_risk 0.667 /
   label "possible". A detector that cries wolf on true statements is worse than
   no detector, because agents learn to ignore it.

2. n<2 SAMPLES IS UNMEASURABLE, NOT MAXIMALLY RISKY. With a single sample there
   is no second opinion to disagree with, so the overlap score carries no
   information. The old code returned hallucination_risk 1.0 / label "likely"
   for every fact — and portability.py assigns samples=1 to the local tier, so
   on local models this tool flagged EVERY fact as a likely hallucination.
   Such runs are now reported as measurable=false with label
   "insufficient-samples"; the numeric fields stay null, never a fake 1.0.
"""
import argparse, json, math, re, sys

STOP = {"the", "a", "an", "of", "in", "on", "to", "and", "or", "is", "are",
        "was", "were", "for", "with", "by", "at", "from", "as", "that", "this"}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors, fail


def tokens(s):
    return set(re.findall(r"[a-z0-9]+", s.lower())) - STOP


def jac(a, b):
    A, B = tokens(a), tokens(b)
    return len(A & B) / len(A | B) if A | B else 0.0


def split_sentences(text):
    """Sentence-ish split; falls back to the whole text so nothing is lost."""
    parts = [p.strip() for p in re.split(r"(?<=[.!?;])\s+|\n+", text) if p.strip()]
    return parts or [text]


def best_overlap(fact, sample):
    """Max Jaccard of the fact against any sentence of the sample.

    Taking the max over sentences is what makes the score length-invariant: a
    200-word response that restates the fact in one clause no longer dilutes the
    denominator. The whole-sample score is kept as a floor so a fact spread
    across clauses still scores.
    """
    scores = [jac(fact, s) for s in split_sentences(sample)]
    return max(scores + [jac(fact, sample)])


def split_facts(claim):
    parts = re.split(r"(?<=[.!?;])\s+|\s+(?:and|but|while|whereas)\s+", claim)
    return [p.strip() for p in parts if len(p.split()) >= 4]


def cluster_entropy(samples, thr=0.45):
    clusters = []
    for s in samples:
        for c in clusters:
            if jac(s, c[0]) >= thr:
                c.append(s); break
        else:
            clusters.append([s])
    n = len(samples)
    sizes = [len(c) for c in clusters]
    H = -sum((k / n) * math.log(k / n) for k in sizes) if n else 0.0
    return H, len(clusters), sizes


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claim"); ap.add_argument("--claim-file")
    ap.add_argument("--samples-file", help="JSON array of sampled responses")
    ap.add_argument("--samples", help="responses joined by ||")
    a = ap.parse_args()
    claim = open(a.claim_file, encoding="utf-8", errors="replace").read() if a.claim_file else a.claim
    if not claim:
        return fail("provide --claim or --claim-file")
    if a.samples_file:
        samples = json.load(open(a.samples_file, encoding="utf-8"))
    elif a.samples:
        samples = a.samples.split("||")
    else:
        return fail("provide --samples or --samples-file")
    if not isinstance(samples, list):
        return fail("--samples-file must be a JSON array of strings",
                    hint='e.g. ["answer one ...", "answer two ..."]')
    samples = [s for s in samples if isinstance(s, str) and s.strip()]
    if not samples:
        return fail("empty samples")

    facts = split_facts(claim) or [claim]
    n = len(samples)
    measurable = n >= 2

    per_fact = []
    for f in facts:
        if not measurable:
            per_fact.append({"fact": f[:120], "max_sample_overlap": None,
                             "hallucination_risk": None, "label": "insufficient-samples"})
            continue
        m = max(best_overlap(f, s) for s in samples)
        per_fact.append({"fact": f[:120], "max_sample_overlap": round(m, 3),
                         "hallucination_risk": round(1 - m, 3),
                         "label": ("likely" if m < 0.15 else
                                   "possible" if m < 0.35 else "unlikely")})

    H, k, sizes = cluster_entropy(samples)
    out = {
        "n_samples": n, "n_facts": len(per_fact),
        "measurable": measurable,
        "per_fact": per_fact,
        "semantic_entropy_lite": {"cluster_entropy": round(H, 3),
                                  "n_clusters": k, "cluster_sizes": sizes,
                                  "note": "high entropy across samples -> model uncertain; verify with L3 tools"},
    }
    if not measurable:
        out["hallucination_score"] = None
        out["high_risk_facts"] = None
        out["verdict"] = "insufficient-samples"
        out["warning"] = (f"self-consistency needs >=2 sampled responses; got {n}. "
                          "No score is reported because none is measurable — "
                          "sample more responses or escalate to L3 tool-grounded verification.")
    else:
        hi = [p for p in per_fact if p["label"] != "unlikely"]
        out["hallucination_score"] = round(
            sum(p["hallucination_risk"] for p in per_fact) / len(per_fact), 3)
        out["high_risk_facts"] = len(hi)
        out["verdict"] = "verify-with-tools" if hi or H > 0.9 else "consistent"
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
