---
name: sith-choir
description: "Cross-model intellect relay across a mesh of stored API keys (multi-provider, multi-key). The conductor farms work out to a choir of models reachable via EVERY stored credential — each provider's api_key and each alt_api_keys entry is its own health-tracked voice with automatic per-key failover — and models that need help are answered using other providers' keys (e.g. a Mistral-key model that is rate-limited or unsure consults Gemini and llm7.io keys). Core moves: (1) weak/cheap models sing candidates in parallel and a reasoning model aggregates them (Mixture-of-Agents, arXiv:2406.04692); (2) vision relay — text-only callers hand images to vision-capable voices (arXiv:2502.16428); (3) mandatory escalation — low confidence, errors or rate limits route to a reasoning court from other providers (FrugalGPT cascade, arXiv:2305.05176); (4) judge panels score 0-10 and a persistent reward ledger punishes weak voices while key-health cooldowns rotate load (arXiv:2306.05685). Plus self-consistency voting (`consensus`, weighted plurality with abstention, arXiv:2203.11171 + 2502.06233), an independent adversarial `verify` round, a verifier revision loop (`refine`, Reflexion arXiv:2303.11366), calibration-driven self-improvement (`calibrate`), multi-turn memory (`--session`), exact-question answer caching, provider cache-read token accounting + `--budget`, provenance `runs`/`report` with latency, task `--lane` routing, `--plan` dry-run, machine-readable `--json` everywhere, and offline `selftest`. Use when you hold many API keys and want every one contributing, or when one model cannot do the whole job alone."
version: 1.3.0
id: "a9e6f0c2-4b71-4f0e-9c3d-sithchoir0001"
license: MIT
dependencies:
  - "python>=3.9"
host_compatibility: [Claude, ChatGPT, Gemini, Groq, Qwen, Kimi, Mistral, Llama]
categories: [agents, development, research]
topics: [multi-agent, delegation, vision-relay, escalation, llm-judge, self-improvement]
invariants: [hash_integrity, offline_selftest, state_perms_0600, no_key_leakage]
metadata:
  openclaw:
    emoji: "🦞"
    requires:
      bins: ["python3"]
    network:
      outbound: ["*.openai.com", "generativelanguage.googleapis.com", "openrouter.ai", "api.groq.com", "api.mistral.ai", "api.cohere.com", "router.huggingface.co", "api.z.ai", "api.llm7.io", "api.cerebras.io", "api.x.ai", "api.moonshot.ai"]
    configPaths: ["~/.config/sith-choir/credentials.json", "~/.cache/sith-choir/"]
---

# 🦞 sith-choir — Cross-Model Intellect Relay (all keys join the choir)

Let the choir sing; let the Sith listen. This skill turns one conductor agent
into an orchestrator of a *choir* of other models: it farms questions out to
the cheapest/weakest models, drains the best intelligence from the strongest
reasoners, relays vision work to models that can actually see, judges every
answer with a panel, keeps a reward ledger that punishes weak singers, and —
v1.3 — **verifies** final answers, **calibrates** voices against a frozen
question set so routing weights self-improve, tracks **cache-read tokens** and
**latency** per voice, and speaks strict **machine-readable JSON** to any host.

The choir is a **mesh, not a single key**: every stored credential — each
provider's `api_key` *and* every `alt_api_keys` entry — becomes its own voice.
Voices carry per-key health cooldowns and automatic failover, so a request that
starts on one provider's key can be served by, or ask help from, the keys of
other providers. A model behind a rate-limited or exhausted Mistral key can be
answered by a court of Gemini keys and llm7.io keys.

## When to use
- You hold many provider API keys across providers (e.g. a 55-key workspace)
  and want every one contributing instead of one lucky model.
- One provider's key is rate-limited or exhausted — the choir fails over to
  that provider's other keys and asks other providers' keys for help.
- A text-only model is handed an image — it must ask a vision-capable model
  to do the job (`vision`).
- A model is error-prone, low-confidence, or rate-limited — policy says it MUST
  escalate to the best reasoning models from other providers (`escalate`).
- You want answers judged by other models, good/bad performers tracked
  (`judge` + `harvest` + `ledger`), answers double-checked by an independent
  verifier (`verify`), voices scored on a frozen question set so routing
  self-improves (`calibrate`), repeated questions served from cache, and
  multi-turn conversation remembered (`--session`).

