# 🦞 sith-choir — Cross-Model Intellect Relay (all keys join the choir)

One conductor model delegates work across a **mesh** of every model reachable
via your stored API keys — each provider's `api_key` plus each `alt_api_keys`
account becomes its own health-tracked voice — then harvests the best
intelligence back. Weak/cheap models sing candidate answers in parallel; a
strong reasoning model aggregates (Mixture-of-Agents); vision work goes to
models that can actually see; models that make mistakes, run dry, or get
rate-limited are *required* to escalate to the best reasoners **from other
providers' keys**; and every answer is judged by a panel that rewards the
strong and punishes the weak in a persistent ledger.

**v1.3** adds: independent adversarial **`verify`** (hallucination guard),
self-improving **`calibrate`** (voices scored on a frozen question set, feeding
vote/routing weights), honest **abstention** in consensus voting with
near-tie arbitration, **provider cache-read token accounting** + per-stage
output caps + trimmed aggregation inputs (token & latency cuts), measured
**tok/s and latency per voice**, budget-bounded **session compaction**, strict
machine-readable **`--json`** on every command, an **exit-code contract** for
host agents, and atomic 0600 state writes.

> The choir is multi-key and multi-provider by design: if a model behind an
> **openrouter or mistral key** needs help, the skill answers it using the
> **gemini or llm7.io keys** — and vice versa. Example:
> `escalate "…" --from mistral/mistral-small-latest --helpmates gemini,llm7`
> answers through a court made of Gemini + llm7 (+ other reasoning) keys when
> Mistral is unsure or rate-limited.

## Functionality

### 0. The mesh: every API key is a voice (`fleet`, per-key failover)
- `fleet` shows every stored key (`provider#k<idx>`), health (`ok`/`cool`),
  cooldowns, token spend, cached-token spend, average latency and call counts.
  A key that 429s, errors, or is exhausted is cooled per-key and the
  provider's other keys take over automatically.
- `list` shows one voice per provider plus the reward ledger.

### 1. The choir proposes, the Sith aggregates (`moa`)
- N voices (fast lane, one per provider) answer the same question in parallel.
- A reasoning voice synthesizes the single best final answer (MoA,
  arXiv:2406.04692). Candidate bodies are trimmed before aggregation so the
  prefill — and therefore time-to-first-token and input tokens — stays small.

### 2. Self-consistency voting with abstention (`consensus`)
- Several voices answer and end with `ANSWER: <concise>`; votes are chosen by
  weighted plurality (arXiv:2203.11171 + confidence-weighted 2502.06233).
- Voices that honestly answer `ANSWER: UNKNOWN` **abstain** and are never
  voted into a plurality; a near-tie between the top two groups is broken by a
  reasoning **arbiter only if it explicitly picks one of the tied groups**.

### 3. Independent adversarial verifier (`verify`, `ask --verify`)
- Two reasoning voices check a final answer and reply `VERDICT:
  PASS | FAIL | PARTIAL`; any FAIL wins (conservative), PARTIAL otherwise.
- Verifier loop = Reflexion-style test-time compute (arXiv:2303.11366,
  2505.24726, 2603.05863). `ask --verify` runs the round automatically on
  fresh (uncached) answers; `refine` remains the full judge→critique→revise
  loop.

### 4. Verifier / revision loop (`refine`)
- Draft (via `moa`) → judge panel → below `--target` (default 7.5)? a revisor
  rewrites against the judges' critiques, re-judged up to `--rounds` times.
  The ledger updates from the final panel only; `--budget` bounds the loop.

### 5. Vision relay (`vision`)
- Text-only callers hand the image to **vision-capable** voices
  (Qwen3-VL / GLM-4.5V / Gemini / Kimi / Pixtral / Claude / GPT-vision
  classes) and get textual reports; optional `--synthesize` fuses them.

### 6. Mandatory escalation across providers (`escalate`)
- Primary answers with `CONF: <0.0-1.0>`; confidence < 0.7, `--force`, or an
  error/rate-limit triggers a **reasoning court from other providers**
  (`--helpmates gemini,llm7` forces those keys in). Lead reasoner merges
  (FrugalGPT cascade, arXiv:2305.05176).

### 7. Judge panel rewards & punishments (`judge`, `harvest`)
- Independent judges score 0-10 (anti-bias instructions; the answer's own
  provider never grades itself). REWARD ≥7.5 / NEUTRAL / PUNISH ≤4 → ledger.

