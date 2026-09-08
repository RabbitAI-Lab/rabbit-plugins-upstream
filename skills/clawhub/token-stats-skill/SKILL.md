---
name: token-stats-skill
slug: token-stats-skill
displayName: token-stats-skill
version: 0.0.1
summary: Local token usage collection and historical analysis for Codex, Claude Code, OpenClaw, Hermes Agent, OpenCode, and DeepSeek Harness using token-stats.
license: MIT
description: Record and analyze local token usage from Codex, Claude Code, OpenClaw, Hermes Agent, OpenCode, and DeepSeek Harness with the published token-stats CLI. Use for daily snapshots, historical date-range reports, agent/model/session breakdowns, or periodic local collection with launchd or cron. Reports reflect available local usage counters, not billing charges.
---

# token-stats-skill

Use `token-stats usage` for daily collection and `token-stats report range` for historical analysis. The CLI reads local agent logs and databases and stores normalized daily reports.

Public distribution: [baijian/token-stats](https://github.com/baijian/token-stats).
The release baseline verified on 2026-09-07 is [v0.0.1](https://github.com/baijian/token-stats/releases/tag/v0.0.1). Check [latest release](https://github.com/baijian/token-stats/releases/latest) when installing or updating. This repository distributes binaries and documentation, not CLI source code. The skill directory and invocation name are `token-stats-skill`.

## Principles

- Keep all collection local. Do not upload session logs or token reports unless the user explicitly asks.
- Prefer `token-stats` from `PATH`. If missing, install the matching release archive after checksum verification; see the reference for platform selection. The public repository's automatic source archives do not contain the CLI implementation. v0.0.1 has no self-update command.
- Prefer JSON output for collection and analysis: pass `--output json`.
- Pass `--agent all` for machine-level accounting. Single-agent selectors are `codex`, `claude`, `openclaw`, `hermes`, `opencode`, and `deepseek`; `usage` itself defaults to `codex`.
- Today's `usage` report refreshes automatically unless `--refresh=false` is explicit. Historical `usage` and every `report range` query read stored records unless `--refresh` is supplied. Refresh missing days or a requested rebuild; cached `all` records do not automatically gain newly supported agents.
- Treat `~/.local/data/cycling-health-cli/token-usage/<agent>/<YYYY-MM-DD>.json` as the durable daily record store unless the user sets `--data-dir`.
- Use CLI report fields directly. Do not re-parse raw logs unless debugging the collector. Trae, Doubao, Doubao Work, and WorkBuddy are not supported in v0.0.1; `all` means all supported collectors, not every application on the machine.
- Preserve warnings, skipped-line counts, missing-agent notes, and storage paths in user-facing summaries.

Read [references/token-recording.md](references/token-recording.md) for installation, scheduling, source paths, JSON fields, and attribution limits.

## Workflow

1. Confirm the CLI:
   - Run `token-stats version --output json`.
   - If unavailable, use the public release binaries; do not fabricate token totals.

2. Refresh or read the target day:
   - Today or explicit refresh:
     `token-stats usage --agent all --day YYYY-MM-DD --refresh --output json`
   - Stored historical day:
     `token-stats usage --agent all --day YYYY-MM-DD --output json`
   - Stored inclusive date range:
     `token-stats report range --agent all --from YYYY-MM-DD --to YYYY-MM-DD --output json`
   - Add `--refresh` to a range query to rescan and persist every day in that range. Without dates, the range is the latest seven days, including today.

3. Set up periodic recording when requested:
   - Use `scripts/install-launchd-token-recorder.sh` on macOS. Installing the CLI alone does not create a scheduler.
   - Use `scripts/record-token-usage.sh` as the scheduler command on other systems.
   - Keep the schedule modest, such as every 30-60 minutes, because each run refreshes the current daily report from local logs.

4. Analyze history:
   - Prefer `report range` for multi-day totals; use a daily report for session-level investigation.
   - Use `total.totalTokens` directly, with `inputTokens`, `cachedInputTokens`, `cacheWriteTokens`, `outputTokens`, and `reasoningOutputTokens` as reported breakdowns. Do not add overlapping cache/reasoning fields to the total again.
   - Use `byAgent`, `byModel`, `byDay`, and `byRateLimit` where available. Range reports contain `days` summaries; only daily reports contain `sessions`.
   - Report date range, agent filter, data directory, missing days, and warnings.

## Common Tasks

### Snapshot Now

Run the bundled wrapper when this skill folder is available:

```bash
AI_TOKEN_AGENT=all ./scripts/record-token-usage.sh
```

Or call the CLI directly:

```bash
token-stats usage --agent all --day "$(date +%F)" --refresh --output json
```

The CLI writes or overwrites the durable daily record. The wrapper can also keep per-run snapshots when `AI_TOKEN_RUN_DIR` is set.

### Install A macOS Recorder

Use the bundled installer from the skill directory:

```bash
./scripts/install-launchd-token-recorder.sh --interval 1800 --agent all --bin "$HOME/.local/bin/token-stats"
```

This creates a user LaunchAgent that periodically runs `record-token-usage.sh`, refreshes today's `token-stats` daily record, and writes operational logs under `~/Library/Logs/ai-token-ayalysis`.

### Query Stored History

For one day:

```bash
token-stats usage --agent all --day 2026-07-10 --output json
```

For a stored date range:

```bash
token-stats report range --agent all --from 2026-09-01 --to 2026-09-06 --output json
```

A missing daily record makes the range query fail with refresh guidance; it is not zero usage. Add `--refresh` for a first collection or rebuild, including backfilling newly supported agents. Do not sum the `all` namespace together with individual-agent namespaces, or add repeated per-run snapshots together.

## Resources

- `scripts/record-token-usage.sh`: scheduler-safe wrapper around `token-stats usage`.
- `scripts/install-launchd-token-recorder.sh`: macOS LaunchAgent installer for periodic local recording.
- `references/token-recording.md`: detailed CLI flags, storage layout, scheduling guidance, and analysis notes.
