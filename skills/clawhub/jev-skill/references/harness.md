# Jev evaluation harness

`scripts/jev_harness.py` is a small, dependency-free runner for Jev golden
sets. It validates typed question definitions, optionally calls the TypeSafe
System One endpoint concurrently, and reports accuracy, calibration,
reliability, latency, and token usage. It does not print state or API keys.

## Input files

Questions are a JSON object:

```json
{
  "urgent": {
    "type": "noul",
    "instructions": "Does this message require urgent attention?"
  },
  "team": {
    "type": "choice",
    "instructions": "Which team should handle this?",
    "criteria": {
      "billing": "Charges or refunds",
      "technical": "Bugs or integration failures",
      "other": "None of the above"
    }
  },
  "severity": {
    "type": "score",
    "instructions": "How severe is the issue?",
    "criteria": ["Minor", "Material", "Critical"]
  }
}
```

Cases are JSONL. `expected` is optional for collection-only runs; include it
for accuracy:

```json
{"id":"ticket-1","tags":["golden","billing"],"state":{"message":"I was charged twice.","tier":"pro"},"expected":{"urgent":true,"team":"billing","severity":{"level":1,"tolerance":0.5}}}
```

Expected Noul values are booleans or `0`/`1`; Choice values are option keys;
Score values are numeric levels. A Score may also use
`{"level": 1, "tolerance": 0.5}` for a case-specific tolerance. The harness
treats a Noul probability of at least `0.5` as the predicted yes/no label and
reports the raw probability too. For Choice and Score it reports the returned
confidence. These are evaluation defaults, not universal production
thresholds. `tags` is optional and is intended for slices such as `golden`,
`metamorphic`, `adversarial`, `numeric`, `date-time`, or `context-rot`.

## Run it

Validate without a key:

```bash
python3 scripts/jev_harness.py \
  --questions questions.json \
  --cases cases.jsonl \
  --validate-only
```

Run against Jev:

```bash
export TYPESAFE_API_KEY='…'
python3 scripts/jev_harness.py \
  --questions questions.json \
  --cases cases.jsonl \
  --output jev-report.json \
  --concurrency 4
```

For a reproducible benchmark, pin the resolved model version; use the alias
for a moving canary:

```bash
python3 scripts/jev_harness.py --questions questions.json --cases cases.jsonl \
  --model jev-1.13.0 --tag golden
```

Useful CI/evaluation controls:

```bash
python3 scripts/jev_harness.py \
  --questions questions.json \
  --cases cases.jsonl \
  --min-accuracy 0.90 \
  --max-error-rate 0 \
  --max-noul-brier 0.12 \
  --max-score-mae 0.40 \
  --input-price-per-million 0.042 \
  --output-price-per-million 0
```

The command exits non-zero when a case fails, a response is malformed, or a
requested gate fails. `--offset`, `--limit`, repeated `--case-id`, and repeated
`--tag` support shards and targeted debugging; all supplied tags must be
present on a selected case. `--noul-threshold` and `--score-tolerance` control
evaluation policy without changing the questions. Pricing is always opt-in so
stale provider pricing is never silently assumed.

The runner validates the documented response contract before scoring: every
question must have a matching typed answer; Choice probabilities must cover
the criteria; Score legends and probability keys must cover every level; all
probabilities, confidence values, scores, and token counts must be finite and
in range. It reports Noul accuracy, Brier score, log loss, precision/recall/F1
and a confusion matrix; Choice accuracy, confidence and confusion; Score level
accuracy, tolerance hit rate, MAE and RMSE; expected calibration error and
confidence-threshold selective coverage; per-question and per-tag slices; plus
mean/p50/p95 latency, state byte sizes, retry attempts, resolved model IDs,
request IDs, and token totals. Missing usage is recorded as a warning, not a
false response failure, because the SDK response surface allows usage to be
absent.

It retries transient `408`, `429`, `500`, `502`, `503`, `504`, and `529`
responses with bounded full-jitter backoff, honoring `Retry-After` when
present. The API key and input state are never written to the report. Keep
golden sets and reports out of source control when they contain customer or
other sensitive data. Use representative, adversarial cases and compare Jev
with the existing model or rule-based baseline before shipping thresholds.

## Build the strongest suite

Do not rely on a large random sample alone. Keep a small, reviewed suite for
each known jaggedness family: literal and indirect references, arithmetic and
numeric formats, dates/time zones, contradictory or prompt-injected content,
missing evidence, structural invariants, and large irrelevant context. Add
metamorphic variants that reorder irrelevant fields or add distractors while
preserving the label. Require a safe escalation label at uncertainty
boundaries, then gate aggregate and tagged-slice metrics in CI. For production
thresholds, prefer a pinned model benchmark plus a separate `jev-latest`
canary so model alias movement cannot silently change the release decision.