## Quick start
```bash
# In an arena.ai workspace with the repo's secrets store:
python3 scripts/choir.py fleet --use-workspace        # every key + health + latency
python3 scripts/choir.py list --use-workspace         # provider voices + ledger
python3 scripts/choir.py moa "explain the CAP theorem" --use-workspace
python3 scripts/choir.py consensus "0.2 vs 1/8?" --use-workspace   # weighted vote
python3 scripts/choir.py verify --question "0.2 vs 1/8?" \
    --answer "@answer.txt" --use-workspace            # adversarial PASS/FAIL check
python3 scripts/choir.py refine "prove sqrt(2) irrational" --use-workspace
python3 scripts/choir.py ask "9*8?" --verify --use-workspace   # answer + verifier
python3 scripts/choir.py calibrate --questions 4 --use-workspace  # self-improve
python3 scripts/choir.py vision --image screenshot.png \
    --question "what is on this screen?" --use-workspace --synthesize
python3 scripts/choir.py escalate "solve this" --use-workspace \
    --from mistral/mistral-small-latest --helpmates gemini,llm7
python3 scripts/choir.py ask "remember: pet=cat" --session me --use-workspace
python3 scripts/choir.py report --use-workspace      # tokens, cache-reads, tok/s
```

Anywhere else, point at your own credentials file:
```bash
python3 scripts/choir.py list --credentials ~/.config/sith-choir/credentials.json
```
Credentials JSON: `{"providers":{"gemini":{"api_key":"..."}, ...}}`. Optional
per provider: `base`, `kind` (`openai`|`gemini`), `model`, `tags`. Add
`"alt_api_keys": ["k2", ...]` for additional accounts — every distinct key is
its own voice.

## Commands
| Command | What it does | Based on |
|---|---|---|
| `fleet` | Every stored API key (`provider#k<idx>`), health, cooldowns, tokens, latency | — |
| `list` | Provider voices + reward ledger | — |
| `ask "Q" [--from prov/model[#k]] [--lane X] [--verify]` | Single direct answer, per-key failover, exact-question cache, optional adversarial verifier | — |
| `moa "Q" [--proposers N] [--aggregator prov]` | Parallel weak/cheap proposals, strong aggregator merges (inputs trimmed to cut tokens/TTFT) | MoA 2406.04692 |
| `consensus "Q" [--samples N]` | Weighted plurality vote; honest `UNKNOWN` abstains; near-ties arbitrated by a reasoning voice | Self-consistency 2203.11171 / CISC 2502.06233 |
| `refine "Q" [--rounds N] [--target X] [--helpmates p]` | Propose→judge→critique→revise verifier loop until target | Reflexion 2303.11366 / 2408.03314 |
| `verify --question Q --answer X` | Independent adversarial PASS/FAIL/PARTIAL round (2 voices) | verifier loops 2505.24726 / 2603.05863 |
| `calibrate [--questions N] [--providers p,...]` | Score voices on frozen questions → calibration.json drives voting weights | self-eval / online eval |
| `vision --image F --question Q [--synthesize]` | Text-only caller relays image to vision voices; optional fusion | 2502.16428 |
| `escalate "Q" [--from ...] [--force] [--helpmates p,q]` | Low confidence/error/rate-limit → mandatory court from other providers | FrugalGPT 2305.05176 |
| `judge --question Q --answer @file [--members ...]` | 0-10 panel; reward ≥7.5 / punish ≤4; author's provider excluded | LLM-as-Judge 2306.05685 |
| `harvest "Q"` | propose → aggregate → judge → ledger in one move | MoA + judge |
| `sessions [--name X --reset]` | List / reset multi-turn memory sessions | — |
| `runs [--last N]` | Provenance: commands, voices, verdicts, tokens, latency | — |
| `report` | Tokens, cache-read tokens, calls, tok/s, calibration accuracy per voice | — |
| `ledger [--reset]` | Persistent reward/punishment history per member | — |
| `selftest` | Offline test suite (sandboxed, no network, no state); exit 0 or 3 | — |

### Cross-cutting flags (any command)
- `--session <name>` — bounded, **compacted** multi-turn memory (context is
  budget-capped per turn so long sessions stay cheap; stored after the run).
- `--no-cache` — bypass the exact-question answer cache (sha256 keys, hits are
  labelled `(cached)` and cost zero tokens).
- `--budget <tokens>` — stop before later stages once *freshly-processed*
  tokens (output + non-cached input) exceed the budget. Cache-read tokens are
  excluded, so repeat session prefixes do not eat the budget.
- `--lane general|fast|reasoning|longctx|code` (`ask`) — route by capability.
- `--plan` — print the exact voices each stage would use, then exit without
  calling any API (also available as `--json --plan` for machines).
- `--json` — machine-readable JSON on **every** command (single document).
  Human banner text never pollutes JSON stdout.
- `--verify` (`ask`, `moa`) — after a fresh answer, run one independent
  adversarial verifier round and report its verdict.

