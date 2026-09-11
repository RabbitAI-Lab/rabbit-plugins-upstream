#!/usr/bin/env python3
"""benchscan.py — Benchmark Robustness Auditor engine (v2.0.0). Offline, stdlib-only.

Defense-side robustness audits for LLM benchmarks: contamination, option/position
bias, judge bias, few-shot artifacts, prompt-rephrase sensitivity — plus WORKED
mitigations (permutation ensemble, blind normalization) and an explicit,
documented severity formula. Every finding cites a static CATALOGUE id; the
engine hard-fails on unknown ids (hallucinated exploit categories are
impossible by construction). Not a tool for inflating scores.

Subcommands
  doctor                                   env + catalogue + contracts (JSON)
  contam  --benchmark B.jsonl --corpus C.jsonl [--n 13] [--cutoff DATE] [--results R.jsonl]
  selection --runs R.jsonl                 option-letter instability + token bias
  fewshot --curve F.jsonl                  shot-count sensitivity curve
  judge   --judgments J.jsonl [--rubric-terms t.json] position/verbosity/echo/injection
  compare --a preds_a.jsonl --b preds_b.jsonl   McNemar + Wilson + paired bootstrap
  ensemble --runs E.jsonl                  WORKED mitigation: permutation majority vote
  blind-normalize --input responses.jsonl -o out.jsonl   WORKED mitigation: strip/normalize
  severity --inflation PP --affected FRACTION --evidence P [--json]
  report --name NAME [--benchmark .. --corpus .. --runs .. --judgments .. --curve ..
         --a-preds .. --b-preds .. --cutoff .. --results .. --tsguess ..] [-o out.md]
  trend  --name NAME                       metric delta vs previous audited run
  audit  [--verify]                        history ledger chain check (always verifies)

Input contracts (JSONL, one object per line):
  benchmark/corpus : {"id": "...", "text": "...", "date": "YYYY-MM-DD"?}
  runs (selection) : {"item": "...", "gold": "A", "letters": ["B","A",...]}
  ensemble         : {"item": "...", "gold": "A", "perms": [["A","B","C","D"],...],
                      "letters": ["C","C","D"]}  (letters[i] was output under perms[i])
  curve            : {"shots": int, "acc": float}
  judgments        : {"pair": "...", "order": "ab"|"ba", "verdict": "a"|"b"|"tie",
                      "len_a": int?, "len_b": int?, "text_a": str?, "text_b": str?}
                      (verdict refers to the PRESENTED order; both orders per pair
                      enables flip analysis, single order enables aggregate bias only)
  preds            : {"id": "...", "ok": 0|1}

Exit codes: 0 ok · 2 usage/ruleset-trip · 3 input/env error · 4 policy FAIL
(report verdict COMPROMISED; severity at CRITICAL) · 1 trend REGRESSED.
"""
import argparse, hashlib, json, math, os, re, sys, time

RULESET_VERSION = "2.0.0"
CHAR_N_DEFAULT = 13          # GPT-3 word-13-gram tradition (here: word n-grams)
OVERLAP_CONTAM = 0.8         # item-level contamination threshold (documented)
OVERLAP_SUSPECT = 0.3
SHINGLE_W = 5                # MinHash-style word shingles (secondary metric)
JACCARD_FLAG = 0.5
PARA_F1_FLAG = 0.8           # token-set F1 paraphrase flag (embedding-analog band)
POSITION_FLIP_FLAG = 0.10    # pairwise order-flip rate flag (evidence: 10-15pt swing)
VERBO_SHARE_FLAG = 0.60      # longer-response-wins share flag (> binomial noise)
FEWSHOT_RANGE_FLAG = 0.08    # 8pp acc range flag (heuristic; see evidence.md)
DATE_GAP_FLAG = 0.10         # 10pp pre/post-cutoff accuracy gap (LiveCodeBench)
SEV_FORMULA = ("round(100*(0.40*min(1,|infl|/15)+0.35*min(1,|aff|/0.10)+"
               "0.25*clamp(ev,0,1))); tiers CRITICAL>=75 HIGH>=50 MEDIUM>=25 else LOW")
# E-3 detection patterns: precision-over-recall on purpose (reviewer-audited) —
# an innocent "score 100%" or "as the judge said" mid-sentence must NOT trip.
HIDDEN_PATTERNS = [
    ("html-comment injection", re.compile(r"<!--[\s\S]{0,2000}?-->")),
    ("instruction override", re.compile(
        r"(?i)\b(ignore|disregard|forget|drop)\b\s+(?:all\s+|any\s+|the\s+){0,2}"
        r"(?:previous|prior|above|earlier)")),
    ("score override", re.compile(
        r"(?i)\b(final|override|set|assign|give|make)\b[^.]{0,24}"
        r"\b(score|grade|mark|rating)\b\s*[:=]?\s*(?:10|100|a\+|perfect|excellent)\b")),
    ("zero-width chars", re.compile(r"[​-‏ - ⁠-⁯﻿­]")),
    ("authority laundering", re.compile(
        r"(?im)^\s*as\s+the\s+(?:lead\s+|head\s+)?(?:grader|judge|evaluator|professor)\b")),
]
MODEL_RE = re.compile(
    r"(?i)\b(gpt-?[\w.]*|claude[\w.-]*|gemini[\w.-]*|llama-?\d[\w.-]*|qwen\d[\w.-]*|"
    r"qwen-[\w.-]+|deepseek[\w.-]*|mistral[\w.-]*|mixtral[\w.-]*|grok-?\d[\w.-]*|"
    r"gemma[\w.-]*|phi-[34]\b|command-r\+?|yi-\d[\w.-]*|codellama[\w.-]*)\b")
CTRL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")

