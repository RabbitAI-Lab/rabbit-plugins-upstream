---
name: benchmark-robustness-auditor
description: >
  Offline, defensive robustness auditor for LLM benchmarks: n-gram exact +
  shingle-Jaccard paraphrase contamination, temporal pre/post-cutoff gaps,
  TS-Guessing above-chance detection, option-letter selection bias (chi2),
  few-shot curve noise, LLM-judge position/verbosity/rubric-echo bias and
  hidden-instruction payload detection, paired McNemar + Wilson + deterministic
  bootstrap for score comparisons, WORKED mitigations (permutation majority
  ensemble, blind content normalization), documented 0-100 severity formula,
  hash-chained per-target history ledger with trend deltas. Findings cite a
  STATIC 17-id exploit catalogue with explicit computable flags — invisible
  exploit classes are declared, never fabricated. 100% stdlib python3.
  NO network, NO telemetry. Defense/auditing only.
version: 2.0.0
category: research
topics: [llm-benchmarks, robustness, red-team, evaluation, contamination]
metadata:
  openclaw:
    emoji: "🔬"
    requires:
      bins: ["python3"]
    network:
      outbound: []
---

# 🔬 Benchmark Robustness Auditor v2.0.0 — executable defense edition

Honest replacement for v1 (registry ships SKILL.md+README only; the README's
"5 executable scripts", "severity_calculator.json", "mitigations/ library" —
none existed). Now every promised capability is real, stdlib-only Python, fully
offline. Details: `docs/operations.md` · research citations: `docs/evidence.md`
· agent/CI wiring: `docs/integration.md`.

> Defensive use only. This skill measures and mitigates benchmark exploits —
> never performs them for score inflation.

## Hard rules for the agent

1. Everything runs through `scripts/benchscan.py` with JSONL inputs and
   compact JSON outputs (`schema: bra.*.v1`). Subcommands: `contam`,
   `selection`, `fewshot`, `judge`, `compare`, `tsguess`, `ensemble`,
   `blind-normalize`, `severity`, `report`, `trend`, `audit`, `doctor`.
   Input contracts are in the tool docstring AND `manifest.json` — match them
   exactly; do not invent fields.
2. Exit codes are the contract: **0** ok · **1** trend REGRESSED · **2**
   usage/ruleset trip · **3** input/env error · **4** report verdict
   COMPROMISED (or severity CRITICAL, or broken ledger chain).
3. Findings ONLY cite catalogue ids from `doctor` (C-1..M-1, G-1). The engine
   hard-fails on unknown ids — do the same when summarizing: if it's not in
   the catalogue, say it's out of scope instead of inventing a category.
   `computable:false` ids (T-1/T-2/T-4/T-5/D-1) require data the engine cannot
   see offline — say exactly that; never fabricate evidence for them.
4. Severity is ONE documented formula (see `doctor.severity_formula`,
   identical string in `manifest.json`); report `score_100` + tier, don't
   re-derive ad-hoc numbers in prose. A report with zero channels evaluated
   is `INSUFFICIENT_COVERAGE` — never present that as ROBUST.
5. `report` appends to a hash-chained ledger (0600, O_NOFOLLOW;
   `${BENCHSCAN_LEDGER:-./.bra_history_<name>.jsonl}` — set it in CI; the
   default lives in cwd and collides if two users share one). `audit` always
   verifies the chain (rc 4 = tampered); `--verify` is accepted for compat.
   Keyless-chain limits documented — snapshot head hashes out-of-band for
   adversarial settings.
6. Modest claims: thresholds are documented heuristics grounded in citations
   (docs/evidence.md), not laws. Small N → wide CIs; the engine computes
   Wilson/McNemar/bootstrap so you never have to guess significance.

## Quickstart

    python3 scripts/benchscan.py doctor
    python3 scripts/benchscan.py contam --benchmark bench.jsonl --corpus train_corpus.jsonl \
        --cutoff 2024-06-01 --results model_preds.jsonl
    python3 scripts/benchscan.py selection --runs mcq_runs.jsonl
    python3 scripts/benchscan.py judge --judgments judge_pairs.jsonl --rubric-terms terms.json
    python3 scripts/benchscan.py compare --a-preds modelA.jsonl --b-preds modelB.jsonl
    python3 scripts/benchscan.py report --name my-bench --benchmark ... --corpus ... -o report.md
    python3 scripts/benchscan.py trend --name my-bench      # IMPROVED/REGRESSED across runs
    bash    scripts/selftest.sh                             # 33 offline checks

## Input contracts (JSONL; one object per line)

- benchmark/corpus: `{"id","text","date"?}`
- runs (selection): `{"item","gold","letters":[..]}`
- ensemble: `{"item","gold","perms":[[..]..],"letters":[..]}`
- curve: `{"shots","acc"}` · preds: `{"id","ok":0|1}`
- judgments: `{"pair","order":"ab|ba","verdict":"a|b|tie","len_a"?,"len_b"?,"text_a"?,"text_b"?}`
- tsguess: `{"guessed","questions","choices"}`