### Exit-code contract (for host agents)
| code | meaning |
|---|---|
| 0 | success (selftest passed, answer produced) |
| 1 | runtime/logic error (message on stderr) |
| 2 | usage / argument error |
| 3 | selftest/invariant failure — do not trust the skill until fixed |

`python3 scripts/choir.py selftest` (or `scripts/selftest.sh`) is the host
readiness gate: 0 = all invariants pass, 3 = something failed. Run it offline
before trusting the skill in a new environment.

## Token & latency discipline (v1.3)
- **Cache-read awareness**: usage is parsed per provider shape (OpenAI
  `prompt_tokens_details.cached_tokens`, Gemini `cachedContentTokenCount`,
  Anthropic `cache_read_input_tokens`) and shown as `cached=` in `report`.
  Request layout keeps the static system prompt byte-identical across calls so
  providers' automatic prompt caching hits; `--budget` and token totals count
  freshly-processed tokens only.
- **Per-stage output caps**: judges/verifiers/voters get tight max_tokens;
  proposal/report bodies are trimmed before aggregation; session context is
  budget-bounded. This cuts both tokens and time-to-first-token.
- **Concurrency**: proposals, judge panels and verifier rounds run in parallel
  across providers. `report` shows measured `tok/s` and `avg ms` per voice.

## Hallucination controls (v1.3)
- **Honest abstention**: proposers/voters are instructed to answer `UNKNOWN`
  rather than guess; `consensus` drops abstentions and never asserts a guess.
- **Independent verifier** (`verify`, or `ask --verify`): two reasoning voices
  grade the final answer `PASS/FAIL/PARTIAL`; any `FAIL` wins (conservative).
- **Arbitration only on agreement**: near-tie consensus results are broken by
  a reasoning arbiter *only if* it explicitly picks one of the tied groups.
- **Fact-pinning**: system prompts forbid invented citations/numbers and tell
  aggregators to attribute disputed claims to the candidate that made them.

## Self-improvement (v1.3)
- `calibrate` scores one voice per provider against a frozen 8-question set
  (facts/arithmetic/code, few-words answers). Accuracy is accumulated in
  `state/calibration.json` (chmod 600) across runs.
- `consensus` vote weights and `report` win-rates read calibration accuracy
  (clamped) before falling back to the reward-ledger EWMA. Run it periodically
  or after provider/model changes; watch the cost with `calibrate --plan`.

## Permissions
- **Reads** the credentials file you point at (`--credentials`, or
  `--use-workspace`). Keys are read in memory only.
- **Writes** state under `~/.cache/sith-choir/` — every file is created with
  mode 0600 atomically (no world-readable window) and never contains API keys:
  `ledger.json`, `fleet.json`, `cache.json`, `sessions/*.json` (only when you
  use `--session`), `runs.jsonl`, `calibration.json`.
- **Network**: outbound HTTPS to the configured model providers only
  (`generativelanguage.googleapis.com`, `openrouter.ai`, `api.groq.com`,
  `api.mistral.ai`, `api.cohere.com`, `router.huggingface.co`, `api.z.ai`,
  `api.llm7.io`, `api.openai.com`, `api.anthropic.com`, `api.x.ai`,
  `api.cerebras.io`, `api.moonshot.ai`), plus any `base` you add.
- `selftest` never touches the network or real user state.

## Security & Privacy
- **API keys are never printed, logged, or written to disk**; only the provider
  endpoints receive them, over HTTPS, in the standard Authorization /
  X-goog-api-key headers.
- The reward ledger, key-health store, provenance runs and calibration store
  only provider/model names, `k<idx>` labels, scores, verdicts, token counts
  and accuracy — never prompts or answers.
- The **answer cache** and **session transcripts** DO store answer text and
  your questions (that is their function) inside the state dir under
  `~/.cache/sith-choir/`, chmod 600. Do not point the skill at secrets you
  must not persist; `--no-cache` and not using `--session` avoids storing
  anything beyond counters.
- Your questions and answers are sent to the third-party providers you
  configure — that is the point of the skill; do not route secrets through it.
- Credentials file should be `chmod 600`; the skill never edits it.
- Review this skill's code before installing, as with any skill that makes
  outbound calls. Behavioral guardrails: hard timeouts, one 429 backoff,
  bounded per-call key failover, per-key cooldowns, `--budget`, `--plan`,
  clear error reporting, honest abstention, never a silent fabricated answer.
- The scanner may describe this skill as a "router/network tool with
  credential access" — that is its honest function, disclosed here.

## Verification hash
SHA-256 of `SKILL.md` (see README for the authoritative block):

```
see README.md "Verification hash"
```
