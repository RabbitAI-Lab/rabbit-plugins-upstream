# ⏳ nonblocking-agent-execution

**Categories:** agents, automation, operations  
**Public tags:** #agents, #nonblocking, #orchestration, #background-jobs, #automation

## ✨ Functionalities

Prevents 'agent stopped responding / stuck / no output' failures in sandboxed agent runtimes (Arena Agent Mode, OpenClaw, Codex) by providing a detach → bounded-poll → durable-state pattern plus a ready-to-use jobctl.sh runner.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/nonblocking-agent-execution
```

Start work through the documented job controller, detach long tasks, poll with bounded waits, persist state, and collect the final exit code and artifacts.

A representative command from the unchanged skill documentation is:

```bash
./jobctl.sh start <name> '<command>'   # detached, returns instantly
./jobctl.sh status <name>              # RUNNING pid=… elapsed=…s | DONE exit=0 | DIED
./jobctl.sh wait <name> [max_sec=25]   # bounded — ALWAYS returns
./jobctl.sh log <name> [n]             # tail live output
./jobctl.sh list                       # every job's state
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Runs and supervises subprocesses
• Writes durable job state files
• May use background/daemon execution

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Supervises the processes you ask it to run.
- Job state is written to local disk.
- No secrets are collected beyond what the supervised command uses.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `b55f3e86da047387cc059cd03eab8f27c2add89c15e433a5e015496cb42d7099`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

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

---

*README-only documentation remediation. No functional artifact file was changed.*