CATALOGUE = {
    "C-1": {"title": "exact-string contamination (n-gram overlap)", "default_sev": 4,
            "computable": True, "mitigation": "decontam-by-ngram"},
    "C-2": {"title": "near-duplicate paraphrase (token-set F1 + shingles)", "default_sev": 3,
            "computable": True, "mitigation": "decontam-by-embedding-or-shingle"},
    "C-3": {"title": "temporal contamination (post-cutoff accuracy gap)", "default_sev": 3,
            "computable": True, "mitigation": "temporal-gating"},
    "G-1": {"title": "masked-choice guessing above chance (TS-Guessing)", "default_sev": 3,
            "computable": True, "mitigation": "rebuild-benchmark"},
    "P-1": {"title": "prompt-rephrase sensitivity (paired McNemar)", "default_sev": 3,
            "computable": True, "mitigation": "multi-surface-scoring"},
    "P-2": {"title": "few-shot priming/order sensitivity", "default_sev": 2,
            "computable": True, "mitigation": "stratified-few-shot"},
    "P-3": {"title": "option-letter / token selection bias", "default_sev": 2,
            "computable": True, "mitigation": "permutation-ensemble"},
    "T-1": {"title": "CoT-washing (style-hacked reasoning)", "default_sev": 2,
            "computable": False, "needs": "paraphrase-rescored answers (P-1 channel)"},
    "T-2": {"title": "refusal suppression", "default_sev": 2, "computable": False,
            "needs": "refusal-rate logs"},
    "T-3": {"title": "rubric keyword echo (judge gaming)", "default_sev": 3,
            "computable": True, "mitigation": "content-rubrics"},
    "T-4": {"title": "CoT leakage (answer-first reasoning)", "default_sev": 2,
            "computable": False, "needs": "reasoning-trace extraction (heuristic only)"},
    "T-5": {"title": "tool-use gaming (verbatim question search)", "default_sev": 3,
            "computable": False, "needs": "tool-call logs from the eval harness"},
    "E-1": {"title": "judge position bias (order flip)", "default_sev": 4,
            "computable": True, "mitigation": "double-swap-averaging"},
    "E-2": {"title": "judge verbosity bias", "default_sev": 2,
            "computable": True, "mitigation": "length-controlled-scoring"},
    "E-3": {"title": "hidden instruction injection into judged content", "default_sev": 4,
            "computable": True, "mitigation": "content-sanitization"},
    "D-1": {"title": "benchmark-specific fine-tuning", "default_sev": 3, "computable": False,
            "needs": "training-data provenance (not offline)"},
    "M-1": {"title": "temperature/sampling variance", "default_sev": 1,
            "computable": True, "mitigation": "multi-seed-mean-and-CI"},
}
SEV_NAME = {1: "LOW", 2: "MEDIUM", 3: "HIGH", 4: "CRITICAL"}
MITIGATIONS = {
    "decontam-by-ngram": "rebuild eval excluding items with >=0.8 n-gram overlap; disclose decon method+corpus",
    "decontam-by-embedding-or-shingle": "drop items with token-F1>=0.8 to corpus; manual review 0.6-0.8 band",
    "temporal-gating": "LiveCodeBench-style: score items released AFTER model cutoff only; report pre/post gap",
    "rebuild-benchmark": "guessing above chance => items/leaks in training; rebuild with unseen items",
    "multi-surface-scoring": "score original + rephrased surfaces (C-BOD); report McNemar-significant deltas",
    "stratified-few-shot": "random non-adjacent exemplars, fixed seed, report 0/2/5/8-shot curve",
    "permutation-ensemble": "majority-vote content over all option permutations (PriDe/permutation debias)",
    "content-rubrics": "blind judge: strip response identifiers/format tells; rubric on content, not style",
    "double-swap-averaging": "judge every pair in both orders; order-dependent verdicts count as ties",
    "length-controlled-scoring": "AlpacaEval-2 style length control; anti-verbosity rubric halves residual",
    "content-sanitization": "reject/strip html comments, zero-width chars, instruction-override strings from judged text",
    "multi-seed-mean-and-CI": "3+ seeds, mean + Wilson/bootstrap CI; never report single-run scores",
}

def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def ledger_path(name=None):
    return os.environ.get("BENCHSCAN_LEDGER") or os.path.join(
        os.getcwd(), f".bra_history_{name or 'default'}.jsonl")

def read_jsonl(path):
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out

# ── statistics helpers (all deterministic, stdlib math) ─────────────────────
def norm_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def gammaincc_Q(a, x):
    """Regularized upper incomplete gamma Q(a,x) via series/continued fraction."""
    if x < 0 or a <= 0:
        return float("nan")
    if x < a + 1.0:   # series for P, return 1-P
        ap, s, d = a, 1.0 / a, 1.0 / a
        for _ in range(200):
            ap += 1; d *= x / ap; s += d
            if abs(d) < abs(s) * 1e-14:
                break
        return max(0.0, min(1.0, 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))))
    b, c, d = x + 1 - a, 1e30, 1.0 / (x + 1 - a)
    h = d
    for i in range(1, 200):
        an = -i * (i - a)
        b += 2
        d = an * d + b;  d = 1e-30 if abs(d) < 1e-30 else d
        c = b + an / c;  c = 1e-30 if abs(c) < 1e-30 else c
        d = 1.0 / d
        h *= d * c
        if abs(d * c - 1.0) < 1e-14:
            break
    return max(0.0, min(1.0, math.exp(-x + a * math.log(x) - math.lgamma(a)) * h))

def chi2_sf(x, df):
    return gammaincc_Q(df / 2.0, x / 2.0)

def binom_two_sided_p(k, n, p):
    """Small-n exact two-sided binomial p (probability of outcome at least as
    extreme as k under B(n,p)); large-n normal approx with continuity corr."""
    if n <= 0:
        return 1.0
    if n > 10000:
        z = (abs(k - n * p) - 0.5) / math.sqrt(n * p * (1 - p) + 1e-12)
        return max(0.0, min(1.0, 2 * (1 - norm_cdf(z))))
    from math import comb
    pk = comb(n, k) * p ** k * (1 - p) ** (n - k)
    tot = 0.0
    for i in range(0, n + 1):
        pi = comb(n, i) * p ** i * (1 - p) ** (n - i)
        if pi <= pk + 1e-18:
            tot += pi
    return min(1.0, tot)

def mcnemar_p(b, c):
    """Exact McNemar (binomial on discordant pairs)."""
    n = b + c
    if n == 0:
        return 1.0
    return binom_two_sided_p(min(b, c), n, 0.5)

def wilson_ci(k, n, z=1.959963984540054):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    den = 1 + z * z / n
    ctr = (p + z * z / (2 * n)) / den
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, ctr - m), min(1.0, ctr + m))

def paired_bootstrap_ci(a, b, iters=2000):
    """Paired-bootstrap (percentile) CI for mean(b)-mean(a); deterministic —
    PRNG seeded by SHA256 of inputs so results are reproducible offline."""
    import random
    n = len(a)
    diffs = [bb - aa for aa, bb in zip(a, b)]
    obs = sum(diffs) / n
    seed = int.from_bytes(hashlib.sha256(
        json.dumps([a, b], separators=(",", ":")).encode()).digest()[:8], "big")
    rng = random.Random(seed)
    boot = []
    for _ in range(iters):
        s = sum(diffs[rng.randrange(n)] for _ in range(n)) / n
        boot.append(s)
    boot.sort()
    lo = boot[int(0.025 * iters)]; hi = boot[min(iters - 1, int(0.975 * iters))]
    return {"observed": obs, "ci95": [lo, hi], "iters": iters, "seed": seed}

