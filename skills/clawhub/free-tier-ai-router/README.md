# 🎛️ free-tier-ai-router

Quota-aware LLM router that squeezes maximum usable AI out of free-tier API keys
(Mistral, Gemini, OpenRouter, Kilo + pluggable Groq/llm7/HuggingFace/Cerebras/Cohere
and any OpenAI-compatible endpoint, including local Ollama / llama.cpp / vLLM servers).

## Functionality (v2.4.0 additions in bold)

- **`--stream`: live SSE passthrough** on the same security path (headers via 0600
  file, payload via stdin) — first token reaches you as soon as the model emits it;
  non-SSE servers degrade gracefully; gemini transport falls back to a normal call.
- **`--learn` self-improvement**: every call records EWMA latency + ok/429/fail per
  route (flock-safe, 14-day decay); ordering inside a tier gets a reliability
  multiplier clamped to [0.5, 1.2] — neutral until 5 observations, never disables a
  route, cooldowns stay authoritative. `--learn` reports, `--learn-reset` clears,
  `--no-learn` opts out per call.
- **Shipped JSON Schemas** (schema/): answer.v1, status.v1, plan.v1, learn.v1 and
  providers.config.schema.json — agents can validate every machine output.
- **Sandboxed selftest** (scripts/selftest.sh + mock_provider.py): 12 stages, zero
  API cost, throwaway HOME — answer/cache/429-cooldown/402-park/cross-process
  persistence/plan-offline/streaming/exit-codes/learn.
- **Progressive-disclosure docs**: SKILL.md is now a lean ~120-line orchestrator;
  deep content lives in references/ (measurements, 27-bug history, providers guide)
  — ~75% fewer always-loaded tokens for consuming agents.
- **Fixes #26–#27**: --discover --apply hot-reload actually reloads now; spec-only
  setups (local gateways) exit 2 instead of 3 on exhaustion.

- Routes each request to the cheapest model that can do the job, spending abundant
  capacity first and reserving scarce daily quota (e.g. Gemini's 20 req/day/model)
  for when it is actually needed.
- Provider-correct cooldowns persisted to disk (`flock`-safe): a 429 discovered in
  one process is respected by the next; account-wide daily caps park the whole
  provider until midnight; per-model caps park one route.
- `providers.json` plugins: declare ANY OpenAI-compatible endpoint (base_url,
  auth bearer|x-api-key|none, models with quality/rpm/rpd/tier) — user entries
  override built-in routes. Local servers need no key at all.
- `--discover [--apply]`: reads `GET /models` from configured providers and adds
  routes (never auto-applied; handles 401/403 listings and odd JSON shapes).
- `--json` machine contract (`ai_router.answer.v1` / `.status.v1` / `.plan.v1`)
  and stable exit codes (0 ok · 2 quota-dead · 3 no keys · 4 invalid config).
- SHA-256 response cache (~40 ms repeat answers, zero API calls), dead-route
  seeding (0 wasted calls relearning known-dead routes), `--setup` with
  verify-before-overwrite and key auto-detection, `--doctor` diagnostics.

## Permissions

- Reads `~/.config/<provider>/credentials.json` (chmod 600 enforced on write) and
  `~/.config/ai_router/providers.json` (chmod 600 enforced when it carries inline keys).
- Writes only under `~/.cache/ai_router/` (state + cache) and `~/.config/`.
- Outbound HTTPS to the configured providers' APIs only; discovery adds one GET
  per provider. No telemetry, no third-party reporting.

## Security & Privacy

- API keys never appear in `ps` output: all headers travel via a `0600` temp file
  passed as `curl -H @file`, deleted immediately.
- Prompts are JSON-encoded and piped via stdin — injection into `curl` argv is
  structurally impossible.
- A malformed `providers.json` is a warning, never a crash; `--json` answers
  surface it with exit code 4.
- `auth: "none"` on a non-local base_url prints a loud warning (unauthenticated
  network path).

## Verification

- sha256: e4c17297cfaba96871d791fb2f138f4a7fc93af32ee65d69978085ecc8dcc45a
  (of this release's `SKILL.md` — verify with `sha256sum SKILL.md`)
- Live-verified: groq `openai/gpt-oss-120b` answer through the spec transport;
  a declared local gateway appeared in `--plan`, answered a live call, and
  accepted `--discover --apply`; 8 parallel calls 8/8 recorded with zero leaked
  counters; cache hit returns in ~40 ms with no API call.
