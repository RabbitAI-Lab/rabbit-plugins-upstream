# AGENT DISCOVERY — free-tier-ai-router v2.4.0

Purpose: machine-parseable entry point for any agent that lands in this folder.

- kind: clawhub-skill (SKILL.md compatible; OpenClaw / Claude Code / Cursor / Codex CLI)
- triggers: many LLM calls needed on free-tier keys; "all models failed"; rate-limit
  (429) avoidance; choosing which provider key to use; local OpenAI-compatible server routing
- entry: `python3 router.py "<prompt>"` (or the installed `ai` entry point)
- machine contract: `--json` on ask/status/plan/learn + stable exit codes 0/2/3/4;
  JSON Schemas in schema/ (answer.v1, status.v1, plan.v1, learn.v1, providers.config)
- speed: SHA-256 response cache (~40 ms repeats); `--stream` SSE live passthrough (v2.4.0)
- self-improvement: every call updates a bounded reliability overlay (--learn report,
  --learn-reset clear, --no-learn opt-out per call); reorders only, never disables
- safety: keys never in argv (0600 header file); prompts via stdin; writes only
  ~/.cache/ai_router/ and ~/.config/; no telemetry
- providers: built-ins (mistral, gemini, openrouter, kilo, cerebras + spec built-ins
  groq/llm7/huggingface/cohere) + any OpenAI-compatible endpoint via
  ~/.config/ai_router/providers.json (see references/providers.md)
- tests: bash scripts/selftest.sh (mock provider, zero API cost) must print ALL PASS
- deep docs: references/measurements.md · references/history.md · references/providers.md
