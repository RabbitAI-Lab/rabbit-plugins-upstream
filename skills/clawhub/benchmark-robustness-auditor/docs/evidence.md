# Evidence — research groundings behind ruleset 2.0.0 (verified 2026-09-06)

Every threshold and detector below cites public literature. Honest caveat:
several numbers are *heuristic flags* (review queues), not universal laws —
that is why the engine also computes exact tests (McNemar/binomial/bootstrap).

## Contamination (C-1/C-2/C-3/G-1)

- **Word-13-gram** decontamination is the GPT-3 lineage (the GPT-3 paper
  marked eval examples with any 13-gram overlap; GPT-4 reports up to 40-gram
  filtering). Engine default `--n 13` mirrors that convention.
- **Thresholds 0.8/0.5-0.7**: practice writeups on n-gram overlap treat ≥0.8
  overlap as contamination and ~0.5–0.7 as suspicion; MinHash LSH guidance
  uses Jaccard ~0.5 for near-duplicate candidates (word-5 shingles) —
  embodied in the C-2 flag (≥0.5) and the 0.3–0.8 review band in C-1.
- **Temporal gating**: LiveCodeBench (Jain et al., ICLR 2025) tags problems
  with release dates and scores only post-cutoff items; documented pre/post
  drops (e.g., DeepSeek/GPT-4o/Codestral cliffs) motivate the ≥10pp gap flag.
- **Rephrase sensitivity**: C-BOD (EMNLP 2025) — avg ~2.75pp drop under
  modest rephrasing, >80% of models with McNemar-significant differences —
  motivates the P-1 channel (paired original/rephrased predictions through
  `compare`) and why McNemar is computed exactly, not eyeballed.
- **TS-Guessing (G-1)**: masked-choice guessing is an inference-level
  contamination signal — e.g. ChatGPT ~57% on MMLU masked vs 25% chance
  (Investigating Data Contamination; widely re-cited 2025–26). The engine
  takes your measured rate and returns exact binomial significance vs 1/k;
  pooling is refused across heterogeneous choice counts (invalid null).
- **GSM1K**: frontier models dropping up to ~13pp on a grade-school math
  mirror benchmark (memorization vs reasoning) — motivates the affected→
  inflation heuristic note in report C-1 (`est_infl = affected × 15pp`,
  DISCLOSED as a heuristic, not literature).

## Judge bias (E-1/E-2/E-3/T-3)

- **Position bias** 10–15pt swing (Zheng et al., LLM-as-a-Judge, NeurIPS 2023
  lineage; re-confirmed 2024–26). Structural, in the decode: prompt-only fixes
  measure ≈0 effect. Fix (also our mitigation doc): run BOTH orders, average,
  treat order-dependent verdicts as ties — hence the E-1 flip-rate metric
  (flag ≥0.10) and the double-swap habit in mitigations.
- **Verbosity bias** 15–30pt inflation for longer answers (Wang 2023,
  arXiv:2305.17926; length-controlled scoring à la AlpacaEval 2). Engine:
  longer-wins share with exact binomial p; flag ≥0.60.
- **Self-preference/self-enhancement** 10–25pt on same-family: cross-family
  judges are the only structural fix — documented, not computed (needs model
  identity provenance).
- **Format bias** 5–15pt; **calibration**: judges track humans at Cohen's
  κ>0.6 (target) and drift 3–8pt per judge swap — re-calibrate monthly. Both
  documented in mitigations, not offline-computable.
- **Hidden instruction injection (E-3)**: judge deceptions via
  html comments / instruction-override / score-override strings / zero-width
  chars / authority laundering — production-hardening writeups recommend
  force-structured judge outputs + input sanitization; the five regex
  families here are our offline-enforceable subset (and blind-normalize's
  strip list).

## Selection bias (P-3) & mitigations

- **"LLMs Are Not Robust Multiple Choice Selectors"** (Zheng et al., 2023,
  arXiv:2309.03882): 20 LLMs on MMLU/ARC/CSQA show selection (token-ID) bias;
  PriDe estimates a debiasing prior via option permutations on a subset.
  Our P-3 measures the same phenomenon (letter chi², instability) and
  `ensemble` is the worked permutation majority-vote variant.

## Statistics grounding (S stack)

- **McNemar for paired per-item correctness** — the field-standard paired
  binary test (as used by C-BOD; exact binomial computed here, df issues
  avoided).
- **Wilson intervals for accuracy CIs** — strongest coverage for small-N
  binary single-sample estimates (stats-for-evals guidance; e.g. ~80%±7.8pp
  at n=100 is the leaderboard-noise rule of thumb).
- **Paired bootstrap (percentile, deterministic)** — recommended for system
  comparisons (LREC 2022 "Please, Don't Forget the Difference and the
  Confidence Interval"); NOTE the BCa-vs-percentile coverage debate (percentile
  chosen, disclosed); seed = SHA256(inputs) for offline reproducibility.
- **Significance vs noise**: 1–2pp on typical N≈100–500 evals is inside CI;
  ~5pp+ is the practical bar. The engine prints CIs so agents stop
  hallucinating significance.
- Regularized-gamma chi² for letter distribution (standard survival function).

## Design notes added by cross-model review (2026-09-06, 4 lenses)

- **C-2 paraphrase metric**: primary is multiset token-F1 (threshold 0.8,
  embedding-analog band from the same decon literature); word-5-gram shingle
  Jaccard is kept informational (guarded: ≥2 shingles — two 6-token docs
  sharing one shingle must not score 1.0). Set-based F1 was rejected in
  review: vocab-overlap inflates on lexical twins and misses repeated-token
  structures.
- **Items shorter than n words** can't yield real n-grams: overlap is
  reported 0.0 + `short_item:true`, not a coincidental 1.0 flag.
- **P-3 chi² interplay**: a model that always picks the CORRECT letter is not
  bias — but an always-picks-"A" model lucky on a degenerate gold
  distribution isn't exonerated either. Suppression only at mean_acc≥0.995
  AND unstable<0.05; chi² additionally suppressed below 5 obs/cell
  (`chi2_small_n`) where the asymptotic p is unreliable.
- **T-3 significance**: grep-share alone trips on noise; flag requires ≥8
  echo-asymmetric pairs AND exact binomial p<0.05 AND share≥0.60.
- **E-3 precision over recall**: naive patterns (e.g. "score 100%", unanchored
  "as the judge ...") false-positive on honest content; the shipped patterns
  are deliberately narrower (imperative-verb score override; line-anchored
  authority; bounded comment span). Some reworded injections WILL evade
  detection — blind-normalize + both-sides judging is the structural defense,
  detection is the tripwire.
- **INSUFFICIENT_COVERAGE**: 0 channels run ⇒ 0 findings ⇒ must NOT read as
  ROBUST. Verdict makes coverage explicit (`channels_run` field).

## What we explicitly do NOT do (hallucination firewall)

- D-1/T-5/T-1/T-2/T-4: need training-data provenance / tool-call logs /
  paraphrase rescores / reasoning traces. They sit in the catalogue as
  `computable:false` and are DISCLOSED in reports — never fabricated.
- No CVE/vuln-db style lookups (offline); no embedding models (offline) —
  paraphrase detection is multiset-token-F1 + shingles by design, weaker than
  embeddings but deterministic and network-free.
- Ledger hash-chains are keyless: they prove records unmodified/unreordered
  but not append-or-truncate-at-tail by a fully-local attacker (snapshot head
  hashes out-of-band for that). Default ledger path is cwd-relative —
  set BENCHSCAN_LEDGER in CI to avoid multi-user collisions.
