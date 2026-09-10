---
name: subagent-overseer
version: 1.1.2
description: "You spawned 4 sub-agents. One died 20 minutes ago. You're still waiting. Overseer watches them so you don't have to — zero tokens, pure OS-level process checks. No polling loops, no wasted heartbeats."
metadata:
  openclaw:
    emoji: "👁️"
    notes:
      security: "No network calls, no credentials, no writes outside its own status directory. It reads /proc, runs `openclaw sessions list` once per cycle, and counts recently-changed files under --workdir. The one piece of real content it handles is filenames: the status file records the basenames of up to five recently-changed files, which can reveal what you are working on. That directory is per-user and mode 0700 (XDG_RUNTIME_DIR, else /tmp/overseer-$UID); --no-filenames drops the names entirely; voice alerts speak counts only unless you pass --voice-files. It is a background daemon, so it ships its own off switch: --stop and --cleanup."
---

# Sub-Agent Overseer

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

You spawned 4 sub-agents. One died 20 minutes ago. You're still waiting.

Nobody told you, because nobody was watching — and the thing you'd normally ask to watch them charges you a tool call every time it blinks.

There's a cheaper kind of eye for this.

Overseer keeps watch over your sub-agents the way the operating system already does — checking which ones are still running and how long each has gone quiet. A tiny background process writes down their health every few seconds, so when your agent's heartbeat wakes up, it just reads that note and goes back to sleep. While everything is healthy it spends nothing: no model, no questions, no busywork. The moment an agent stalls or dies, the note says so, and you can act before another twenty minutes leak away.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

<why_this_matters>
A heartbeat agent polling sub-agents with LLM tool calls burns tokens for what is fundamentally an OS-level check. Overseer is a lightweight pull-based bash daemon that monitors sub-agent health, writes a status file every N seconds, and lets the heartbeat handler do zero tool calls when the status file is fresh and healthy.
</why_this_matters>

## Architecture

```
overseer.sh (bash, runs in background)
    ├── /proc/<pid>  → gateway alive? CPU? threads?
    ├── openclaw sessions list  → sub-agent count + ages
    ├── find -newer marker  → filesystem activity
    └── writes <status-dir>/status.json  (atomic mv)

heartbeat (agent, every 3min)
    └── reads <status-dir>/status.json → summarize or HEARTBEAT_OK

<status-dir> defaults to $XDG_RUNTIME_DIR/overseer, or /tmp/overseer-$UID.
Ask for it rather than guessing:  scripts/overseer.sh --status-path
```

The overseer does all the data collection. The heartbeat handler does zero tool calls if the status file is fresh and healthy.

## Quick Start

### 1. Start the overseer when spawning sub-agents

```bash
setsid scripts/overseer.sh \
  --workdir /path/to/repo \
  --interval 180 \
  --max-stale 4 \
  &>/dev/null &
```

Scope `--workdir` as narrowly as the work allows: the names of files that change
under it are what ends up in the status file. Add `--voice` for spoken alerts
(counts only), or `--no-filenames` to keep names out of the status file entirely.

### 2. Heartbeat reads the status file

```bash
cat "$(scripts/overseer.sh --status-path)"
```

### 3. Stop it when you are done

```bash
scripts/overseer.sh --stop      # stop the daemon
scripts/overseer.sh --cleanup   # stop it and delete its status, log and pid files
```

It also stops itself after two cycles with no sub-agents, but a background process
you cannot stop on demand is not really optional, so the off switch is explicit.

### 4. Interpret the status

| Field | Meaning |
|---|---|
| `subagents.count` | Active sub-agent sessions |
| `subagents.details[].stale` | Consecutive cycles with no filesystem changes |
| `subagents.details[].status` | `active` / `idle` / `warning` / `stuck` |
| `gateway.health.alive` | Is `openclaw-gateway` running? |
| `filesystem.changes_since_last` | Files modified since last check |

### 5. Staleness thresholds (at 180s interval)

