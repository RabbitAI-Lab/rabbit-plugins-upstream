---
name: self-review
description: Reviews logged incidents and activity to improve agent configuration through proposed edits to core files
---

# Self-Review Skill

Free to use. If this saved you time, you can support development here:
[PAYMENT_LINK]

## Overview
This skill helps agents improve their own configuration by analyzing logged incidents and activity patterns, then proposing specific edits to enhance future performance. It examines AGENTS.md, SOUL.md, HEARTBEAT.md, MEMORY.md, TOOLS.md, USER.md, Manuel.md, and SKILLS.md.

## Installation
1. Place this skill in your agent's skills directory (e.g., `./skills/self-review/`)
2. The skill will automatically create a `trainer/` directory at `../../trainer/` relative to itself on first run:
   - If skill is at `./skills/self-review/`, trainer will be created at `../../trainer/`
   - Adjust the path if your directory structure differs
3. The trainer directory contains all state needed for the self-review process:
   - `logs/incidents.md` - incident log file
   - `config.js` - configuration file (AUTO_APPLY: false/true)
   - `logs/.last-review` - timestamp tracking last review run
   - `proposals/` - directory for review proposals awaiting approval
   - `backups/` - directory for file backups before applying changes

## How It Works

### When to run
- Weekly, or when `../../trainer/logs/incidents.md` has 10+ new entries since the last review
- On manual request ("run self-review")

### Step 1 — Gather
**First-run setup**: If `../../trainer/` doesn't exist, the skill automatically creates the complete folder structure:
- Creates `../../trainer/logs/`, `../../trainer/proposals/`, `../../trainer/backups/` directories
- Creates `../../trainer/config.md` with: `AUTO_APPLY: false`
- Creates `../../trainer/logs/.last-review` with: `2000-01-01T00:00:00`
- Creates `../../trainer/logs/incidents.md` with: `<!-- format: ## [YYYY-MM-DD HH:MM] short title / type: fail|friction|win / what happened / what was tried / result / suspected file -->`

- Read every entry in `../../trainer/logs/incidents.md` timestamped after the value in
  `../../trainer/logs/.last-review` (create with far-past date if missing)
- Skim `HEARTBEAT.md` and `MEMORY.md` for relevant activity not formally logged
- If nothing new since last review, stop and report "nothing to review"

### Step 2 — Classify
For each incident, note:
- type: fail / friction / win
- what happened, what was tried, what worked or didn't
- best-guess target file:
  - AGENTS.md — behavior rules, task workflow, decision logic
  - SOUL.md — identity, values, tone, personality
  - HEARTBEAT.md — recurring routines, check-in cadence
  - MEMORY.md — durable facts worth remembering
  - TOOLS.md — tool usage patterns, gotchas, correct invocations
  - USER.md — user preferences, context, constraints
  - Manuel.md — step-by-step how-tos / procedures
  - SKILLS.md — skill index, when to use which skill

### Step 3 — Draft proposed edits
- Surgical, specific edits only — never a full-file rewrite
- Every proposed edit must cite the incident(s) that justify it
- Group by target file
- Save as `../../trainer/proposals/<YYYY-MM-DD>-review.md`, formatted like:

 ### AGENTS.md
 - ADD under [section]: "..."
 - Reason: incidents #3, #7 — repeated X failure

 (repeat per affected file)

### Step 4 — Apply or hold
- Read `../../trainer/config.md`
- If AUTO_APPLY: false (default) — stop here. Present the proposal to the agent operator
  in chat and wait for explicit approval before touching any live file.
- If AUTO_APPLY: true — for each approved-category edit:
  1. Copy the current file to `../../trainer/backups/<filename>.<timestamp>.bak`
  2. Apply the edit exactly as drafted — no improvising beyond what was proposed
  3. Log what changed to `../../trainer/logs/applied.md`
- Regardless of AUTO_APPLY, SOUL.md and USER.md always require manual approval —
  never auto-edit identity or user-context files.

### Step 5 — Close out
- Update `../../trainer/logs/.last-review` to the current timestamp
- Summarize in plain language what was found and what changed (or is pending approval)

## Configuration
The `../../trainer/config.md` file controls behavior:
```
AUTO_APPLY: false
```

Set to `true` to enable automatic application of safe edits (excludes SOUL.md and USER.md which always require manual approval).

The system will automatically initialize required files with these defaults on first run:
- `../../trainer/logs/.last-review`: `2000-01-01T00:00:00`
- `../../trainer/logs/incidents.md`: `<!-- format: ## [YYYY-MM-DD HH:MM] short title / type: fail|friction|win / what happened / what was tried / result / suspected file -->`