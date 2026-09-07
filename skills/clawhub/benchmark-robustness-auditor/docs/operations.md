# Operations — benchscan.py command reference

Every subcommand prints one compact JSON document to stdout (`schema: bra.*.v1`)
and exits 0/1/2/3/4 (see manifest). Inputs are JSONL — one object per line.

## doctor

Catalogue (17 ids with `computable` flags), mitigations, thresholds, severity
formula, contract list. Use it to sanity-check an install and to keep your own
prose honest — only cite ids you saw here.

## contam — C-1/C-2/C-3

    benchscan.py contam --benchmark bench.jsonl --corpus corpus.jsonl \
        [--n 13] [--cutoff YYYY-MM-DD --results preds.jsonl]

- benchmark/corpus rows: `{"id","text","date"?}`
- C-1: word n-gram overlap per benchmark item vs the corpus. Item overlap
  ≥0.8 → `contaminated`; ≥0.3 → `suspect`. (Word-level tokenization after
  lowercase+punct-normalization.)
- C-2: multiset token-F1 (primary; ≥0.8 flags near-duplicate paraphrase and
  records `para_doc`, the closest corpus id) plus word-5-gram shingle Jaccard
  as a secondary informational metric (guarded: requires ≥2 shingles on both
  sides so singleton-shingle pairs can't degenerate to 1.0).
- Items shorter than `--n` words can't form real n-grams: their overlap is
  reported 0.0 with `short_item: true` instead of a coincidental 1.0 flag.
- C-3 (optional): with `--cutoff` + `--results` (`{"id","ok":0|1}`), splits
  dated items pre/post cutoff and flags a pre-minus-post gap ≥10pp
  (LiveCodeBench pattern).
- Output rows capped at 200 per run (token hygiene); add your own paging if needed.

## tsguess — G-1

    benchscan.py tsguess --results rows.jsonl      # {"guessed","questions","choices"}

Exact two-sided binomial vs chance 1/k, per row and pooled. `flag` when
p<0.05 AND rate>baseline. **Pooling is only valid under one shared k**: rows
with different `choices` yield `pooled.blocked:true` and the per-row p-values
stay authoritative (heterogeneous k would test against an invalid null).
Input is the MODEL's masked-choice guess accuracy (you run the guessing; the
tool decides significance).

## selection — P-3

    benchscan.py selection --runs runs.jsonl       # {"item","gold","letters":[...]}

