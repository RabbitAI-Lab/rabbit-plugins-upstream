# Token Recording Reference

## Public Release And Installation

Use [baijian/token-stats](https://github.com/baijian/token-stats) for public documentation and [release binaries](https://github.com/baijian/token-stats/releases/latest). Verified baseline: v0.0.2 on 2026-09-09, binary commit `c17d30954d39`. This distribution repository contains no CLI implementation; do not try to build its automatic GitHub source archives. v0.0.2 has no self-update command or built-in scheduler. Its release notes and binary help supersede the stale v0.0.1 coverage in the public README.

Choose `token-stats_<tag>_<os>_<arch>.tar.gz` for `darwin_arm64`, `darwin_amd64`, `linux_amd64`, `linux_arm64`, or `windows_amd64`. Download `checksums.txt` alongside the archive and verify the matching entry before extracting. For macOS Apple Silicon v0.0.2:

```bash
rg '  token-stats_v0.0.2_darwin_arm64.tar.gz$' checksums.txt | shasum -a 256 -c -
tar -xzf token-stats_v0.0.2_darwin_arm64.tar.gz
mkdir -p "$HOME/.local/bin"
install -m 0755 token-stats_v0.0.2_darwin_arm64/token-stats "$HOME/.local/bin/token-stats"
export PATH="$HOME/.local/bin:$PATH"
token-stats version --output json
```

Run extraction only after checksum verification succeeds. On Linux use `sha256sum -c -`; on Windows extract the matching archive and run `token-stats.exe`. Match the archive name and checksum to the selected release and platform. Use an absolute binary path for schedulers when possible.

## CLI Surface

Primary commands:

```bash
token-stats sources --output json
token-stats usage --agent all --day YYYY-MM-DD --refresh --output json
token-stats report range --agent all --from YYYY-MM-DD --to YYYY-MM-DD --output json
```

Useful flags:

- `--agent codex|claude|openclaw|hermes|opencode|deepseek|workbuddy|workbuddy-ai|all`: select sources. `usage` defaults to `codex`; `report range` defaults to `all`. `sources` lists every source and has no `--agent` filter.
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
- `--workbuddy-home PATH`: override `WORKBUDDY_HOME` or `~/.workbuddy`.
- `--workbuddy-ai-home PATH`: override `WORKBUDDY_AI_HOME` or `~/.workbuddy-ai`.
- `--output json`: emit machine-readable data.

Default scanned locations:

- Codex: `~/.codex/sessions` and `~/.codex/archived_sessions`.
- Claude Code: `~/.claude/projects`.
- OpenClaw: `~/.openclaw/agents/*/sessions`.
- Hermes Agent: `~/.hermes/state.db` (SQLite).
- OpenCode: `~/.local/share/opencode/opencode.db` (SQLite).
- DeepSeek Harness: `~/.dsh/sessions/<workspace>/<session>/session.jsonl` or `session.jsonl.zstd`.
- WorkBuddy: `~/.workbuddy/projects/**/*.jsonl`.
- WorkBuddy AI: `~/.workbuddy-ai/projects/**/*.jsonl`.

### Source Diagnostics

`sources --output json` returns an array with `agent`, `supported`, `detected`, `paths`, `note`, and optional `errors`. All eight home flags above apply. It checks path existence without reading chats or writing daily reports. Use the same overrides as the target `usage` or `report range` command.

- `supported: true, detected: true`: the collector exists and a source path exists; this does not prove that counters are present or complete.
- `supported: true, detected: false`: the collector exists but its source paths were not found. Check overrides and `errors` before interpreting totals.
- `supported: false`: no token collector. Trae, Doubao, and Doubao Work are diagnostic-only and excluded from `all`; their known-path discovery is macOS-only.

Unsupported or missing sources must not be presented as verified zero usage, even when a usage report's aggregate counters are zero. Do not infer token counts from chat text or application credits.

### Daily Storage

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
- `AI_TOKEN_WORKBUDDY_HOME`: optional WorkBuddy home override.
- `AI_TOKEN_WORKBUDDY_AI_HOME`: optional WorkBuddy AI home override.
- `AI_TOKEN_RUN_DIR`: optional directory for per-run JSON snapshots.

The daily `token-stats` record is the durable source for historical analysis. Per-run snapshots are useful when the user wants intra-day growth traces or audit logs.

The installer accepts all eight `--*-home` flags and persists them for launchd. For compatibility after the skill rename, its defaults retain label `com.baijian.ai-token-ayalysis`, logs under `~/Library/Logs/ai-token-ayalysis`, and snapshots under `~/.local/state/ai-token-ayalysis/runs`. The LaunchAgent PATH includes `~/.local/bin`. Keep snapshots and operational logs private too; the CLI's daily-file permission guarantees do not automatically apply to shell redirects.

Installation starts a persistent user task immediately. Only install or replace it when requested. To stop the default task without deleting reports or its plist:

```bash
launchctl bootout "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.baijian.ai-token-ayalysis.plist"
```

It can load again at login while the plist remains. For permanent removal, confirm removal of that specific plist; retain daily reports unless the user also requests deletion. Substitute the actual label when customized.

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

- Eight agents have collectors in v0.0.2, including the separate `workbuddy` and `workbuddy-ai` sources. Trae, Doubao, and Doubao Work remain diagnostic-only. Missing sources and parser warnings can make machine-level totals incomplete.
- WorkBuddy reads project JSONL, deduplicates responses within each application by session and provider message ID, and excludes mirrored traces. `message.usage`, `providerData.usage`, and `rawUsage` are alternative representations, not additive usage. Each response belongs to its local date; repeated samples use the final timestamp. Cached input is part of input, and reasoning is part of output. `workbuddy.db` context occupancy and credits are not cumulative token usage. Collection was verified with macOS records; do not assume other platforms or log versions provide the same counters.
- Hermes delegated-task usage is included from `session_model_usage`; main-session counters are attributed to the session start day, including sessions spanning midnight.
- SQLite sources are read-only. The immutable fallback emits a warning and may omit uncheckpointed WAL updates; disclose this limitation when it affects a report.
- DeepSeek Harness v0 JSONL and concatenated Zstandard logs are supported (verified upstream with `dsh 0.1.1-rc.2`). Final assistant messages replace earlier samples for the same turn/step, chunk-only usage is included, fork-inherited history is excluded, and subagents use `deepseek:subagent` buckets. Each request belongs to its last usage sample's local day.
- DeepSeek input includes uncached input, cache reads, and cache writes; reasoning is already part of output. Unknown session versions produce warnings.
