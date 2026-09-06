---
name: free-tier-ai-router
description: Quota-aware LLM router that squeezes maximum usable AI out of free-tier API keys across Gemini, Mistral, OpenRouter, Kilo and Cerebras plus any OpenAI-compatible endpoint (including local Ollama/llama.cpp/vLLM). Probes every model on every key, measures real quality and real published rate limits, then routes each request to the cheapest model that can do the job — spending abundant capacity first and reserving scarce daily quota for when it is actually needed. Persists cooldowns to disk so a 429 discovered in one process is respected by the next. Use when an agent must make many LLM calls on free keys without hitting rate limits, when "all models failed", or when deciding which of several provider keys to use for a task.
version: 2.4.0
metadata: {"openclaw":{"emoji":"🎛️","requires":{"bins":["curl","python3"]},"configPaths":["~/.config/gemini/credentials.json","~/.config/mistral/credentials.json","~/.config/openrouter/credentials.json","~/.config/kilo/credentials.json","~/.cache/ai_router/state.json"],"network":{"outbound":["generativelanguage.googleapis.com","api.mistral.ai","openrouter.ai","api.kilo.ai","api.cerebras.ai"]}}}
categories: [development, agents, productivity]
topics: [llm-routing, free-tier, rate-limits, openai-compatible, providers]
---

# 🎛️ free-tier-ai-router

**Get the most AI out of free keys, without hitting limits.** Routes *before* failure
using measured quota budgets; a 429 is remembered with the right scope (per-model vs
account-wide) and respected by the next process. Complements `model-fallback` (reacts
after failure) and `local-llm-router` (local machines).

Deep background: [`references/measurements.md`](references/measurements.md) ·
full audit history (25+ fixed bugs): [`references/history.md`](references/history.md) ·
pluggable providers guide: [`references/providers.md`](references/providers.md).

## Quick start

```bash
npx --yes clawhub@latest install free-tier-ai-router
bash skills/free-tier-ai-router/install.sh <your-api-key>   # or integrate.sh for zero API calls
ai "your question"                                          # entry point created by install
```

One self-contained alternative (payload checksum-verified inside the script):

```bash
bash get-ai-router.sh <your-api-key> && ai "your question"
```

No key yet? Any one free tier works — Mistral has the most generous limits:
[Mistral](https://console.mistral.ai/api-keys) · [Gemini](https://aistudio.google.com/apikey) ·
[OpenRouter](https://openrouter.ai/keys) · [Kilo](https://app.kilo.ai/profile).
`ai --doctor` diagnoses any setup problem.

## Usage (portable paths)

```bash
R=skills/free-tier-ai-router/router.py     # from the install directory (or use `ai`)

python3 $R "explain X in one line"          # general: cheapest abundant model
python3 $R -t code "write a python retry decorator"
python3 $R -t fast "yes or no: is 17 prime"
python3 $R -t best -q 5 "audit this argument"
python3 $R "long answer" --stream           # v2.4.0: live SSE streaming (faster first token)
python3 $R --learn                          # v2.4.0: learned-reliability report
python3 $R --status                         # live budget per route
python3 $R --plan -t code                   # routing order, zero calls
python3 $R --discover [--apply]             # list/add models from configured providers
python3 $R --setup <key>                    # install+verify a key (auto-detects provider)
python3 $R --reset                          # clear cooldowns
```

- `-q N` — only use models that **measured** ≥N/5 · `--no-cache` — skip the SHA-256
  response cache (repeat prompts return in ~40 ms with zero API calls)
- `--no-learn` — one call without updating the learning overlay · `--learn-reset` — clear it

## How it decides

```
task=general → cheap tier, highest rpm×reliability first   (spend abundance)
task=fast    → cheap tier, learned EWMA latency first
task=code    → code-tagged models first · task=best → highest measured quality
   ↓ skip anything in cooldown / over daily budget / known-dead (health.json)
   ↓ call → success: bank it, update EWMA (bounded reordering, never disables)
   ↓        429: provider-correct cooldown (gemini parked for the day · mistral 60-300s
   ↓        · openrouter account-wide until midnight · 402/404 24h) — persisted with flock
   ↓ persist state atomically → the next process inherits the knowledge
```

Scarce capacity (Gemini 20/day/model) keeps a 20% reserve — only `-q5`/`-t best` may
spend it. Gemini is tried last in general mode.

## Machine contract

`--json` on ask/status/plan/learn emits schema-versioned objects —
[`schema/`](schema/) holds JSON Schemas (`ai_router.answer.v1`, `.status.v1`,
`.plan.v1`, `.learn.v1`, plus `providers.config.schema.json` for the config file).
Exit codes: **0** ok · **2** all routes quota-dead · **3** no keys configured ·
**4** invalid providers.json. `--stream` and `--json` are mutually exclusive.

## Self-improvement (v2.4.0)

Every call updates `~/.cache/ai_router/learn.json` (EWMA latency, ok/429/fail counts,
14-day decay, flock-safe). Ordering inside a tier gets a reliability multiplier
clamped to [0.5, 1.2] — neutral until 5 observations, never disables a route,
cooldowns stay authoritative. Zero API cost. `--learn` reports, `--learn-reset` clears.

## Safety, limits, honesty

- Keys never appear in `ps` (headers via 0600 temp file, `-H @file`); prompts travel
  via stdin (argv injection impossible). Credentials files chmod 600.
- Writes only under `~/.cache/ai_router/` and `~/.config/`. No telemetry.
- `integrate.sh` self-heals stale installs (sha256-audited against the bundled blob)
  — belt-and-braces for any registry lag; the registry freeze observed during
  v1.x–v2.1 was resolved by 2026-09 (installs deliver current code).
- Provider state notes (Cerebras unfunded, Kilo free-only) are as-of the
  2026-07-30 probe — re-run `probe.py` to refresh. Router does not stream for the
  gemini transport (falls back to a normal call). Quality scores = 5 objective
  questions: good at catching reasoning failures, not a full benchmark.

## Testing

`bash scripts/selftest.sh` — 12-stage suite against a local mock provider
(zero API cost, throwaway HOME): answer/cache/429-cooldown/402-park/persistence/
plan-offline/stream/exit-codes/learn — must print `ALL PASS`.
