---
name: nonblocking-agent-execution
description: >
  Prevents "agent stopped responding / stuck / no output" failures in sandboxed agent
  runtimes (Arena Agent Mode, OpenClaw, Codex) where a single long tool call blocks the
  turn and stdin is closed so interactive prompts hang forever. Provides the
  detach → bounded-poll → durable-state pattern plus a ready-to-use jobctl.sh runner.
  Use when: a build/download/model-inference/mass-install takes minutes, a CLI may
  prompt for input, or the user reports the agent freezing mid-task.
metadata: {"openclaw":{"emoji":"⏳"}}
---

# Non-Blocking Agent Execution

Field-authored in Arena Agent Mode (2026-07) after a real 173-skill install + llama.cpp
build froze the session. Synthesizes lessons from ClawHub skills
`@aowind/long-running-harness`, `@wonko6x9/durable-task-runner`,
`@skywalker-lili/polling-best-practices`, `@liyooyin/task-progress-stream`,
`@nyxun123/agent-heartbeat`, `@hollis9087/long-task-handoff`.

## The three real causes of "agent not responding"

| Cause | Symptom | Fix |
|---|---|---|
| **Blocking tool call** — one `bash` call runs 20 min | UI shows nothing, user aborts | Detach the work; poll in ≤30 s bursts |
| **Interactive prompt with closed stdin** | Hangs forever, never times out | `--yes` / `--no-input` shims + always wrap in `timeout` |
| **Aborted turn kills the child process** | Work silently lost, half-done state | Detach with `setsid`, persist state to disk |

## Core rules

1. **No tool call over ~60 s.** Long work is launched, not awaited.
2. **`setsid nohup … < /dev/null &`** — survives the turn being cancelled; plain `&` does not.
3. **Bounded wait only.** A poll helper that *always* returns within N seconds. Never `wait`.
4. **Every external command gets `timeout N`.** No exceptions for network CLIs.
5. **Non-interactive flags always** (`--yes`, `--no-input`, `-y`, `DEBIAN_FRONTEND=noninteractive`).
6. **State on disk, not in context** — `pid`, `exit_code`, `log`, `started_at` per job, so any
   context reset or new turn can resume by reading files.
7. **Report progress every poll** (`[k/N] item`) so the user sees liveness instead of silence.
8. **Idempotent resume**: recompute what is *missing* and redo only that, never restart from zero.

## The runner

```bash
./jobctl.sh start <name> '<command>'   # detached, returns instantly
./jobctl.sh status <name>              # RUNNING pid=… elapsed=…s | DONE exit=0 | DIED
./jobctl.sh wait <name> [max_sec=25]   # bounded — ALWAYS returns
./jobctl.sh log <name> [n]             # tail live output
./jobctl.sh list                       # every job's state
```

State lives in `~/.jobs/<name>/{cmd,pid,log,exit_code,started_at,finished_at}`.

## Agent loop

```
start job  →  status (2 s)  →  do other useful work  →  wait 25 s  →  report "[k/N]"  →  repeat  →  verify exit=0
```

Parallelize independent jobs in one message; only serialize true dependencies.

## Resume-after-reset recipe

```bash
comm -13 <(ls installed | sort) <(sort wanted.txt) > missing.txt   # diff, don't restart
./jobctl.sh start fill 'while read x; do timeout 120 install "$x"; done < missing.txt'
```

Verify with a byte-exact or hash-exact assertion, never with "it looked fine".