# ── engines ──────────────────────────────────────────────────────────────────
def words(text):
    return re.sub(r"[^\w\s]", " ", str(text).lower()).split()

def word_ngrams(toks, n):
    if len(toks) < n:
        return {tuple(toks)} if toks else set()
    return {tuple(toks[i:i+n]) for i in range(len(toks) - n + 1)}

def cmd_contam(a):
    bench = read_jsonl(a.benchmark)
    corpus = read_jsonl(a.corpus)
    if not bench or not corpus:
        print("error: benchmark and corpus JSONL must be non-empty", file=sys.stderr); return 3
    n = max(4, a.n)
    corp_grams = {}
    dcache = []  # (id, toks, multiset-counts, shingles)
    for d in corpus:
        ct = words(d.get("text", ""))
        cc = {}
        for t in ct:
            cc[t] = cc.get(t, 0) + 1
        for g in word_ngrams(ct, n):
            corp_grams.setdefault(g, d.get("id"))
        csh = {frozenset(ct[i:i+SHINGLE_W]) for i in range(max(1, len(ct) - SHINGLE_W + 1))}
        dcache.append((d.get("id"), ct, cc, csh))
    items = []
    hits_exact, hits_para = 0, 0
    for bit in bench:
        toks = words(bit.get("text", ""))
        grams = word_ngrams(toks, n)
        short_item = len(toks) < n
        # short items (< n words) cannot form real n-grams: skip the overlap
        # metric rather than letting a coincidental singleton flag as 1.0
        ov = 0.0 if short_item else (
            (len([g for g in grams if g in corp_grams]) / len(grams)) if grams else 0.0)
        best_j, best_f1, best_doc = 0.0, 0.0, None
        sh = {frozenset(toks[i:i+SHINGLE_W]) for i in range(max(1, len(toks) - SHINGLE_W + 1))}
        tcnt = {}
        for t in toks:
            tcnt[t] = tcnt.get(t, 0) + 1
        for cid, ct, cc, csh in dcache:
            if len(sh) >= 2 and len(csh) >= 2:   # singleton-shingle Jaccard is degenerate
                j = len(sh & csh) / len(sh | csh)
                if j > best_j:
                    best_j = j
            inter = sum(min(v, cc.get(t, 0)) for t, v in tcnt.items())  # multiset F1
            f1 = (2 * inter / (len(toks) + len(ct))) if (toks or ct) else 0.0
            if f1 > best_f1:
                best_f1, best_doc = f1, cid
        row = {"id": bit.get("id"), "overlap": round(ov, 4),
               "para_f1": round(best_f1, 4), "para_jaccard": round(best_j, 4)}
        if short_item:
            row["short_item"] = True
        if ov >= OVERLAP_CONTAM:
            row["flag"] = "contaminated"; hits_exact += 1
        elif ov >= OVERLAP_SUSPECT:
            row["flag"] = "suspect"
        if best_f1 >= PARA_F1_FLAG:
            row["para_doc"] = best_doc; hits_para += 1
        items.append(row)
    N = len(bench)
    affected = hits_exact / N
    out = {"schema": "bra.contam.v1", "n_gram": n, "items": N,
           "exact": {"hits": hits_exact, "affected": round(affected, 4),
                     "thresholds": {"contaminated": OVERLAP_CONTAM, "suspect": OVERLAP_SUSPECT}},
           "paraphrase": {"hits": hits_para, "affected": round(hits_para / N, 4),
                          "para_f1_threshold": PARA_F1_FLAG,
                          "jaccard_threshold": JACCARD_FLAG, "shingle_w": SHINGLE_W},
           "rows": items[:200], "rows_truncated": len(items) > 200}
    # optional temporal channel: items carry "date"; --cutoff + --results join
    if a.cutoff:
        resmap = {}
        if a.results:
            for r in read_jsonl(a.results):
                resmap[r.get("id")] = int(r.get("ok", 0))
        pre = [i for i in bench if i.get("date") and i["date"] <= a.cutoff]
        post = [i for i in bench if i.get("date") and i["date"] > a.cutoff]
        if resmap and pre and post:
            ap = sum(resmap.get(i.get("id"), 0) for i in pre) / len(pre)
            bp = sum(resmap.get(i.get("id"), 0) for i in post) / len(post)
            out["temporal"] = {"cutoff": a.cutoff, "pre_n": len(pre), "post_n": len(post),
                               "pre_acc": round(ap, 4), "post_acc": round(bp, 4),
                               "gap_pp": round((ap - bp) * 100, 2),
                               "flag": (ap - bp) >= DATE_GAP_FLAG}
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_selection(a):
    runs = read_jsonl(a.runs)
    if not runs:
        print("error: runs JSONL empty", file=sys.stderr); return 3
    letters_all, correct_flags = [], []
    acc_by_run, unstable = {}, 0
    item_letters = []
    ensemble_fmt = False
    for it in runs:
        letters = [str(x).strip().upper() for x in it.get("letters", []) if str(x).strip()]
        gold = str(it.get("gold", "")).strip().upper()
        if "perms" in it:
            ensemble_fmt = True
        item_letters.append((letters, gold))
        letters_all.extend(letters)
        correct_flags.extend(1 if l == gold else 0 for l in letters)
        if len(set(letters)) > 1:
            unstable += 1
        for i, l in enumerate(letters):
            acc_by_run.setdefault(i, []).append(1.0 if l == gold else 0.0)
    # k from declared options when consistent across rows, else from the
    # observed letter alphabet (a 5-option MCQ must not be tested against a
    # k=4 uniform; MIXED per-item option counts have no single valid null)
    opt_counts = {len([str(x) for x in it.get("options", [])])
                  for it in runs if it.get("options")}
    k = (opt_counts.pop() if len(opt_counts) == 1 else 0) \
        or max((ord(l) - 64 for l in letters_all if "A" <= l <= "Z"), default=4) or 4
    obs = [letters_all.count(chr(65 + i)) for i in range(k)]
    tot = sum(obs) or 1
    # k<2 (single observed letter everywhere) degenerates chi2 (df 0) — report None
    chi2 = sum((o - tot / k) ** 2 / (tot / k) for o in obs) if k >= 2 else None
    chi2_p = round(chi2_sf(chi2, k - 1), 5) if (k >= 2 and chi2 is not None) else None
    chi2_small_n = tot < 5 * k     # chi2 asymptotics unreliable below 5 obs/cell
    mean_acc = sum(correct_flags) / len(correct_flags) if correct_flags else 0.0
    # per-run-index accuracy over FULL-LENGTH items only (ragged items would skew
    # higher indices toward items that merely recorded more runs)
    maxlen = max((len(ls) for ls, _ in item_letters), default=0)
    full = [(ls, g) for ls, g in item_letters if len(ls) == maxlen]
    accs = [sum(1.0 for ls, g in full if ls[i] == g) / len(full)
            for i in range(maxlen)] if full else [0.0]
    out = {"schema": "bra.selection.v1", "items": len(runs),
           "k_options": k, "runs_per_item": maxlen,
           "letter_counts": {chr(65 + i): obs[i] for i in range(k)},
           "letter_chi2": round(chi2, 4) if chi2 is not None else None,
           "letter_chi2_p": chi2_p,
           "chi2_small_n": chi2_small_n,
           "unstable_items": unstable, "unstable_share": round(unstable / len(runs), 4),
           "mean_acc": round(mean_acc, 4),
           "acc_by_run_index": [round(x, 4) for x in accs],
           "acc_range_pp": round((max(accs) - min(accs)) * 100, 2)}
    if ensemble_fmt:
        out["note"] = ("rows carry `perms` (ensemble format): selection metrics ignore "
                       "permutations; use the `ensemble` subcommand for vote semantics")
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_fewshot(a):
    curve = sorted((int(c.get("shots", 0)), float(c.get("acc", 0.0))) for c in read_jsonl(a.curve))
    if len(curve) < 2:
        print("error: need >=2 shot points", file=sys.stderr); return 3
    accs = [x for _, x in curve]
    rng = max(accs) - min(accs)
    mono = all(curve[i][1] <= curve[i + 1][1] + 1e-9 for i in range(len(curve) - 1))
    out = {"schema": "bra.fewshot.v1", "points": curve,
           "range_pp": round(rng * 100, 2), "monotonic": mono,
           "flag": rng >= FEWSHOT_RANGE_FLAG}
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_judge(a):
    js = read_jsonl(a.judgments)
    if not js:
        print("error: judgments JSONL empty", file=sys.stderr); return 3
    # pair-id → {ab: verdict, ba: verdict}; single-order rows count as 'ab'
    pairs = {}
    longer_wins, len_known = 0, 0
    echo_pairs, echo_better_for_longer_list = [], []
    terms = []
    if a.rubric_terms:
        # word-boundary matching: a rubric term "ai" must not match inside "fail"
        terms = [re.compile(r"\b" + re.escape(t.lower()) + r"\b")
                 for t in json.load(open(a.rubric_terms))]
    def canon(v, order):  # verdict in presented order → canonical candidate identity side 0/1/tie
        if v == "tie":
            return "tie"
        if order == "ab":
            return 0 if v == "a" else 1
        return 1 if v == "a" else 0
    inj_hits = 0
    for j in js:
        pairs.setdefault(j.get("pair"), {})[j.get("order", "ab")] = j.get("verdict", "tie")
        la, lb = j.get("len_a"), j.get("len_b")
        if isinstance(la, (int, float)) and isinstance(lb, (int, float)) and la != lb and j.get("verdict") in ("a", "b"):
            len_known += 1
            winner_len = la if j.get("verdict") == "a" else lb
            if winner_len > min(la, lb):
                longer_wins += 1
        ta, tb = j.get("text_a") or "", j.get("text_b") or ""
        for kind, pat in HIDDEN_PATTERNS:
            if pat.search(ta) or pat.search(tb):
                inj_hits += 1
                break
        if terms and ta and tb:
            tal, tbl = ta.lower(), tb.lower()
            ea = sum(len(p.findall(tal)) for p in terms); eb = sum(len(p.findall(tbl)) for p in terms)
            if ea != eb and j.get("verdict") in ("a", "b"):
                echo_pairs.append((j.get("pair"), j.get("verdict"),
                                   "a" if max(ea, eb) == ea else "b"))
    flips = tot = 0
    for pid, orders in pairs.items():
        v_ab, v_ba = orders.get("ab"), orders.get("ba")
        if v_ab is not None and v_ba is not None:
            tot += 1
            if canon(v_ab, "ab") != canon(v_ba, "ba"):
                flips += 1
    flip_rate = flips / tot if tot else None
    echo_w_in = sum(1 for _, v, hi in echo_pairs if v == hi)
    # T-3 needs significance: share>=0.6 AND >=8 echo-asymmetric pairs AND
    # binomial p<0.05 — small samples no longer trip the flag on noise alone
    echo_p = (round(binom_two_sided_p(echo_w_in, len(echo_pairs), 0.5), 5)
              if len(echo_pairs) >= 2 else None)
    echo_flag = (len(echo_pairs) >= 8 and echo_w_in / len(echo_pairs) >= 0.6
                 and echo_p is not None and echo_p < 0.05)
    pos = {"paired": tot, "flips": flips,
           "flip_rate": round(flip_rate, 4) if flip_rate is not None else None,
           "flag": (flip_rate is not None and flip_rate >= POSITION_FLIP_FLAG)}
    if tot == 0:
        pos["note"] = ("no pair carries both orders; judge every pair twice "
                       "(ab+ba) to enable flip analysis")
    out = {"schema": "bra.judge.v1", "judgments": len(js), "pairs": len(pairs),
           "position": pos,
           "verbosity": {"scorable": len_known, "longer_wins": longer_wins,
                         "share": round(longer_wins / len_known, 4) if len_known else None,
                         "p_vs_0.5": round(binom_two_sided_p(longer_wins, len_known, 0.5), 5) if len_known >= 8 else None,
                         "flag": len_known >= 8 and longer_wins / len_known >= VERBO_SHARE_FLAG,
                         "note": "length ties and tie verdicts are excluded from scoring"},
           "injection_payloads_detected": inj_hits,
           "rubric_echo": {"pairs": len(echo_pairs),
                           "winner_has_more_echo": echo_w_in,
                           "share": round(echo_w_in / len(echo_pairs), 4) if echo_pairs else None,
                           "p_vs_0.5": echo_p,
                           "flag": echo_flag}}
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_tsguess(a):
    """G-1: masked-choice guessing (TS-Guessing channel). Rows:
    {"guessed": n_correct, "questions": n, "choices": k}. Above-chance guessing
    of a benchmark item whose option CONTENTS were masked is a contamination
    signal (evidence: ChatGPT 57% on MMLU vs 25% chance)."""
    rows = read_jsonl(a.results)
    if not rows:
        print("error: results JSONL empty", file=sys.stderr); return 3
    out_rows = []
    for i, r in enumerate(rows):
        g, n, k = int(r.get("guessed", 0)), int(r.get("questions", 0)), int(r.get("choices", 4))
        if n <= 0 or k < 2 or g > n:
            print(f"error: row {i}: need 0<=guessed<=questions, choices>=2", file=sys.stderr)
            return 3
        base = 1.0 / k
        p = binom_two_sided_p(g, n, base)
        out_rows.append({"row": i, "guessed": g, "questions": n, "choices": k,
                         "rate": round(g / n, 4), "baseline": round(base, 4),
                         "p": round(p, 6), "flag": p < 0.05 and g / n > base})
    worst_p = min((r["p"] for r in out_rows), default=1.0)
    any_flag = any(r["flag"] for r in out_rows)
    tot_g = sum(r["guessed"] for r in out_rows); tot_n = sum(r["questions"] for r in out_rows)
    ks = {r["choices"] for r in out_rows}
    # pooling is only valid under a single shared baseline 1/k — heterogeneous
    # k would test the pooled rate against an arithmetically invalid null
    if len(ks) > 1:
        pooled = {"blocked": True,
                  "note": "mixed choice counts across rows; pooling disabled "
                          "(per-row p-values remain authoritative)"}
        pooled_flag = False
    else:
        base = 1.0 / out_rows[0]["choices"]
        p_pool = binom_two_sided_p(tot_g, tot_n, base)
        pooled = {"guessed": tot_g, "questions": tot_n,
                  "rate": round(tot_g / max(1, tot_n), 4),
                  "baseline": round(base, 4), "p": round(p_pool, 6),
                  "flag": p_pool < 0.05 and tot_g / max(1, tot_n) > base}
        pooled_flag = pooled["flag"]
    print(json.dumps({"schema": "bra.tsguess.v1", "rows": out_rows,
                      "pooled": pooled, "worst_p": worst_p,
                      "flag": pooled_flag or any_flag}, separators=(",", ":")))
    return 0


