# MoA (Mixture of Agents) Skill for OpenClaw

Run multiple LLM reference models in parallel to get diverse perspectives, then let the current agent (aggregator) synthesize the best answer with full tool access.

## Quick Start

```
/moa <question>
/moa balanced <question>
/moa deep <question>
```

## Presets

| Preset | References | Timeout | Best for |
|--------|-----------|---------|----------|
| `default` | sensenova/dsv3-flash ×1 | 60s | Quick single reference |
| `balanced` | dsv3-flash + NVIDIA step-3.7-flash | 90s | Daily work, 2 perspectives |
| `deep` | dsv3-flash + step-3.7 + step-3.5 | 120s | Hard problems, 3 references |

## How It Works

```
User question
  → Node.js executor calls N reference models in parallel
  → Collects all reference outputs + token usage + cost
  → Injects references into user message
  → Current agent (aggregator) responds with full tool access
```

## Features

- **Parallel execution** — All reference models called concurrently (max 8)
- **Context truncation** — Automatically fits conversation within each model's context window
- **Retry logic** — Retries on 429/5xx errors with exponential backoff
- **Concurrency control** — Semaphore limits parallel calls
- **Global timeout** — Configurable per preset (60s/90s/120s)
- **Cost tracking** — Per-model pricing table, NVIDIA models are free
- **12 providers** — OpenAI, Anthropic, DeepSeek, SenseNova, NVIDIA, Google Gemini, OpenRouter, Together, xAI, Moonshot, Agnes, and more
- **Persistent mode** — `/moa on` / `/moa off` for always-on MoA

## Files

| File | Description |
|------|-------------|
| `moa-executor.js` | Node.js engine that calls reference models in parallel |
| `SKILL.md` | Agent instructions for OpenClaw skill system |
| `presets.default.yaml` | Preset configurations (default/balanced/deep) |
| `manifest.json` | Skill metadata |

## Architecture

Reference models receive only the conversation text (no system prompt, no tool schema) — they are **advisors, not actors**. A system prompt frames them as analysts:

> "You are a reference advisor... You do NOT execute anything... A separate aggregator holds those capabilities."

The aggregator (current OpenClaw agent) gets the reference outputs injected at the tail of the user message and responds with full tool access.

## Comparision with Hermes Agent

| Aspect | Hermes Agent | This Skill |
|--------|-------------|-----------|
| Integration | Built into agent loop | Skill layer, loaded on demand |
| Iteration | Every model call | Single-shot (first turn only) |
| Mode | Persistent model provider | Per-command `/moa` |
| Aggregator | Preset-defined model | Current agent's model |

## License

MIT

## References

- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692) (arXiv 2406.04692)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — MoA implementation reference