| stale count | Time | Status | Action |
|---|---|---|---|
| 0-1 | 0-3 min | `active`/`idle` | Normal |
| 2-3 | 6-9 min | `warning` | Voice alert (if --voice) |
| ≥4 | ≥12 min | `stuck` | Agent should investigate/kill |

<heartbeat_protocol>
When HEARTBEAT.md fires:

1. Read the status file (`overseer.sh --status-path`). If missing or stale (>10 min), restart overseer.
2. If `subagents.count == 0` for 2+ cycles → overseer auto-exits → reply `HEARTBEAT_OK`.
3. If all agents `active` → brief one-line status → `HEARTBEAT_OK`.
4. If any `stuck` → report which labels are stuck → consider killing via `subagents kill`.
5. Always read the status file fresh; don't cache a previous heartbeat response.
</heartbeat_protocol>

## Flags

| Flag | Default | Description |
|---|---|---|
| `--interval` | 180 | Seconds between checks |
| `--workdir` | cwd | Directory to watch for file changes |
| `--labels` | (all) | Comma-separated labels to filter |
| `--max-stale` | 4 | Cycles before marking `stuck` |
| `--voice` | off | Local TTS alerts via `jarvis` command. Speaks counts, never filenames |
| `--voice-files` | off | Speak changed filenames aloud too. Implies `--voice` — anyone in earshot hears what you are working on |
| `--no-filenames` | off | Never record filenames: the status file gets the change count and nothing else |
| `--status-dir` | per-user | Where status/log/pid live (also `OVERSEER_DIR`) |
| `--status-path` | — | Print the status file path and exit |
| `--stop` | — | Stop the running overseer |
| `--cleanup` | — | Stop it, then delete its status, log, marker and pid files |

<how_it_works>
No AI tokens involved:

1. **Gateway health:** Reads `/proc/<pid>/status` for CPU, memory, threads, FD count. Pure kernel data.
2. **Sub-agent list:** Single `openclaw sessions list` call per cycle. Parses grep output.
3. **Filesystem diff:** `find -newer marker` — detects any file writes in the workdir.
4. **Status file:** JSON written atomically (write to temp, `mv` into place). Any reader sees a complete file.
5. **Self-exit:** If no sub-agents for 2 consecutive cycles, the overseer stops itself.
6. **Dedup:** `flock` ensures only one overseer instance runs at a time.
</how_it_works>

## What it records, and who can read it

The only content this daemon handles is filenames. Everything else is counters and
process state. The status file holds the number of files changed under `--workdir`
since the last cycle and the basenames of up to five of them — enough to tell you an
agent is alive, and enough for someone reading the file to tell what you are working on.

So the runtime directory is per-user and created mode 0700: `$XDG_RUNTIME_DIR/overseer`
when that exists, otherwise `/tmp/overseer-$UID`. (Before 1.1.2 it was `/tmp/overseer`,
one shared directory for every user on the machine. If you have tooling pinned to that
path, `--status-dir /tmp/overseer` restores it — knowing what that means.) `--no-filenames`
drops names entirely, and voice alerts speak counts unless you pass `--voice-files`.

Nothing leaves the machine: no network calls, no telemetry, no credentials read. Writes
are confined to the status directory.

## Running the tests

```bash
bash tests/test_overseer.sh
```

Starts throwaway daemons in temp directories and checks the privacy and lifecycle
controls above. It never touches a real overseer or a real workspace.

<cost>
- Overseer: $0.00 (bash + /proc + one CLI call per cycle)
- Voice alerts: $0.00 (local sherpa-onnx via `jarvis`)
- Heartbeat reads status file: $0.00 (one `cat` command)
- Only cost is the heartbeat model itself (qwen3 local = free)
</cost>

## Pairs Well With

- [agent-superpowers](https://clawhub.ai/globalcaos/agent-superpowers) — the three-agent review pipeline that Overseer was built to monitor
- [smart-model-router](https://clawhub.ai/globalcaos/smart-model-router) — auto-select models for each sub-agent role

https://github.com/globalcaos/tinkerclaw

_Clone it. Fork it. Break it. Make it yours._