def cmd_compare(a):
    A = {r.get("id"): int(r.get("ok", 0)) for r in read_jsonl(a.a_preds)}
    B = {r.get("id"): int(r.get("ok", 0)) for r in read_jsonl(a.b_preds)}
    ids = [i for i in A if i in B]
    if len(ids) < 8:
        print("error: need >=8 matched prediction ids", file=sys.stderr); return 3
    pa = [A[i] for i in ids]; pb = [B[i] for i in ids]
    b_n = sum(1 for i in ids if A[i] == 1 and B[i] == 0)
    c_n = sum(1 for i in ids if A[i] == 0 and B[i] == 1)
    p_m = mcnemar_p(b_n, c_n)
    acca, accb = sum(pa) / len(pa), sum(pb) / len(pb)
    h = 2 * (math.asin(math.sqrt(accb)) - math.asin(math.sqrt(acca)))
    out = {"schema": "bra.compare.v1", "n": len(ids),
           "a": {"acc": round(acca, 4), "wilson95": [round(x, 4) for x in wilson_ci(sum(pa), len(pa))]},
           "b": {"acc": round(accb, 4), "wilson95": [round(x, 4) for x in wilson_ci(sum(pb), len(pb))]},
           "delta_pp": round((accb - acca) * 100, 2),
           "mcnemar": {"b": b_n, "c": c_n, "p": round(p_m, 5), "significant_0.05": p_m < 0.05},
           "cohens_h": round(h, 4),
           "bootstrap": paired_bootstrap_ci(pa, pb)}
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_ensemble(a):
    """WORKED mitigation M-PER: permutation majority vote over CONTENT.
    Each row: {item, gold, perms, letters}; perms[i][j] = canonical letter shown
    at DISPLAY slot j (label chr(65+j)) in run i, and letters[i] is the letter
    the model picked in that display. The vote's canonical content is therefore
    perms[i][ord(letters[i])-65]. raw_acc = FIRST-RUN letter accuracy vs gold —
    only meaningful as a "before" baseline when perms[0] is canonical order;
    compare delta_pp within the same file, never across files."""
    res = []
    raw_correct = ens_correct = 0
    for ri, it in enumerate(read_jsonl(a.runs)):
        votes = {}
        letters, perms = it.get("letters", []), it.get("perms", [])
        for i, L in enumerate(letters):
            L = str(L).strip().upper()
            if len(L) != 1 or not ("A" <= L <= "Z"):
                print(f"error: row {ri}: invalid option letter {L!r} "
                      "(need single A-Z)", file=sys.stderr)
                return 3
            if i < len(perms):
                perm = [str(x).upper() for x in perms[i]]
                slot = ord(L) - 65 if len(L) == 1 else -1
                content_letter = perm[slot] if 0 <= slot < len(perm) else L
            else:
                content_letter = L
            votes[content_letter] = votes.get(content_letter, 0) + 1
        decided = max(sorted(votes), key=votes.get) if votes else None
        gold = str(it.get("gold", "")).strip().upper()
        if letters:
            if str(letters[0]).strip().upper() == gold:
                raw_correct += 1
        if decided == gold:
            ens_correct += 1
        res.append({"item": it.get("item"), "gold": gold, "raw_first": letters[0] if letters else None,
                    "ensemble": decided, "votes": votes})
    n = len(res) or 1
    out = {"schema": "bra.ensemble.v1", "items": len(res),
           "raw_acc": round(raw_correct / n, 4), "ensemble_acc": round(ens_correct / n, 4),
           "delta_pp": round((ens_correct - raw_correct) / n * 100, 2),
           "rows": res[:200], "rows_truncated": len(res) > 200}
    print(json.dumps(out, separators=(",", ":")))
    return 0