### 8. Self-improvement (`calibrate`)
- One voice per provider answers a frozen 8-question set (facts/arithmetic/
  code, few-words answers; default 3 questions, `--questions N` up to 8).
- Per-voice accuracy accumulates in `state/calibration.json` (0600).
  `consensus` vote weights and `report` accuracy columns consume it
  (clamped [0.2, 3.0]) before falling back to the reward-ledger EWMA.
- See the cost first: `calibrate --plan`.

### 9. Multi-turn memory (`--session`)
- `--session <name>` injects prior context and stores the exchange. Context is
  **budget-compacted** (newest turns keep detail, older turns truncate) so a
  long conversation does not balloon per-turn tokens.

### 10. Cache, budgets, provenance, machine output
- `ask` serves identical repeats from `state/cache.json` (sha256, `(cached)`,
  zero tokens). `--no-cache` bypasses.
- **Cache-read accounting**: usage parsed per provider shape (OpenAI
  `cached_tokens`, Gemini `cachedContentTokenCount`, Anthropic
  `cache_read_input_tokens`); `report` shows `cached=` and `tok/s`. The system
  prompt stays byte-stable so provider prompt caches can hit. `--budget N`
  counts output + non-cached input only.
- `runs` lists provenance with latency (never your content); `report`
  aggregates tokens, cached tokens, calls, tok/s, and calibration accuracy per
  voice.
- `--plan` prints the exact voices (JSON too). `--json` is single-document on
  every command. Exit codes: 0 ok · 1 runtime error · 2 usage · 3 selftest/
  invariant failure (`selftest` returns 3 on failure).

## Quick start
```bash
# workspace (reads repo secrets + model catalog automatically)
python3 scripts/choir.py fleet --use-workspace
python3 scripts/choir.py moa "explain supervised vs RL fine-tuning" --use-workspace
python3 scripts/choir.py consensus "0.2 vs 1/8?" --use-workspace
python3 scripts/choir.py verify --question "0.2 vs 1/8?" --answer "@a.txt" --use-workspace
python3 scripts/choir.py ask "9*8?" --verify --use-workspace
python3 scripts/choir.py calibrate --questions 4 --use-workspace
python3 scripts/choir.py escalate "…" \
    --from mistral/mistral-small-latest --helpmates gemini,llm7 --use-workspace
python3 scripts/choir.py ask "remember pet=cat" --session me --use-workspace
python3 scripts/choir.py report --use-workspace
python3 scripts/choir.py selftest          # host readiness gate (exit 0/3)

# anywhere (bring your own credentials, incl. alt_api_keys for multi-key)
python3 scripts/choir.py list --credentials ~/.config/sith-choir/credentials.json
```

## Permissions
- **Reads** the credentials file you point at (`--credentials`, or
  `--use-workspace`). Keys are read in memory only.
- **Writes** state under `~/.cache/sith-choir/` — every file is created with
  mode 0600 atomically (no world-readable window): `ledger.json` (scores),
  `fleet.json` (per-key health, cooldowns, tokens, latency), `cache.json`
  (answer cache), `sessions/*.json` (only when you use `--session`),
  `runs.jsonl` (provenance labels + verdicts + tokens + latency — never your
  prompts or answers), `calibration.json` (per-voice accuracy).
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
  your questions (that is their function) inside the state dir, chmod 600,
  under `~/.cache/sith-choir/` only. Do not point the skill at secrets you
  must not persist; `--no-cache` and not using `--session` avoids storing
  anything beyond counters.
- Your questions and answers are sent to the third-party providers you
  configure — that is the point of the skill; do not route secrets through it.
- Credentials file should be `chmod 600`; the skill never edits it.
- Review this skill's code before installing, as with any skill that makes
  outbound calls. Behavioral guardrails: hard timeouts, one 429 backoff,
  bounded per-call key failover, per-key cooldowns, `--budget`, `--plan`,
  honest abstention, clear error reporting, never a silent fabricated answer.
- The scanner may describe this skill as a "router/network tool with
  credential access" — that is its honest function, disclosed here.

## Verification hash
SHA-256 of `SKILL.md`:

```
6c92633cb50bd41c0f75b3cbf79fac639b766b3b62d86df7615b28adac647cd6
```

Check with: `sha256sum SKILL.md` (must equal the line above).

## Design & research
Full citations and the company capability survey: `references/design.md`.
Multi-key failover mirrors `tools/router.py` (per-key cooldowns, health
rotation) — see MULTI_API_KEYS_PER_PROVIDER in that repo.
