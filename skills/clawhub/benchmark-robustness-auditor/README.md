# benchmark-robustness-auditor v2.0.0

**Offline, defensive robustness audits for LLM benchmarks.** One stdlib python3
script, JSONL in / compact JSON out, zero network, zero install. Detects
contamination, exploitable selection/few-shot artifacts, and LLM-judge biases —
and ships two WORKED mitigations (permutation majority ensemble, blind content
normalization) plus a documented severity calculator with a hash-chained
history ledger so posture trends across runs.

| Capability | v1.x (registry) | v2.0.0 (this) |
|---|---|---|
| Executable scripts | claimed 5 + mitigations library; **registry ships zero code** | ✅ one engine, 12 subcommands, all functional |
| Contamination | abstract bash snippets | ✅ 13-gram exact + shingle-Jaccard paraphrase + temporal pre/post-cutoff gap + TS-Guessing (G-1) |
| Selection bias | "shuffles 4, variance" prose | ✅ chi² letter distribution, instability share, acc-per-run, **accomplice-aware flag** (right-always ≠ bias) |
| Judge bias | payload list in README | ✅ position flip rate, verbosity binomial, rubric-echo, E-3 hidden-instruction regexes |
| Score comparisons | — | ✅ McNemar exact + Wilson CIs + deterministic paired bootstrap (seed = hash of inputs) |
| Severity | "severity_calculator.json" (absent) | ✅ one documented formula, engine-backed tiers, rc 4 at CRITICAL |
| Mitigations | files promised, absent | ✅ `ensemble` (content majority vote) + `blind-normalize` (strips injections/identity tells) |
| Self-improvement | — | ✅ per-target hash-chained ledger + `trend` deltas (REGRESSED × rc1) |
| Honesty | claimed everything | ✅ catalogue marks T-1/T-2/T-4/T-5/D-1 `computable:false` — declared invisible, never fabricated |

## Quickstart

    python3 scripts/benchscan.py doctor                 # catalogue + thresholds + contracts
    python3 scripts/benchscan.py contam --benchmark bench.jsonl --corpus corpus.jsonl \
        --cutoff 2024-06-01 --results preds.jsonl
    python3 scripts/benchscan.py report --name my-bench --benchmark bench.jsonl \
        --corpus corpus.jsonl --runs runs.jsonl --judgments j.jsonl -o report.md
    python3 scripts/benchscan.py trend --name my-bench  # after ≥2 reports
    bash    scripts/selftest.sh                         # 33 offline checks

## Exit codes

| rc | meaning |
|---|---|
| 0 | ok |
| 1 | `trend` REGRESSED |
| 2 | usage / ruleset trip |
| 3 | input/env error |
| 4 | verdict COMPROMISED / severity CRITICAL / broken ledger chain |

Report verdicts: ROBUST / CAUTION / SUSPECT / COMPROMISED — plus INSUFFICIENT_COVERAGE when zero audit channels ran (never trust a “clean” report with 0 channels). Precision-first suppressions: P-3 chi² needs ≥5 obs/cell and isn't fired against a ≥0.995-accuracy model with stable answers; T-3 needs binomial p<0.05 AND ≥8 echo-asymmetric pairs; G-1 pooling blocks on mixed choice counts.

## Honest scope

Offline auditing has hard limits: proving a model did NOT train on a benchmark
requires training-data provenance the skill cannot see (D-1, T-5, T-1/T-2/T-4
stay `computable:false`). Every threshold is a documented heuristic grounded in
the citations in `docs/evidence.md` — treat outputs as a **defensible signal**,
not proof. Defensive use only.

## Layout

- `SKILL.md` — agent operating rules + input contracts
- `scripts/benchscan.py` — the engine
- `scripts/selftest.sh` — 33 offline regression checks
- `manifest.json` — entrypoints, contracts, catalogue discipline, thresholds
- `docs/operations.md` / `docs/evidence.md` / `docs/integration.md`
- `CHANGELOG.md` — history

License: MIT-0.