def cmd_blind(a):
    """WORKED mitigation M-BLIND: strip/normalize judged text so the judge can't
    see identity/format tells or hidden injections."""
    rows = read_jsonl(a.input)
    out_rows = []
    stripped = 0
    hits = 0
    for r in rows:
        t = str(r.get("text", ""))
        t = CTRL_RE.sub(" ", t)                    # ANSI/control chars out first
        removed = []
        for kind, pat in HIDDEN_PATTERNS:
            found = pat.findall(t)
            if found:
                removed.append(kind)
                hits += len(found)
                t = pat.sub(" ", t)
        t = MODEL_RE.sub("[MODEL]", t)
        t = re.sub(r"\s+", " ", t).strip()  # judge-formatting normalization (intended)
        if removed:
            stripped += 1
        out_rows.append({**{k: v for k, v in r.items() if k != "text"}, "text": t,
                         "normalized": True, "stripped_kinds": removed})
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            for r in out_rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(json.dumps({"schema": "bra.blind.v1", "rows": len(out_rows),
                      "injection_like_removed": stripped, "injection_hits": hits,
                      "out": a.out or None}, separators=(",", ":")))
    return 0

def cmd_severity(a):
    inflation = min(1.0, abs(a.inflation) / 15.0)     # 15pp+ saturates
    affected = min(1.0, abs(a.affected) / 0.10)       # 10%+ of items saturates
    evidence = max(0.0, min(1.0, a.evidence))
    score = round(100 * (0.40 * inflation + 0.35 * affected + 0.25 * evidence))
    tier = "CRITICAL" if score >= 75 else "HIGH" if score >= 50 else "MEDIUM" if score >= 25 else "LOW"
    out = {"schema": "bra.severity.v1", "score_100": score, "tier": tier,
           "inputs": {"inflation_pp": a.inflation, "affected": a.affected, "evidence": evidence},
           "formula": SEV_FORMULA}
    print(json.dumps(out, separators=(",", ":")))
    return 4 if tier == "CRITICAL" else 0

