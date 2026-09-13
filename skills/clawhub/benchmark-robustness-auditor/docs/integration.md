# Integration — wiring benchscan into eval pipelines & agents

Everything is one JSON document on stdout + an exit code. Parse rule: **trust
`schema`, read documented fields, branch on rc** — never scrape prose.

## Contracts

| Schema | From | Key fields |
|---|---|---|
| bra.doctor.v1 | doctor | catalogue, mitigations, thresholds, formula |
| bra.contam.v1 | contam | exact{hits,affected}, paraphrase{hits,para_f1_threshold}, rows[] (cap 200, `rows_truncated`), temporal? |
| bra.selection.v1 | selection | letter_chi2_p, chi2_small_n, k_options, unstable_share, mean_acc, acc_range_pp, note? |
| bra.fewshot.v1 | fewshot | range_pp, monotonic, flag |
| bra.judge.v1 | judge | position{flip_rate,flag,note?}, verbosity{share,p_vs_0.5,flag}, injection_payloads_detected, rubric_echo{pairs,winner_has_more_echo,share,p_vs_0.5,flag} |
| bra.compare.v1 | compare | a/b {acc,wilson95}, delta_pp, mcnemar{p}, bootstrap{ci95,seed}, cohens_h |
| bra.tsguess.v1 | tsguess | pooled{rate,baseline,p} or pooled{blocked,note}, rows[], flag |
| bra.ensemble.v1 | ensemble | raw_acc (first-run baseline), ensemble_acc, delta_pp, rows[], rows_truncated |
| bra.blind.v1 | blind-normalize | rows, injection_like_removed (rows touched), injection_hits, out |
| bra.severity.v1 | severity | score_100, tier, inputs, formula |
| bra.report.v1 | report | verdict (incl. INSUFFICIENT_COVERAGE), worst_score, channels_run, findings[], not_computable[], report_sha256 |
| bra.trend.v1 | trend | direction, worst_prev/now, metric_deltas |
| bra.audit.v1 | audit (always verifies) | chain_ok, entries, bad_lines |

## Exit-code routing

| rc | report | trend | severity | audit | detectors |
|---|---|---|---|---|---|
| 0 | not COMPROMISED, coverage ≥1 channel | improved/unchanged | not CRITICAL | chain ok | ok |
| 1 | — | REGRESSED | — | — | — |
| 2 | usage / ruleset trip | usage | usage | usage | usage |
| 3 | input/env error | — | — | — | input/env error |
| 4 | COMPROMISED or INSUFFICIENT_COVERAGE | — | CRITICAL | tampered | — |

Flags that SUPPRESS rather than fire (precision-first): P-3 chi² suppressed
when `chi2_small_n` or near-perfect accuracy with stable answers; T-3 needs
binomial p<0.05 AND ≥8 pairs; G-1 pooled blocks on mixed `choices`.

## Producing the input JSONLs (you own the runs; the tool audits)

An agent/harness runs the model, then writes JSONL audit artifacts:

- **MCQ runs**: repeat each item under k option permutations; log
  `{"item","gold","letters":[...]}` → `selection`. To REMEDIATE, also record
  each run's permutation as `perms` and use `ensemble`.
- **Judge pairs**: judge every pair twice (`order:"ab"`,`order:"ba"`) with the
  SAME rubric; log verdicts in presented order (+`len_a/len_b`; texts only if
  you want E-3/T-3 channels) → `judge`.
- **Contamination**: export benchmark items (`{"id","text","date"?}`) and the
  training-corpus sample (`{"id","text"}`) → `contam`. Add `--cutoff` +
  per-item correctness for the temporal channel.
- **Compare**: `{"id","ok":0|1}` per model over identical ids → `compare`.

## Agent recipes

**Benchmark release gate**

    python3 scripts/benchscan.py report --name qg-v3 \
      --benchmark qg.jsonl --corpus train.jsonl --runs mcq.jsonl \
      --judgments jr.jsonl -o gate.md || echo GATE-FAILED  # rc 4

**Remediation loop (self-improving)**

    python3 scripts/benchscan.py selection --runs mcq.jsonl | jq .unstable_share
    python3 scripts/benchscan.py ensemble  --runs mcq_ens.jsonl | jq '{raw:.raw_acc,ens:.ensemble_acc}'
    python3 scripts/benchscan.py report --name qg-v3 ...   # after fixes
    python3 scripts/benchscan.py trend  --name qg-v3       # expect IMPROVED

**Honest delta reporting between model versions**

    python3 scripts/benchscan.py compare --a-preds old.jsonl --b-preds new.jsonl \
      | jq '{delta_pp, p: .mcnemar.p, ci: .bootstrap.ci95}'
    # report delta ONLY if ci excludes 0 AND mcnemar p<0.05; else "within noise"

## Output hygiene for token-constrained agents

- `contam`'s `rows[]` is capped at 200; aggregate fields land first.
- Ask for fields with `jq` (as in recipes) instead of re-printing full JSONL
  back into the context.
- Severity/state fields are enums (ROBUST/CAUTION/SUSPECT/COMPROMISED,
  IMPROVED/UNCHANGED/REGRESSED) — branch on them instead of re-deriving.

## Notes

- Determinism: the bootstrap is seeded by input SHA-256 — byte-identical
  inputs give byte-identical CIs (don't "re-roll" to hunt for significance).
- Ledger: `${BENCHSCAN_LEDGER:-./.bra_history_<name>.jsonl}`; move it with the
  env var for a central CI history. 0600 + O_NOFOLLOW at creation.
- This is v2.0.0 examined across lenses before publish (distributed review);
  the 33-check selftest is the arbiter — merges only if all stay green.
