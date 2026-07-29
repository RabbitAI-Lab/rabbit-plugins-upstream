---
name: idempotent-rebuild-verification
description: Verify hash-pinned workspace rebuild scripts survive sandbox snapshot wipes, and detect self-mutating config files whose checksum drifts because a later step rewrites an earlier step's output.
version: 1.0.0
tags: [rebuild, idempotency, sha256, sandbox, snapshot, agent-workspace, verification]
license: MIT
---

# Idempotent Rebuild Verification

Runbooks that recreate an agent workspace ("run these 25 steps") pin each written file
with a `sha256 must be:` line. That is the right instinct — a truncated heredoc paste is
the #1 failure mode. But hash-pinning has a trap that produces **false alarms**, and this
skill is how to tell a real corruption from a benign one.

## The core trap: a step that rewrites its own input

Pattern observed in the field:

```bash
# STEP 20 — writes the canonical file (hash-pinned)
cat > ~/dynamic_system_prompt.txt << 'EOF'
...content...
EOF                      # heredoc leaves a trailing \n  -> 1116 bytes

# STEP 23 — loads it, and the loader writes BACK to the same path
python3 manage_system_prompt.py set "$(cat ~/dynamic_system_prompt.txt)"
```

`$(...)` **strips all trailing newlines**, and `set_prompt()` does
`open(PROMPT_FILE,"w").write(text)` — same path, no newline re-added. Net effect:

| | bytes | sha256 |
|---|---|---|
| after STEP 20 | 1116 | `b23dd398…add12114` ✅ pinned value |
| after STEP 23 | 1115 | `3b5db856…f1908148` ❌ "mismatch" |

The runbook's own step sequence guarantees the pinned hash fails on re-verify. Nothing is
corrupt: the content is byte-identical minus one `\n`.

## Triage: benign drift vs. real corruption

Run this before re-pasting anything (re-pasting a big heredoc is how you *cause* damage):

```bash
f=~/dynamic_system_prompt.txt; want=b23dd398...   # the pinned hash
got=$(sha256sum "$f" | cut -d' ' -f1)
[ "$got" = "$want" ] && { echo OK; exit 0; }

# 1) trailing-newline-only difference?
if [ "$(printf '%s\n' "$(cat "$f")" | sha256sum | cut -d' ' -f1)" = "$want" ]; then
  echo "BENIGN: trailing-newline drift (a later step rewrote this file)"
else
  echo "REAL: content differs — diff before you re-paste"
fi
```

Decision table:

| Symptom | Meaning | Action |
|---|---|---|
| size off by exactly 1, tail lost `\n` | consumed by `"$(cat …)"` round-trip | re-run the *writer* step; do not re-paste blindly |
| size much smaller, file ends mid-token | truncated heredoc paste | delete + re-paste whole block |
| size 15 bytes on a "model download" | HTML error page, not a model | wrong URL/repo path |
| hash differs, size identical | real content change | `diff` against a fresh write |

## Rules that make a rebuild genuinely idempotent

1. **Never let step N rewrite a file that step M<N hash-pinned.** Load into a variable or
   a *different* path (`~/.active_prompt`), leaving the canonical file immutable.
2. **Pin content, not bytes**, for files that pass through shells:
   `sha256 of "$(cat f)"` normalises trailing newlines and is round-trip stable.
3. **Re-verify after a wipe, not just after a write.** Snapshot-excluded dirs
   (`build/`, `node_modules/`, `dist/`, `__pycache__/`, `.venv/`, `target/`, `out/`) vanish
   between turns while `~/*.sh` survives — so "scripts OK, binaries gone" is the normal
   post-wipe state, and only the compile step needs re-running.
4. **Extract runbook steps programmatically, and beware nested fences.** Splitting a
   markdown runbook on ` ```bash … ``` ` breaks on any step whose heredoc *contains* a
   code fence — the regex stops at the inner fence and silently truncates the payload.
   Cut such steps by explicit line range and confirm the terminating `EOF_*` label is
   present before executing.
5. **Parallelise only across independent steps** (source clone ∥ toolchain install;
   compile ∥ model download). Keep declared ordering constraints; wall-clock drops a lot
   on 2-core sandboxes where downloads are I/O-bound and builds are CPU-bound.
6. **Assert byte sizes on binary downloads.** A byte-exact match is a cheap, strong
   integrity signal; a curl of an HTML error page is otherwise indistinguishable from success.

## Post-wipe symptom → step router

```
cmake/g++ missing .............. toolchain install step
~/.shim gone / npx hangs ....... shim step (sandboxes with closed stdin need --yes)
build/bin/* missing ............ compile step   (build/ is snapshot-excluded)
*.gguf missing ................. model download step
script hash mismatch ........... run the triage block above FIRST
skill count dropped ............ mass-install step (idempotent, safe to re-run)
```

Authored in the field (Arena Agent Mode, 2026-07) while executing a 25-step, hash-pinned
workspace rebuild: 12/12 files matched on first write; the single "mismatch" on re-verify
was this newline round-trip, and one step needed line-range extraction because its
heredoc embedded a code fence.
