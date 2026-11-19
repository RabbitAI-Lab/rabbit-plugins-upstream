---
name: evolver
description: Run EvoMap V2 evolution cycles — convert sessions to transcripts, ingest material, distill genes, run cycles, and manage the autoexec daemon. Use when running or debugging EvoMap evolution (evolver >= 2.0.23).
---

# Evolver Skill

Automates the EvoMap V2 evolution cycle within OpenClaw (material-driven flow, evolver >= 2.0.23).

## Quick Start

```bash
# 1. Convert a recent OpenClaw session into a transcript (material)
node skills/evolver/scripts/sessions-to-transcripts.js

# 2. Ingest + distill (no runner needed) or run a full cycle
node skills/evolver/scripts/evolve-cycle.js            # ingest -> cycle
node skills/evolver/scripts/evolve-cycle.js --distill  # ingest -> distill (no runner)

# 3. Manage the autoexec self-learning daemon
node skills/evolver/scripts/autoexec-manage.js status
node skills/evolver/scripts/autoexec-manage.js start
node skills/evolver/scripts/autoexec-manage.js stop

# 4. Verify a GEP prompt was captured
node skills/evolver/scripts/verify-gep.js
```

## V2 Workflow (replaces V1 `evolver run` / `evolver solidify`)

1. **Convert** — `sessions-to-transcripts.js` turns OpenClaw session JSONL into `*.transcript.jsonl` (OpenAI chat-completions shape) in `memory/evolution/`.
2. **Ingest** — `evolve-cycle.js` finds the latest transcript and runs `evolver ingest` to create material with extracted signals.
3. **Distill or Cycle** — `--distill` runs `evolver distill` (no runner required); plain mode runs `evolver cycle --repo` (needs a configured runner).
4. **Review / Publish** — review the cycle output; publishing in V2 requires a Gene + Capsule **pair**.
5. **Daemon** — `autoexec-manage.js` starts/stops the autoexec daemon (config at `~/.evomap/autoexec/config.json`, runner e.g. `gemini`).

## Files

- `scripts/sessions-to-transcripts.js` — Session JSONL → generic-chat transcript converter
- `scripts/evolve-cycle.js` — V2 material-driven cycle runner (`--distill` for no-runner mode)
- `scripts/autoexec-manage.js` — Start/stop/status for the autoexec daemon
- `scripts/verify-gep.js` — Quick GEP prompt verification

## Notes

- V1 commands `evolver run` / `evolver solidify` are **deprecated** in 2.x — use the V2 flow above.
- `evolver solidify` does a `git reset --hard` on failure — commit your work first if you must use it.
- Materials should come from **actual coding work logs**, not QQ chat conversations (chat-derived genes are homogeneous and unproven).
- `evolver cycle` requires a runner (e.g. `gemini`); if the execute queue is disabled, prefer `--distill`.
- The `--loop` daemon historically doesn't work reliably; use `autoexec-manage.js` instead.
