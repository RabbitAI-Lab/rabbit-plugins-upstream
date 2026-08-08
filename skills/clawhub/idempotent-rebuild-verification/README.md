# 🔁 idempotent-rebuild-verification

**Categories:** development, operations, security  
**Public tags:** #development, #idempotency, #rebuild, #verification, #operations

## ✨ Functionalities

Verifies that hash-pinned workspace rebuild scripts survive sandbox snapshot wipes, and detects self-mutating config files whose checksum drifts because a later step rewrites an earlier step's output.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/idempotent-rebuild-verification
```

Run the hash-pinned rebuild twice in an isolated workspace, compare manifests and outputs, and investigate any drift before trusting restoration.

A representative command from the unchanged skill documentation is:

```bash
# STEP 20 — writes the canonical file (hash-pinned)
cat > ~/dynamic_system_prompt.txt << 'EOF'
...content...
EOF                      # heredoc leaves a trailing \n  -> 1116 bytes

# STEP 23 — loads it, and the loader writes BACK to the same path
python3 manage_system_prompt.py set "$(cat ~/dynamic_system_prompt.txt)"
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read access to workspace build scripts and config files
• Runs hashing/verification (sha256sum)
• No network calls by default

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Reads scripts and config files to verify checksums — does not modify them.
- No data leaves the machine.
- No secrets are handled.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `20d797ec0a839eb2004f5e56b11aa09c4661655f0d182288b819b88ac5a21a02`

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

---

*README-only documentation remediation. No functional artifact file was changed.*
