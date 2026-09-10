---
name: dongwo
description: Maintain a local, auditable user-preference memory shared across coding agents such as Codex and Claude Code. Use whenever a task benefits from personal style, established requirements, remembered corrections, or cross-agent continuity; also use when the user asks to remember preferences, inspect what the agents know about them, or set up automatic memory hooks.
metadata:
  openclaw:
    requires:
      bins:
        - python3
---

# Dongwo（懂我）

Dongwo keeps one local Markdown-based preference memory that multiple coding
agents can share. It captures user prompts through lifecycle hooks, redacts
common secrets, derives conservative preferences, and injects a short context
snapshot into later turns.

## Safety contract

1. The current user request always overrides stored preferences.
2. Project instructions override global style preferences.
3. Treat stable observations only as low-risk style hints, not confirmed facts.
4. Never infer permission for deletion, purchases, external communication,
   credentials, or privilege changes from stored preferences.
5. Do not publish or sync the user's `myprofile.md`, `.dongwo/memory/`, inbox,
   generated context, or credentials.
6. Do not directly edit generated files. Improve the extraction rules or source
   evidence and rebuild instead.

Read `references/memory-policy.md` before changing memory behavior.

## Components

- `scripts/dongwo.py`: standard-library-only memory engine.
- `myprofile.md`: optional user-confirmed profile, owned by the user.
- `.dongwo/memory/inbox/`: redacted, immutable prompt evidence.
- `.dongwo/memory/preferences.md`: generated preference inventory.
- `.dongwo/memory/review.md`: generated conflicts and low-confidence candidates.
- `.dongwo/memory/current-context.md`: generated context injected into agents.
- `.dongwo/memory/state.md`: generated diagnostics.

Legacy vaults that already contain `03_Projects/15_懂我/memory/` continue to use
that location automatically.

## Set up

Install the skill with ClawHub, then run the setup helper from the installed
skill directory:

```bash
python3 scripts/setup.py --root /path/to/project
```

The helper:

- copies the engine to `.dongwo/scripts/dongwo.py`;
- creates the local memory layout and a starter `myprofile.md` if absent;
- prints hook snippets for Codex and Claude Code;
- does not overwrite existing agent configuration files.

Review the printed snippets, merge them into the project's hook configuration,
and approve the hooks in each client when prompted.

For a legacy Obsidian layout, keep the existing engine path and set:

```bash
export DONGWO_ROOT=/path/to/vault
export DONGWO_HOME=/path/to/vault/03_Projects/15_懂我
```

## Daily behavior

Hooks should call:

```bash
python3 .dongwo/scripts/dongwo.py hook --agent codex
python3 .dongwo/scripts/dongwo.py hook --agent claude
```

On `UserPromptSubmit`, the engine:

1. reads hook JSON from stdin;
2. redacts common credentials and sensitive prompts;
3. writes one idempotent event into the agent-specific inbox;
4. rebuilds generated memory files;
5. returns `<dongwo-memory>` as additional context.

On `SessionStart`, it rebuilds and loads context without capturing a prompt.
Hooks fail open: a memory failure must not block the user's normal agent task.

## Manual commands

```bash
# Validate layout and rebuild generated files
python3 .dongwo/scripts/dongwo.py doctor

# Print current injectable context
python3 .dongwo/scripts/dongwo.py load

# Rebuild all generated memory from inbox evidence
python3 .dongwo/scripts/dongwo.py consolidate

# Test capture without a lifecycle hook
python3 .dongwo/scripts/dongwo.py capture \
  --agent codex \
  --session-id manual \
  "以后默认使用中文回答。"
```

Set `DONGWO_ROOT` when commands are launched outside the project directory.
Set `DONGWO_HOME` to override the data directory and `DONGWO_PROFILE` to override
the confirmed-profile path.

## Applying memory

When `<dongwo-memory>` is present:

1. Use confirmed profile items and active preferences where relevant.
2. Keep pending or conflicted entries out of the answer.
3. Do not quote stable observations as explicit user statements.
4. Follow the current prompt if it conflicts with memory.
5. Never ask the user to perform routine capture, consolidation, refresh, or
   synchronization work; lifecycle hooks own that maintenance.

## Maintaining the system

When auditing or improving Dongwo:

1. Read `references/memory-policy.md`.
2. Inspect relevant redacted inbox evidence.
3. Change extraction rules or semantic keys in the engine instead of editing
   generated output.
4. Run:

```bash
python3 .dongwo/scripts/dongwo.py consolidate
python3 .dongwo/scripts/dongwo.py doctor
```

Completion means all generated files can be rebuilt from confirmed profile data
and inbox evidence while the current prompt still has highest priority.