# ── history ledger (hash-chained, per-benchmark target) ─────────────────────
def ledger_append(name, metrics):
    lp = ledger_path(name)
    entries = ledger_read(lp)
    prev = entries[-1]["hash"] if entries else "0" * 64
    rec = {"ts": now_iso(), "seq": len(entries), "target": name,
           "ruleset": RULESET_VERSION, "metrics": metrics, "prev": prev}
    rec["hash"] = hashlib.sha256(json.dumps(rec, separators=(",", ":")).encode()).hexdigest()
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(lp, flags, 0o600)
    try:
        os.fchmod(fd, 0o600)
        os.write(fd, (json.dumps(rec, separators=(",", ":")) + "\n").encode("utf-8"))
    finally:
        os.close(fd)

def ledger_read(path):
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]

def cmd_report(a):
    findings = []
    metrics = {}
    channels = {"run": 0}
    def sev_score(infl, aff, ev):
        ev = max(0.0, min(1.0, ev))   # match the documented clamp(ev,0,1)
        return round(100 * (0.40 * min(1, abs(infl) / 15) + 0.35 * min(1, abs(aff) / 0.10) + 0.25 * ev))
    # contamination channel
    if a.benchmark and a.corpus:
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_contam(a)
        if rc != 0:
            print("error: contam channel failed", file=sys.stderr); return 3
        c = json.loads(buf.getvalue())
        aff = c["exact"]["affected"]; hits = c["exact"]["hits"]
        metrics["contam_overlap_affected"] = aff
        metrics["para_hits"] = c["paraphrase"]["hits"]
        est_infl = aff * 15.0   # assumption disclosed in docs/evidence.md
        if hits:
            s = sev_score(est_infl, aff, 0.9)
            findings.append({"cat": "C-1", "severity_score": s, "tier": tier_of(s),
                             "affected": aff, "evidence": f"{hits}/{c['items']} items >=0.8 n-gram overlap"})
        if c["paraphrase"]["hits"]:
            pa = c["paraphrase"]["affected"]
            s = sev_score(pa * 12.0, pa, 0.7)
            findings.append({"cat": "C-2", "severity_score": s, "tier": tier_of(s),
                             "affected": pa, "evidence": f"{c['paraphrase']['hits']} items multiset token-F1>=0.8"})
        if "temporal" in c and c["temporal"].get("flag"):
            gap = c["temporal"]["gap_pp"]
            s = sev_score(gap, c["temporal"]["post_n"] / max(1, c["temporal"]["pre_n"] + c["temporal"]["post_n"]), 0.75)
            findings.append({"cat": "C-3", "severity_score": s, "tier": tier_of(s),
                             "affected": round(min(1.0, gap / 100), 4),
                             "evidence": f"pre/post-cutoff gap {gap}pp (pre {c['temporal']['pre_acc']} vs post {c['temporal']['post_acc']})"})
    if a.runs:
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_selection(a)
        if rc != 0:
            print("error: selection channel failed", file=sys.stderr); return 3
        s_out = json.loads(buf.getvalue())
        metrics["letter_chi2_p"] = s_out["letter_chi2_p"]
        metrics["unstable_share"] = s_out["unstable_share"]
        metrics["acc_range_pp"] = s_out["acc_range_pp"]
        # bias matters when not explained by correct content-following — but an
        # always-right model lucky on a degenerate gold distribution is no
        # excuse either: suppress only at near-perfect acc AND stable answers.
        chi2_sig = (not s_out.get("chi2_small_n")
                    and s_out["letter_chi2_p"] is not None
                    and s_out["letter_chi2_p"] < 0.05)
        lucky = s_out["mean_acc"] >= 0.995 and s_out["unstable_share"] < 0.05
        if (chi2_sig and not lucky) or s_out["unstable_share"] >= 0.25:
            aff = max(s_out["unstable_share"], 0.05)
            s = sev_score(s_out["acc_range_pp"], aff, 0.85)
            chi2_txt = (f", chi2 p={s_out['letter_chi2_p']}"
                        if s_out["letter_chi2_p"] is not None else "")
            findings.append({"cat": "P-3", "severity_score": s, "tier": tier_of(s), "affected": aff,
                             "evidence": f"unstable {s_out['unstable_share']*100:.1f}%, range {s_out['acc_range_pp']}pp{chi2_txt}"})
    if a.curve:
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_fewshot(a)
        if rc != 0:
            print("error: fewshot channel failed", file=sys.stderr); return 3
        f = json.loads(buf.getvalue())
        metrics["fewshot_range_pp"] = f["range_pp"]
        if f["flag"]:
            aff = 0.5  # unknown denominator; heuristic share, disclosed
            s = sev_score(f["range_pp"], aff, 0.6)
            findings.append({"cat": "P-2", "severity_score": s, "tier": tier_of(s), "affected": aff,
                             "evidence": f"shot-curve range {f['range_pp']}pp (monotonic={f['monotonic']})"})
    if a.judgments:
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_judge(a)
        if rc != 0:
            print("error: judge channel failed", file=sys.stderr); return 3
        j = json.loads(buf.getvalue())
        metrics["judge_flip_rate"] = j["position"]["flip_rate"]
        metrics["judge_verbosity_share"] = j["verbosity"]["share"]
        metrics["injection_payloads"] = j["injection_payloads_detected"]
        if j["position"]["flag"]:
            fr = j["position"]["flip_rate"]
            s = sev_score(fr * 100, 0.6, 0.9)
            findings.append({"cat": "E-1", "severity_score": s, "tier": tier_of(s), "affected": fr,
                             "evidence": f"order-flip rate {fr*100:.1f}% on {j['position']['paired']} pairs"})
        if j["verbosity"]["flag"]:
            vs = j["verbosity"]["share"]
            s = sev_score((vs - 0.5) * 100, 0.5, 0.8)
            findings.append({"cat": "E-2", "severity_score": s, "tier": tier_of(s), "affected": vs - 0.5,
                             "evidence": f"longer-response wins {vs*100:.0f}% (p={j['verbosity']['p_vs_0.5']})"})
        if j["injection_payloads_detected"]:
            s = sev_score(10.0, 0.2, 0.95)
            findings.append({"cat": "E-3", "severity_score": s, "tier": tier_of(s), "affected": 0.2,
                             "evidence": f"{j['injection_payloads_detected']} judgments contained hidden-instruction patterns"})
        if j["rubric_echo"].get("flag"):
            s = sev_score(8.0, 0.4, 0.7)
            findings.append({"cat": "T-3", "severity_score": s, "tier": tier_of(s), "affected": 0.4,
                             "evidence": f"winner echoes rubric terms more often ({j['rubric_echo']['winner_has_more_echo']}/{j['rubric_echo']['pairs']})"})
    if a.a_preds and a.b_preds:
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_compare(a)
        if rc != 0:
            print("error: compare channel failed", file=sys.stderr); return 3
        cmp_ = json.loads(buf.getvalue())
        metrics["mcnemar_p"] = cmp_["mcnemar"]["p"]
        metrics["delta_pp"] = cmp_["delta_pp"]
        if cmp_["mcnemar"]["significant_0.05"] and abs(cmp_["delta_pp"]) >= 1.0:
            s = sev_score(abs(cmp_["delta_pp"]), 0.5, 1.0 - cmp_["mcnemar"]["p"])
            findings.append({"cat": "P-1", "severity_score": s, "tier": tier_of(s), "affected": 0.5,
                             "evidence": f"rephrase delta {cmp_['delta_pp']}pp, McNemar p={cmp_['mcnemar']['p']}"})
    if getattr(a, "tsguess", None):
        channels["run"] += 1
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_tsguess(a)
        if rc != 0:
            print("error: tsguess channel failed", file=sys.stderr); return 3
        t = json.loads(buf.getvalue())
        metrics["tsguess_flag"] = t["flag"]
        if t["flag"]:
            pooled = t["pooled"]
            if pooled.get("blocked"):
                infl = 12.0
                ev_txt = ("masked-choice guessing above chance in at least one row "
                          "(pooled test blocked: mixed choice counts)")
            else:
                infl = min(15.0, round((pooled["rate"] - pooled["baseline"]) * 100, 2))
                ev_txt = (f"masked-choice guessing {pooled['rate']*100:.0f}% vs "
                          f"{pooled['baseline']*100:.0f}% chance (p={pooled['p']})")
            s = sev_score(infl, 0.05, 0.8)
            findings.append({"cat": "G-1", "severity_score": s, "tier": tier_of(s),
                             "affected": 0.05, "evidence": ev_txt})
    # registry discipline: every finding must resolve — catalogue AND mitigation
    for f in findings:
        assert f["cat"] in CATALOGUE, f"hallucinated catalogue id {f['cat']!r}"
        assert CATALOGUE[f["cat"]]["mitigation"] in MITIGATIONS, \
            f"catalogue id {f['cat']!r} cites unknown mitigation"
    worst = max([f["severity_score"] for f in findings], default=0)
    # partial honesty: with zero channels actually evaluated, "no findings at
    # threshold" is NOT evidence of robustness — say so in the verdict itself
    verdict = ("INSUFFICIENT_COVERAGE" if channels["run"] == 0 else
               "COMPROMISED" if worst >= 75 else "SUSPECT" if worst >= 50 else
               "CAUTION" if worst >= 25 else "ROBUST")
    rep = {"schema": "bra.report.v1", "target": a.name, "generated": now_iso(),
           "ruleset": RULESET_VERSION, "verdict": verdict, "worst_score": worst,
           "channels_run": channels["run"],
           "findings": [{**f, "title": CATALOGUE[f["cat"]]["title"],
                         "mitigation": MITIGATIONS[CATALOGUE[f["cat"]]["mitigation"]]} for f in findings],
           "not_computable": [k for k, v in CATALOGUE.items() if not v["computable"]]}
    rep["report_sha256"] = hashlib.sha256(
        json.dumps(rep, separators=(",", ":")).encode()).hexdigest()
    metrics["verdict"] = verdict
    metrics["worst_score"] = worst
    metrics["report_sha256"] = rep["report_sha256"]
    try:
        ledger_append(a.name, metrics)
    except OSError as e:
        print(f"warning: ledger unwritable ({e}) — run unaudited", file=sys.stderr)
    if a.out:
        try:
            with open(a.out, "w", encoding="utf-8") as f:
                f.write(render_report_md(rep, metrics))
        except OSError as e:
            print(f"error: cannot write {a.out}: {e}", file=sys.stderr); return 3
    print(json.dumps(rep, separators=(",", ":")))
    # rc 4 on policy FAIL: COMPROMISED verdict, or INSUFFICIENT_COVERAGE —
    # a CI gate must never treat an empty-coverage audit as a pass
    return 4 if verdict in ("COMPROMISED", "INSUFFICIENT_COVERAGE") else 0

