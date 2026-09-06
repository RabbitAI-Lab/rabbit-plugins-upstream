# Changelog

## 2.0.0 (2026-09-06) — full functional rewrite

v1.x shipped marketing only: the registry payload is SKILL.md + README +
skill-card — **zero code** — while claiming "5 executable scripts", a
`severity_calculator.json`, a `mitigations/` library, payload packs, and
GitHub-API date checking. v2.0.0 replaces the shell with one real, offline,
stdlib-only engine (`scripts/benchscan.py`, ~750 LOC) plus an offline
regression suite.

**Added — detectors (all grounded in cited research, docs/evidence.md)**
- `contam` — C-1 word n-gram exact contamination (default n=13, GPT-3 lineage;
  thresholds 0.8 contaminated / 0.3 suspect); C-2 paraphrase via multiset
  token-F1 ≥0.8 (shingle Jaccard kept informational, min-2-shingle guard);
  short-item (<n words) guard; C-3 temporal channel: pre/post-cutoff accuracy
  gap (LiveCodeBench design, gap ≥10pp flags).
- `tsguess` — G-1 masked-choice guessing above chance: exact two-sided
  binomial vs the 1/k baseline (per-row; pooled refused on mixed choice
  counts). Wired into `report` (--tsguess).
- `selection` — P-3 option-letter/token bias: chi² letter distribution vs
  uniform (regularized-gamma p), per-item instability share, per-run accuracy
  dispersion (full-length items only); k derived from `options` or the
  observed alphabet; chi² suppressed below 5 obs/cell and against
  ≥0.995-accuracy stable models — an always-picks-"A" model is NOT
  exonerated merely because a degenerate gold set made it right.
- `fewshot` — P-2 shot-curve sensitivity: range in pp, monotonicity, ≥8pp flag.
- `judge` — E-1 position bias via order-flip rate on doubly-judged pairs
  (double-swap is also the shipped mitigation habit; single-order rows emit a
  note instead of silence); E-2 verbosity bias via longer-response-wins share
  with exact binomial p; T-3 rubric-echo (word-boundary matching, share≥0.6
  + ≥8 pairs + binomial p<0.05); E-3 hidden-instruction detection from five
  precision-tuned families (html comments, imperative instruction/score
  overrides, zero-width+directional chars, line-anchored authority
  laundering).
- `compare` — paired model-vs-model statistics: McNemar exact (discordant
  pairs), Wilson 95% CIs per model, Cohen's h, deterministic paired-bootstrap
  CI (PRNG seeded by SHA256 of inputs — reproducible offline).

**Added — worked mitigations**
- `ensemble` — permutation majority vote over answer CONTENT (fixes P-3 class:
  re-votes each run's letter back to canonical content and takes the majority).
- `blind-normalize` — sanitizes judged text: strips the five hidden-injection
  pattern classes and neutralizes model-identity tells (→ `[MODEL]`).

**Added — scoring / honesty / memory**
- `severity` — single documented formula
  `100*(0.40*min(1,|infl|/15)+0.35*min(1,|aff|/0.10)+0.25*ev)`, tiers at
  75/50/25; exits 4 at CRITICAL so CI can gate.
- `report` — composes whichever channels have inputs (contam/selection/
  fewshot/judge/compare/tsguess); findings cite ONLY the static 17-id
  catalogue (engine asserts id AND mitigation; rc 2 on violation —
  hallucinated exploit categories are impossible); `computable:false` ids are
  disclosed in every report instead of being fabricated; verdict ladder
  ROBUST/CAUTION/SUSPECT/COMPROMISED plus **INSUFFICIENT_COVERAGE when 0
  channels ran** (no false ROBUST on partial invocations — and it also
  returns **rc 4**, so a CI gate can't treat an empty audit as a pass);
  `channels_run` field; optional markdown report (escaped); `report_sha256`.
- `trend`/`audit` — hash-chained per-ledger history (`O_NOFOLLOW`, atomic
  0600, monotonic `seq`); trend emits IMPROVED/UNCHANGED/REGRESSED (rc 1)
  with per-metric deltas; `audit` always verifies the chain (rc 4 +
  `bad_lines` on tamper); default ledger path is cwd-relative (set
  BENCHSCAN_LEDGER in CI).
- JSON contracts `bra.*.v1`; deterministic outputs; 33-check offline selftest
  (33/33).

**Cross-model review (4 distributed lenses) found+fixed in this release**
(ensemble permutation→content mapping was an identity no-op; T-3/share
significance gating; precision-tuned injection patterns; mixed-k pooled
block; small-n chi² suppression; degenerate shingle guard; short-item
overlap guard; INSUFFICIENT_COVERAGE verdict; single-letter k<2 NaN guard).

**Removed / never re-add:** claims of bundled e5-mistral embedders, prompt-cache
integration, GitHub-API date checking (all need network/models), abstract
PoC-prompt lists for exploiting benchmarks (defense-only scope), and every
reference to files that never existed.

## 1.2.0 → 1.1.6
- Marketing README iterations; registry payload contained no scripts. Kept for history.
