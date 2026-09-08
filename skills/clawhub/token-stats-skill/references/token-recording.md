# Token Recording Reference

## Public Release And Installation

Use [baijian/token-stats](https://github.com/baijian/token-stats) for public documentation and [release binaries](https://github.com/baijian/token-stats/releases/latest). Verified baseline: v0.0.1 on 2026-09-07. This distribution repository contains no CLI implementation; do not try to build its automatic GitHub source archives. v0.0.1 has no self-update command or built-in scheduler.

Choose `token-stats_<tag>_<os>_<arch>.tar.gz` for `darwin_arm64`, `darwin_amd64`, `linux_amd64`, `linux_arm64`, or `windows_amd64`. Download `checksums.txt` alongside the archive and verify the matching entry before extracting. For macOS Apple Silicon v0.0.1:

```bash
rg '  token-stats_v0.0.1_darwin_arm64.tar.gz$' checksums.txt | shasum -a 256 -c -
tar -xzf token-stats_v0.0.1_darwin_arm64.tar.gz
mkdir -p "$HOME/.local/bin"
install -m 0755 token-stats_v0.0.1_darwin_arm64/token-stats "$HOME/.local/bin/token-stats"
export PATH="$HOME/.local/bin:$PATH"
token-stats version --output json
```

Run extraction only after checksum verification succeeds. On Linux use `sha256sum -c -`; on Windows extract the matching archive and run `token-stats.exe`. Match the archive name and checksum to the selected release and platform. Use an absolute binary path for schedulers when possible.

## CLI Surface

Primary command:

```bash
token-stats usage --agent all --day YYYY-MM-DD --refresh --output json
token-stats report range --agent all --from YYYY-MM-DD --to YYYY-MM-DD --output json
```

Useful flags:

- `--agent codex|claude|openclaw|hermes|opencode|deepseek|all`: select sources. `usage` defaults to `codex`; `report range` defaults to `all`.
- `--day YYYY-MM-DD`: choose a local calendar day; defaults to today.
- `--from YYYY-MM-DD`, `--to YYYY-MM-DD`: inclusive range; defaults to the seven days ending today. Ranges longer than 366 days must be split.
- `--refresh`: rescan local sources and overwrite the selected daily record or every day in a range.
- `--refresh=false`: force a stored-only daily read, including today. Without this flag, today's `usage` auto-refreshes. `report range` never auto-refreshes, even when the range includes today.
- `--data-dir PATH`: override the daily report store.
- `--codex-home PATH`: override `CODEX_HOME` or `~/.codex`.
- `--claude-home PATH`: override `CLAUDE_HOME` or `~/.claude`.
- `--openclaw-home PATH`: override `OPENCLAW_HOME` or `~/.openclaw`.
- `--hermes-home PATH`: override `HERMES_HOME` or `~/.hermes`.
- `--opencode-home PATH`: override `OPENCODE_HOME`, `$XDG_DATA_HOME/opencode`, or `~/.local/share/opencode`.
- `--deepseek-home PATH`: override `DSH_HOME` or `~/.dsh`.
- `--output json`: emit machine-readable data.

Default scanned locations:

- Codex: `~/.codex/sessions` and `~/.codex/archived_sessions`.
- Claude Code: `~/.claude/projects`.
- OpenClaw: `~/.openclaw/agents/*/sessions`.
- Hermes Agent: `~/.hermes/state.db` (SQLite).
- OpenCode: `~/.local/share/opencode/opencode.db` (SQLite).
- DeepSeek Harness: `~/.dsh/sessions/<workspace>/<session>/session.jsonl` or `session.jsonl.zstd`.

Default daily storage:

```text
~/.local/data/cycling-health-cli/token-usage/<agent>/<YYYY-MM-DD>.json
```

The legacy `cycling-health-cli` path is retained for compatibility. Records are namespaced by agent selector. `--agent all` writes to an `all` namespace and keeps per-agent breakdowns inside the JSON. Do not add `all` and individual-agent namespaces together. Daily writes are atomic, files use mode `0600`, and agent directories use mode `0700`.

A historical `usage` read or stored-only `report range` fails when a required daily record is absent; it does not zero-fill or return a partial range. Use `--refresh` for first collection or a rebuild. After upgrading to a version with new collectors, explicitly refresh the relevant historical `all` range to include them. Usage absent from local sources cannot be recovered.

## Scheduling

Use a scheduler to refresh today's report periodically. A 30-60 minute interval is usually enough for historical token analytics.

macOS LaunchAgent:

```bash
./scripts/install-launchd-token-recorder.sh --interval 1800 --agent all --bin "$HOME/.local/bin/token-stats"
```

Manual scheduler command:

```bash
AI_TOKEN_AGENT=all /path/to/token-stats-skill/scripts/record-token-usage.sh
```

Environment variables accepted by `record-token-usage.sh`:

- `TOKEN_STATS_BIN`: command or absolute path for `token-stats`.
- `AI_TOKEN_STATS_BIN`: deprecated compatibility alias used only when
  `TOKEN_STATS_BIN` is unset.
- `AI_TOKEN_AGENT`: any supported selector above; default `all`.
- `AI_TOKEN_DAY`: day to refresh; default today.
- `AI_TOKEN_DATA_DIR`: optional token-usage data directory.
- `AI_TOKEN_CODEX_HOME`: optional Codex home override.
- `AI_TOKEN_CLAUDE_HOME`: optional Claude Code home override.
- `AI_TOKEN_OPENCLAW_HOME`: optional OpenClaw home override.
- `AI_TOKEN_HERMES_HOME`: optional Hermes Agent home override.
- `AI_TOKEN_OPENCODE_HOME`: optional OpenCode data directory override.
- `AI_TOKEN_DEEPSEEK_HOME`: optional DeepSeek Harness home override.
- `AI_TOKEN_RUN_DIR`: optional directory for per-run JSON snapshots.

The daily `token-stats` record is the durable source for historical analysis. Per-run snapshots are useful when the user wants intra-day growth traces or audit logs.

The installer accepts all six `--*-home` flags and persists them for launchd. For compatibility after the skill rename, its defaults retain label `com.baijian.ai-token-ayalysis`, logs under `~/Library/Logs/ai-token-ayalysis`, and snapshots under `~/.local/state/ai-token-ayalysis/runs`. The LaunchAgent PATH includes `~/.local/bin`. Keep snapshots and operational logs private too; the CLI's daily-file permission guarantees do not automatically apply to shell redirects.

This recorder refreshes only the current day. For complete history, backfill missed dates after sleep or downtime and refresh the previous day after midnight when its final events may not have been collected. Repeated snapshots are cumulative daily totals, not additive usage events.

## JSON Fields For Analysis

Common daily and range report fields:

- `schemaVersion`: report schema identifier; the verified release uses `1`.
- `generatedAt`: when the report was produced.
- `agent`: selected agent namespace.
- `cached`: whether the result came from storage.
- `scanned.files`, `scanned.events`, `scanned.skippedLines`: collection coverage.
- `total`: aggregate token buckets.
- `byAgent`: per-agent totals when using `--agent all`.
- `byModel`: per-model totals.
- `byRateLimit`: rate-limit buckets where the source exposes them; not a live account quota.
- `byDay`: daily totals.
- `warnings`: parser or environment warnings to preserve in summaries.

Daily reports add `day`, `storagePath`, and `sessions` with session ID, path, cwd, model, usage, and event count. Range reports add `from`, `to`, `storageDir`, and `days` (daily storage paths, cache status, scans, totals, and warnings); they do not contain `sessions`. Query the relevant daily report to investigate a session.

The `byAgent`, `byModel`, `byRateLimit`, and `byDay` values are arrays of `{key, usage, events}` buckets, not objects keyed by name. Read counters from each bucket's `usage` object.

Token buckets:

- `inputTokens`
- `cachedInputTokens`
- `cacheWriteTokens`
- `outputTokens`
- `reasoningOutputTokens`
- `totalTokens`

## Analysis Guidance

- Always state the date range, agent selector, and data directory used.
- Treat missing JSON files as missing data, not zero usage, unless the user explicitly wants zero-filled charts.
- Prefer `report range` over manually combining daily files. Use `--refresh` on old days for first collection or rebuilds.
- Break down machine-level reports by `byAgent` first, then `byModel`.
- Use `sessions` for root-cause analysis of spikes, but avoid exposing sensitive paths unless needed.
- Include warnings and skipped-line counts when they may affect totals.
- Read `totalTokens` as provided. Cache and reasoning fields may overlap with input and output counters; do not sum every bucket to recompute total consumption. These are local usage counters, not billed amounts or authoritative provider invoices.

## Source Coverage And Attribution

- Only the six named agents have collectors in v0.0.1. Trae, Doubao, Doubao Work, and WorkBuddy are unsupported. Missing sources and parser warnings can make machine-level totals incomplete.
- Hermes delegated-task usage is included from `session_model_usage`; main-session counters are attributed to the session start day, including sessions spanning midnight.
- SQLite sources are read-only. The immutable fallback emits a warning and may omit uncheckpointed WAL updates; disclose this limitation when it affects a report.
- DeepSeek Harness v0 JSONL and concatenated Zstandard logs are supported (verified upstream with `dsh 0.1.1-rc.2`). Final assistant messages replace earlier samples for the same turn/step, chunk-only usage is included, fork-inherited history is excluded, and subagents use `deepseek:subagent` buckets. Each request belongs to its last usage sample's local day.
- DeepSeek input includes uncached input, cache reads, and cache writes; reasoning is already part of output. Unknown session versions produce warnings.