def tier_of(score):
    return "CRITICAL" if score >= 75 else "HIGH" if score >= 50 else "MEDIUM" if score >= 25 else "LOW"

def md_escape(s):
    return str(s).replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|") \
                 .replace("<", "\\<").replace(">", "\\>")

def render_report_md(rep, metrics):
    L = [f"# Benchmark Robustness Report — {md_escape(rep['target'])}", "",
         f"- Verdict: **{rep['verdict']}** (worst severity {rep['worst_score']}/100; channels run: {rep.get('channels_run', 0)})",
         f"- Generated: {rep['generated']} · ruleset {rep['ruleset']} · report sha256 `{rep['report_sha256'][:16]}…`",
         "", "## Findings"]
    if rep["verdict"] == "INSUFFICIENT_COVERAGE":
        L.append("**No audit channels were evaluated** (no input files matched any "
                 "channel) — zero findings here is not evidence of robustness.")
    elif not rep["findings"]:
        L.append("No computable-channel findings at/above thresholds (coverage: "
                 f"{rep.get('channels_run', 0)} channel(s)).")
    for f in sorted(rep["findings"], key=lambda x: -x["severity_score"]):
        L += ["", f"### [{f['cat']}] {md_escape(f['title'])} — {f['tier']} ({f['severity_score']}/100)",
              f"- Evidence: {md_escape(f['evidence'])}", f"- Affected: {f['affected']}",
              f"- Mitigation: {md_escape(f['mitigation'])}"]
    L += ["", "## Not computable offline (honest gap)",
          "These catalogue exploit classes need data the engine cannot see offline: "
          + ", ".join(f"`{k}`" for k in rep["not_computable"]),
          "", "## Metrics", "```json", json.dumps(metrics, indent=2), "```"]
    return "\n".join(L) + "\n"

