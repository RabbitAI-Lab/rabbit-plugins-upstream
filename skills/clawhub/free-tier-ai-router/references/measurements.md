# Measurements (probe 2026-07-30 — refresh with `probe.py`)

Every number came from probing **113 models across 5 provider keys** with live
completions — not from docs, not from model names.

| Provider | Models answered a live prompt |
|---|---|
| Mistral | **40 / 42** |
| OpenRouter (free) | **12 / 14** |
| Kilo (free) | **11 / 13** |
| Gemini | **11 / 41** |
| Cerebras | **0 / 3** — account unfunded at probe time, every call 402 |
| **Total** | **74 / 113** |

## Three findings that drive the whole design

**1. Gemini's free tier is 20 requests per DAY, per model.** The 429 body names it:
`limit: 20, metric: generate_content_free_tier_requests`. Verified per-model, not
per-key: `gemini-3.6-flash` was exhausted while `gemini-3.5-flash` still returned 200
on the same key. → Gemini is treated as **scarce**, tried last, budgeted per model.

**2. Mistral publishes exact limits in headers, and they vary 187×.**
From `x-ratelimit-limit-req-minute`:

| Model | req/min | | Model | req/min |
|---|---|---|---|---|
| `ministral-3b-latest` | **750** | | `mistral-large-latest` | **4** |
| `ministral-8b-latest` | 188 | | `magistral-medium-latest` | 5 |
| `codestral-latest` | 125 | | `mistral-small/medium` | 50 |

→ Routine work goes to 750/min models; the 4/min flagship is reserved, not squandered.

**3. A 429 is not a failure — it is a fact worth remembering, and its scope differs.**
Re-probing 21 Gemini 429s after a 45s cooldown recovered **0** — hard daily caps.
Mistral 429s clear in seconds. OpenRouter meters **account-wide**: hitting
`Rate limit exceeded: free-models-per-day` kills every model on that key at once,
so one 429 must sideline the whole provider (observed live after this skill's own
probing exhausted the daily allowance). → Backoff is provider-specific, correctly
scoped (per-model vs per-account), and persisted so the next process inherits it.

## Measured quality (5 objective questions: 91-prime, bat-and-ball, strawberry r's, 9.11 vs 9.9, Canberra)

10 models scored a perfect 5/5. Fastest first:

| Model | Score | Latency |
|---|---|---|
| `mistral/mistral-medium-latest` | 5/5 | 0.43s |
| `gemini/gemini-3.1-flash-lite` | 5/5 | 0.63s |
| `gemini/gemini-3.5-flash-lite` | 5/5 | 0.66s |
| `openrouter/inclusionai/ling-3.0-flash:free` | 5/5 | 0.93s |
| `kilo/kilo-auto/free` | 5/5 | 1.46s |
| `kilo/nvidia/nemotron-3-ultra-550b-a55b:free` | 5/5 | 2.30s |

Two Gemini models scored 0/5 — that was quota exhaustion mid-test, not low quality
(verified separately). A benchmark that can't tell "wrong" from "rate-limited"
produces a poisoned ranking; `quality.py` re-checks every zero.

## Verified behaviour (author sessions, v1.x–v2.3)

| Test | Result |
|---|---|
| 25 distinct prompts back-to-back | **25/25 in 10s, zero 429s** |
| Gemini daily budget after that burst | **0/20 used on all 4 models** |
| Top 3 routes forced into cooldown | transparently fell through to route 4 |
| Repeat prompt | cache hit, ~40 ms, no API call |
| OpenRouter daily quota exhausted | provider parked in one step; 12/12 prompts still served |
| 12 concurrent processes | 12/12 recorded, 0 crashes, 0 leaked counters (v1.2 fix) |
