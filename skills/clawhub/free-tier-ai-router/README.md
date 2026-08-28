# 🎛️ free-tier-ai-router

Quota-aware LLM router that squeezes maximum usable AI out of free-tier API keys
(Mistral, Gemini, OpenRouter, Kilo + pluggable Groq/llm7/HuggingFace/Cerebras/Cohere
and any OpenAI-compatible endpoint, including local Ollama / llama.cpp / vLLM servers).

## Functionality

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

- sha256: e59a7bbbe36f9ec9991845f375aabe4a6b1badb8de809cd325c5fb5cec6e3a53
  (of this release's `SKILL.md` — verify with `sha256sum SKILL.md`)
- Live-verified: groq `openai/gpt-oss-120b` answer through the spec transport;
  a declared local gateway appeared in `--plan`, answered a live call, and
  accepted `--discover --apply`; 8 parallel calls 8/8 recorded with zero leaked
  counters; cache hit returns in ~40 ms with no API call.