def cmd_trend(a):
    entries = [r for r in ledger_read(ledger_path(a.name)) if r.get("target") == a.name]
    if len(entries) < 2:
        print(json.dumps({"schema": "bra.trend.v1", "target": a.name,
                          "note": "need >=2 audited runs — run `report` twice"}, separators=(",", ":")))
        return 0
    pre, cur = entries[-2]["metrics"], entries[-1]["metrics"]
    keys = ["contam_overlap_affected", "unstable_share", "judge_flip_rate",
            "judge_verbosity_share", "acc_range_pp", "fewshot_range_pp", "injection_payloads"]
    deltas = {}
    net = 0
    for k in keys:
        if k in pre and k in cur and isinstance(pre[k], (int, float)) and isinstance(cur[k], (int, float)):
            d = round(cur[k] - pre[k], 4)
            if d:
                deltas[k] = d
                net += 1 if d > 0 else (-1 if d < 0 else 0)
    degrading = cur.get("worst_score", 0) - pre.get("worst_score", 0)
    direction = ("REGRESSED" if degrading > 0 or net > 0 else
                 "IMPROVED" if degrading < 0 or net < 0 else "UNCHANGED")
    print(json.dumps({"schema": "bra.trend.v1", "target": a.name, "direction": direction,
                      "worst_prev": pre.get("worst_score"), "worst_now": cur.get("worst_score"),
                      "metric_deltas": deltas}, separators=(",", ":")))
    return 1 if direction == "REGRESSED" else 0

def cmd_audit(a):
    p = ledger_path(a.name)
    bad, prev = [], "0" * 64
    entries = ledger_read(p)
    for i, r in enumerate(entries):
        r2 = dict(r)               # copy: never mutate the caller's entries
        h = r2.pop("hash", None)
        calc = hashlib.sha256(json.dumps(r2, separators=(",", ":")).encode()).hexdigest()
        r = r2
        if r.get("prev") != prev or calc != h:
            bad.append(i)
        prev = h or prev
    print(json.dumps({"schema": "bra.audit.v1", "ledger": p, "chain_ok": not bad,
                      "entries": len(entries), "bad_lines": bad}, separators=(",", ":")))
    return 0 if not bad else 4

DOCTOR = {"schema": "bra.doctor.v1", "python": None, "ruleset": RULESET_VERSION,
          "catalogue": CATALOGUE, "mitigations": MITIGATIONS,
          "thresholds": {"overlap_contam": OVERLAP_CONTAM, "overlap_suspect": OVERLAP_SUSPECT,
                         "para_f1": PARA_F1_FLAG, "jaccard_flag": JACCARD_FLAG,
                         "position_flip": POSITION_FLIP_FLAG,
                         "verbo_share": VERBO_SHARE_FLAG, "fewshot_range": FEWSHOT_RANGE_FLAG,
                         "date_gap": DATE_GAP_FLAG, "char_n_default": CHAR_N_DEFAULT},
          "severity_formula": SEV_FORMULA,
          "contracts": ["bra.doctor.v1", "bra.contam.v1", "bra.selection.v1", "bra.fewshot.v1",
                        "bra.judge.v1", "bra.compare.v1", "bra.ensemble.v1", "bra.blind.v1",
                        "bra.severity.v1", "bra.report.v1", "bra.trend.v1", "bra.audit.v1",
                        "bra.tsguess.v1"]}


def main():
    ap = argparse.ArgumentParser(prog="benchscan.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("contam"); p.add_argument("--benchmark", required=True); p.add_argument("--corpus", required=True)
    p.add_argument("--n", type=int, default=CHAR_N_DEFAULT); p.add_argument("--cutoff"); p.add_argument("--results")
    p = sub.add_parser("selection"); p.add_argument("--runs", required=True)
    p = sub.add_parser("fewshot"); p.add_argument("--curve", required=True)
    p = sub.add_parser("judge"); p.add_argument("--judgments", required=True); p.add_argument("--rubric-terms")
    p = sub.add_parser("compare"); p.add_argument("--a-preds", required=True); p.add_argument("--b-preds", required=True)
    p = sub.add_parser("tsguess"); p.add_argument("--results", required=True)
    p = sub.add_parser("ensemble"); p.add_argument("--runs", required=True)
    p = sub.add_parser("blind-normalize"); p.add_argument("--input", required=True); p.add_argument("-o", "--out")
    p = sub.add_parser("severity"); p.add_argument("--inflation", type=float, required=True)
    p.add_argument("--affected", type=float, required=True); p.add_argument("--evidence", type=float, default=0.5)
    p = sub.add_parser("report"); p.add_argument("--name", required=True)
    for ch in ("benchmark", "corpus", "runs", "judgments", "curve", "a-preds", "b-preds",
               "cutoff", "results", "rubric-terms", "tsguess"):
        p.add_argument(f"--{ch}")
    p.add_argument("--n", type=int, default=CHAR_N_DEFAULT); p.add_argument("-o", "--out")
    p = sub.add_parser("trend"); p.add_argument("--name", required=True)
    p = sub.add_parser("audit"); p.add_argument("--name", default="default"); p.add_argument("--verify", action="store_true")
    sub.add_parser("doctor")
    a = ap.parse_args()
    if a.cmd == "doctor":
        d = {**DOCTOR, "python": sys.version.split()[0]}
        print(json.dumps(d, indent=2))
        return 0
    fn = {"contam": cmd_contam, "selection": cmd_selection, "fewshot": cmd_fewshot,
          "judge": cmd_judge, "compare": cmd_compare, "ensemble": cmd_ensemble,
          "blind-normalize": cmd_blind, "severity": cmd_severity, "report": cmd_report,
          "tsguess": cmd_tsguess, "trend": cmd_trend, "audit": cmd_audit}[a.cmd]
    try:
        return fn(a)
    except FileNotFoundError as e:
        print(f"error: input file missing: {e.filename}", file=sys.stderr); return 3
    except json.JSONDecodeError as e:
        print(f"error: malformed JSONL: {e}", file=sys.stderr); return 3
    except AssertionError as e:
        print(f"benchscan internal (ruleset discipline): {e}", file=sys.stderr); return 2

if __name__ == "__main__":
    sys.exit(main())
