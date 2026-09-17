---
name: "dr-agent-backup"
description: "6-hour deterministic backup runner"
---

# DR. Agent Backup

Use when setting up, auditing, repairing, or restoring backup continuity for a Daniel-owned agent.

Goal: agent memory and workspace state should survive VM loss or migration. Restore should be boring: clone or pull the repo, restore credentials separately, verify the agent starts, and reindex memory if needed.

## Core Policy

1. Back up agent-owned workspace files to a Daniel-owned Azure DevOps git repository.
2. Treat backup execution as deterministic infrastructure, not conversational agent memory.
3. Install or verify an independent non-LLM backup runner on each agent host once a remote and credential method are configured.
4. Run routine backup every 6 hours by default using a local scheduler such as a systemd user timer, OS cron, or equivalent deterministic substrate.
5. Commit only allowlisted restore-relevant workspace files and push them to the configured backup remote.
6. Keep credentials, local stores, runtime logs, caches, databases, bulky generated state, raw transcripts, media dumps, and env files out of git unless Daniel explicitly approves.
7. Treat git as continuity for human-readable source of truth, not a full machine image.
8. Restore auth material through the approved secret manager, protected env file, deploy key, credential helper, or provider login flow.
9. Notify Daniel immediately if an intended backup commit or push cannot be completed.

## Execution Architecture

Prefer Pattern B1: thin scheduler trigger to a non-agent runner plus local manifest or config resolution.

The scheduler should only wake the runner. It should not depend on an LLM, a chat session, heartbeat memory, profile shell startup, or stale prompt state.

The backup runner should be self-contained:

- resolve the workspace path explicitly
- load its own manifest or config at runtime
- use an explicit credential path or git credential helper
- load the approved backup credential contract itself at runtime
- set `GIT_TERMINAL_PROMPT=0`
- run safe git status checks
- stage only allowlisted restore-relevant paths
- run a path and content safety scan before commit
- commit only when staged changes exist
- push to the configured remote and branch
- write a small local status or ledger artifact outside git
- exit non-zero on auth, staging, commit, or push failure

Do not rely on an agent remembering that an env file exists. The script or scheduler unit must make the credential contract explicit.

## Routine Schedule

Default routine backup schedule:

- every 6 hours
- persistent or catch-up enabled when the substrate supports it
- deterministic non-LLM runner
- no live notification on success unless Daniel asks

For systemd user timers, prefer:

- `OnBootSec=5min`
- `OnUnitActiveSec=6h`
- `AccuracySec=5min`
- `Persistent=true`

## Backup Health vs Backup Execution

Separate backup execution from health monitoring.

The 6-hour backup job is responsible for committing and pushing safe changes.

A health monitor is responsible for detecting and notifying on failures. It may run more often than the backup job, but it should not treat ordinary restore-relevant dirty files as a failure until the backup runner has had a reasonable chance to process them.

Health checks should detect:

- scheduler or timer inactive or missing
- backup runner missing or not executable
- protected credential contract missing or malformed
- rejected Git credentials
- failed remote access
- failed push or push dry-run
- local backup branch not matching the remote after a backup attempt
- no successful backup within the approved freshness window
- restore-relevant files still uncommitted after the backup job attempted to run
- notification delivery failure

Recommended alert policy:

- check health every 15 minutes when a monitor is installed
- DM Daniel at most once every 24 hours while the same failure remains active
- include concise failure reason and inspect command
- do not print credential values

## What To Track

Default include list:

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `MEMORY.md`
- `HEARTBEAT.md` when present
- `memory/**/*.md`
- intentional durable `memory/**/*.json`
- `context_pipeline/**`
- `automation/**` excluding runtime outputs and protected credential files
- `skills/**` for workspace-local skills
- `doc_reviews/**/*.md` when used as active review state
- project notes and templates Daniel expects to restore

Default exclude list:

- credential material and local auth profiles
- `.env`, `*.env`, `gateway.systemd.env`, and backups of env files
- SQLite databases and WAL or SHM files unless explicitly approved
- `node_modules/`, package caches, build outputs
- raw session transcripts unless Daniel explicitly wants them tracked
- inbound or outbound media files unless intentionally curated
- temporary files, logs, downloads, generated archives
- large binary or customer files unless explicitly approved

