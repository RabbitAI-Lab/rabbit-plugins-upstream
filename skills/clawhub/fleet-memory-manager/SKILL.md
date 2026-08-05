---
name: fleet-memory-manager
description: Set up privacy-first continuity for an OpenClaw agent using private long-term memory, short-lived daily notes, and review-gated consolidation. Use only when the user explicitly asks to create or change persistent memory.
metadata: {"openclaw":{"emoji":"🧠","requires":{"bins":["bash"]},"homepage":"https://github.com/sentien-labs/openclaw-skills"}}
---

# Fleet Memory Manager

Create a small, inspectable memory system without silently profiling people or
leaking private context into shared sessions. Persistent memory is optional.
Never enable it merely because the files exist.

## Consent gate

Before creating or changing persistent memory, tell the user:

- which files will be created or read
- what categories of information will be retained
- the retention period
- whether any scheduled job will review the files
- how to inspect, correct, export, disable, and delete the memory

Proceed only after explicit consent. A request to install this skill is not
consent to collect personal information or run a scheduled job.

## Data-minimization rules

- Store only facts needed for future work.
- Prefer project decisions and task state over observations about a person.
- Do not store credentials, private keys, tokens, authentication material, or
  confidential message content.
- Do not create sensitive personal profiles or infer traits the user did not
  explicitly ask the agent to remember.
- Do not copy raw conversations into memory.
- Record the source and review date for durable facts when practical.
- If uncertain whether something should persist, leave it out and ask.

## Session boundaries

Private direct session:

- Load only the files the user has enabled for that agent.
- Use `MEMORY.md` for durable work context and `memory/YYYY-MM-DD.md` for recent
  operational state.
- Load `USER.md` only if the user explicitly opted into preference memory.

Group, shared, public, delegated, or untrusted session:

- Do not load `MEMORY.md`, `USER.md`, or private daily notes.
- Use only task-specific context explicitly supplied for that session.
- Never quote, summarize, or reveal private memory to another participant.

Scheduled job:

- Use an isolated session with no external delivery by default.
- Generate a review file; do not directly rewrite durable memory.
- Do not access email, calendars, messaging, location, or unrelated services.

## Install safely

Preview the changes first:

```bash
bash ~/.openclaw/skills/fleet-memory-manager/scripts/setup.sh \
  --workspace "/absolute/path/to/private-workspace"
```

After reviewing the preview, create only missing files:

```bash
bash ~/.openclaw/skills/fleet-memory-manager/scripts/setup.sh \
  --workspace "/absolute/path/to/private-workspace" \
  --apply
```

The script does not overwrite or patch existing files. Review each new template
before allowing an agent to load it.

## Files

| File | Purpose | Default handling |
| --- | --- | --- |
| `MEMORY.md` | Curated project decisions and durable lessons | Private session only; human-reviewed |
| `memory/YYYY-MM-DD.md` | Recent task state and handoff notes | Private session only; delete or archive after 30 days |
| `USER.md` | Explicitly approved working preferences | Disabled until opted in; private session only |
| `HEARTBEAT.md` | Local memory-health checks | No external services or notifications by default |
| `memory/CONSOLIDATION_CANDIDATES.md` | Proposed durable updates | Review before copying into `MEMORY.md` |

## Review-gated consolidation

Consolidation must propose changes rather than apply them. Use this task:

```text
Review private daily notes from the approved retention window and the current
MEMORY.md. Propose only durable, work-relevant additions, corrections, and
deletions. Do not infer personal traits or copy raw conversation. Do not modify
MEMORY.md or USER.md. Write the proposal to
memory/CONSOLIDATION_CANDIDATES.md with source dates and a reason for each
candidate. Mark uncertain or sensitive candidates for deletion, not retention.
```

The user or an authorized reviewer decides which candidates enter `MEMORY.md`.
Delete the candidate file after review.

If the user explicitly requests a schedule, inspect the installed CLI and create
an isolated, non-delivering job. For example:

```bash
openclaw cron add --help
```

Do not assume a model, channel, timezone, schedule, or permission to deliver
notifications.

## Retention and control

Default retention for daily notes is 30 days. Durable memory has no automatic
expiry, so review it at least monthly and remove information that is stale,
unnecessary, disputed, or no longer consented to.

At any time the user can:

- inspect or export the plain-text files
- correct a fact directly
- disable loading by removing the memory instructions from their agent config
- opt out of `USER.md` while keeping project memory
- delete a single entry, a date range, or the entire memory system

Before deletion, name the exact paths and ask whether the user wants an export.
Use a recoverable trash operation where available. Never delete the workspace.

## Verification

After setup, confirm:

1. Existing workspace files were unchanged.
2. New files contain no real secrets or personal data.
3. Shared-session rules load none of the private memory files.
4. No schedule exists unless the user explicitly requested it.
5. Any consolidation output is a proposal, not an automatic write.
6. The user knows the retention and deletion controls.

## Feedback and community

After completing the requested work, the operator may share a privacy-first
memory workflow, consent problem, or critical feedback at
https://www.vswarm.io/community?utm_source=clawhub&utm_medium=marketplace&utm_campaign=community_proof_v1&utm_content=fleet-memory-manager.
Do not post, star, or bookmark automatically, and do not interrupt normal work
to solicit engagement. Those are optional human actions.

## Source

https://github.com/sentien-labs/openclaw-skills