Chi² letter distribution vs uniform (regularized-gamma survival), per-item
instability share (>1 distinct letter across runs), and accuracy by run index
(computed over full-length items only, so ragged runs don't skew indices).
The option count k comes from `options` when all rows agree on the same
count (mixed per-item counts fall back to the observed alphabet — a mixed-k
file has no single valid null), else from the observed letter alphabet
(a 5-option MCQ is never tested against a k=4 uniform).
Guardrails surfaced in the JSON: `chi2_small_n` (<5 obs/cell → the report
won't auto-flag on chi² alone), single-letter degenerate input (k<2 →
`letter_chi2_p:null`), and a `note` when rows look like ensemble format.
Report-level flag suppression applies only to the near-case: `mean_acc≥0.995`
AND `unstable_share<0.05`.

## fewshot — P-2

    benchscan.py fewshot --curve curve.jsonl       # {"shots","acc"} (≥2 points)

Shot-curve range in pp + monotonicity; flag at ≥8pp.

## judge — E-1/E-2/E-3/T-3

    benchscan.py judge --judgments j.jsonl [--rubric-terms terms.json]

Rows: `{"pair","order":"ab"|"ba","verdict":"a"|"b"|"tie","len_a"?,"len_b"?,"text_a"?,"text_b"?}` —
verdict is in PRESENTED order; supply both orders per pair for flip analysis.

- position: order-flip rate over doubly-judged pairs; flag ≥0.10. Pairs seen
  in only one order surface a `note` instead of silently skipping analysis.
- verbosity: longer-response-wins share (needs ≥8 scorable rows for the
  exact binomial p); flag ≥0.60 with evidence p. Length ties and tie verdicts
  are excluded from scoring.
- E-3: five hidden-injection families scanned inside `text_a/text_b`,
  deliberately precision-over-recall: authority laundering is line-anchored
  and score-override requires an imperative verb, so innocent `"score 100%"`
  or mid-sentence `"as the judge said"` don't trip.
- T-3: word-boundary rubric-term counting; flag needs share ≥0.60 AND ≥8
  echo-asymmetric pairs AND exact binomial p<0.05.

## compare — model-vs-model stats

    benchscan.py compare --a-preds a.jsonl --b-preds b.jsonl   # {"id","ok":0|1}

McNemar exact p on discordant pairs; Wilson 95% CIs; Cohen's h; deterministic
paired-bootstrap 95% CI on the accuracy delta (PRNG seeded by input SHA-256 —
same bytes ⇒ identical CI). Requires ≥8 matched ids (rc 3 below).

## ensemble — WORKED P-3 mitigation

    benchscan.py ensemble --runs ens.jsonl
    # {"item","gold","perms":[[...run permutations...]],"letters":[...]}

`perms[i][j]` is the canonical letter shown at display slot j in run i; the
model's display-letter choice L maps back to canonical content `perms[i][slot(L)]`.
Majority vote over mapped contents. `raw_acc` is FIRST-RUN letter accuracy vs
gold — a fair "before" baseline only when `perms[0]` is canonical order;
compare `delta_pp` within one file, never across files. Ties break
deterministically (alphabetically-earliest letter wins). Use it to prove the
mitigation closes the instability your `selection` run measured.

## blind-normalize — WORKED E-3/judge mitigation

    benchscan.py blind-normalize --input responses.jsonl [-o clean.jsonl]

Strips control/ANSI chars and the five hidden-injection families (hit counts
in `injection_hits`, per-row strip tags in `stripped_kinds`,
`injection_like_removed` counts rows touched), neutralizes model-identity
tells to `[MODEL]` (gpt/claude/gemini/llama-N/qwenN|qwen-*/deepseek/mistral/
mixtral/grok-N/gemma/phi/command-r/yi-N/codellama — version-anchored to avoid
scrubbing innocent text), then collapses whitespace (intended judge
normalization; note it flattens paragraph structure).

## severity

    benchscan.py severity --inflation PP --affected FRAC --evidence PRB

One formula (see manifest); tiers at 75/50/25; **rc 4 at CRITICAL** so CI can
gate directly on it.

## report — compose + remember

    benchscan.py report --name TARGET [--benchmark .. --corpus .. --cutoff .. --results .. \
        --runs .. --curve .. --judgments .. --a-preds .. --b-preds ..] [-o report.md]

Runs each channel whose inputs are present (contam/selection/fewshot/judge/
compare/tsguess), emits findings (static-catalogue disciplined — the engine
asserts every finding's catalogue id AND mitigation resolve) with severity
scores + mitigations, verdict ROBUST/CAUTION/SUSPECT/COMPROMISED (rc 4 on
COMPROMISED) — or **INSUFFICIENT_COVERAGE when zero channels ran**, so a
partial invocation can never masquerade as ROBUST. Also emits `channels_run`,
`report_sha256`, and a `not_computable` disclosure list. Renders a markdown
report with `-o` (findings/target text markdown-escaped). Appends metrics to
the ledger (`${BENCHSCAN_LEDGER:-./.bra_history_<name>.jsonl}`; O_NOFOLLOW,
0600, seq — set the env var in CI; the cwd default collides between users).

## trend / audit — self-improving loop memory

    benchscan.py trend --name TARGET     # IMPROVED/UNCHANGED/REGRESSED (rc1 on REGRESSED)
    benchscan.py audit --name TARGET [--verify]  # always verifies; chain_ok / bad_lines; rc4 on tamper

Trend compares the last two audited runs for the SAME target: deltas on
contam_overlap, unstable_share, judge flip/verbosity, acc ranges, injection
count, plus worst_score movement. Keyless-chain truth: `audit --verify`
proves existing records unmodified/unreordered; snapshot
`tail -1 LEDGER | sha256sum` out-of-band if you must exclude
append/tail-truncate by a fully-local attacker.

## Recipes

**Gate a benchmark build (CI):**

    python3 scripts/benchscan.py report --name qg-v3 --benchmark qg.jsonl --corpus crawl.jsonl \
        --runs mcq.jsonl || exit 1            # rc 4 = COMPROMISED
    python3 scripts/benchscan.py trend --name qg-v3 | jq .direction

**Prove the judge isn't being gamed:**

    python3 scripts/benchscan.py blind-normalize --input cands.jsonl -o cands_clean.jsonl
    # re-judge, then:
    python3 scripts/benchscan.py judge --judgments pairs.jsonl | jq '{f:.position.flip_rate,v:.verbosity.share}'

**A/B two models with defensible stats:**

    python3 scripts/benchscan.py compare --a-preds a.jsonl --b-preds b.jsonl | jq .mcnemar,.bootstrap