## Setup Workflow

1. Confirm the Azure DevOps organization, project, repo name, branch, and credential method.
2. Confirm credential method: SSH deploy key, Azure DevOps PAT stored outside git, or existing authenticated git credential helper.
3. Initialize or connect the workspace repo.
4. Add or verify a `.gitignore` that blocks credentials, env files, runtime state, caches, databases, logs, media dumps, and generated archives.
5. Create or verify the backup manifest or config.
6. Create or verify the self-contained backup runner.
7. Run a dry-run status review before the first commit.
8. Run a dry-run backup or safe first backup with Daniel-approved remote and credentials.
9. Install or verify the 6-hour deterministic scheduler.
10. Verify the registered scheduler payload or substrate, not just local template files.
11. Create or verify backup health monitoring and failure notification.
12. Test health-check output and notification rendering before enabling live notifications.
13. Record restore notes in memory or an approved ops file.

## Commit Policy

Commit after meaningful changes to:

- long-term memory
- daily memory logs that contain decisions or restore-relevant facts
- agent instructions or identity files
- automation manifests and scripts
- local skills or proposal-derived workflow files
- context pipeline files
- important operational notes

The routine 6-hour runner may batch related changes. It should avoid empty commits and noisy transient logs.

Recommended commit message style:

```text
memory: capture gateway restore and embedding fix
agent: update baseline behavior notes
backup: add six-hour backup runner
skill: revise agent backup policy
```

## Before Commit Checklist

Before committing, the runner or agent must:

1. Run `git status --short` or equivalent porcelain status.
2. Stage only allowlisted restore-relevant files.
3. Inspect staged filenames for protected/runtime patterns.
4. Scan staged textual content for high-risk credential patterns where practical.
5. Confirm `.gitignore` covers known OpenClaw protected files and runtime state.
6. Commit only intentional files.

If protected material appears staged, stop and unstage it. Do not rely on later cleanup.

## Restore Workflow

1. Install OpenClaw and baseline system packages.
2. Clone or pull the Azure DevOps repo into the expected workspace path.
3. Restore credentials and auth using the approved path or provider flow, not git.
4. Install or enable required plugins and skills.
5. Verify gateway service and lingering if this is a Linux user service.
6. Run memory status and reindex if needed:

```bash
openclaw memory status --index
openclaw memory index --force
```

7. Verify channels and delivery targets.
8. Run a small end-to-end DM test.
9. Commit any restore-specific notes that are useful for next time.

## Agent Behavior

Agents should run safe git checks, local backup dry-runs, commits, and deterministic scheduler verification themselves when they have access.

Ask Daniel before:

- creating a new Azure DevOps repo
- adding or changing credentials or PATs
- pushing to a new remote for the first time
- enabling live notifications when schedule, target, cooldown, retry behavior, or message format has not already been approved
- changing access controls
- committing files that may contain private or customer data beyond normal memory notes
- deleting history or rewriting commits

## Audit Workflow

For an existing agent, audit backup health by checking:

- Is the workspace a git repo?
- Is the remote Azure DevOps and reachable?
- Is the current branch the intended backup branch?
- Is `.gitignore` strong enough?
- Is there a self-contained backup runner?
- Is a deterministic 6-hour backup scheduler installed and active?
- Does the registered scheduler payload or substrate point to the expected runner and manifest?
- When was the last successful backup commit and push?
- Does the health monitor distinguish backup execution failures from ordinary dirty files awaiting the next run?
- Are protected files absent from tracked and staged files?
- Is there a documented restore path?

Report the result as:

1. backup status
2. routine backup job status
3. monitor/notification status
4. risks
5. recommended `.gitignore` changes
6. files that should be tracked
7. verification results
8. exact next action

Keep it short unless Daniel asks for full detail.

## Boundaries

This skill does not replace VM snapshots or system-level backups. It protects the agent's durable working memory and configuration source, not every runtime artifact.

This skill does not store credentials in git.
