---
name: self-improvement-memory
description: "Self-Improvement Memory (SIM) for agents: records fixes for recurring problems, what was tried, why, what it was expected to fix and what actually happened. Use when diagnosing a problem that came back (a silent bot, a failing cron, release or pipeline run, an error seen before) and before or after changing an agent's config, instructions, skills, schedules or tooling. Based on the paper Self-Improvement Memory Enables Continual Recursive Self-Improvement (Yu et al., 2026)."
license: MIT-0
metadata:
  {
    "openclaw":
      {
        "emoji": "🧠",
        "homepage": "https://github.com/Ricardodpalmeida/self-improvement-memory",
      },
  }
---

# Self-Improvement Memory (SIM)

The harness is everything around the model: config, bootstrap files such as AGENTS.md, skills, schedules, plugins and the scripts an agent runs. When it breaks, the fix usually lands in the harness, and the reasoning behind it is forgotten by the next session. This memory keeps, for each recurring problem, every change tried, why, what it was expected to fix and what actually happened. Keep the evidence, not only the diagnosis.

Typical triggers: a bot or agent goes silent again, a cron, release or publication run fails again, an error that was seen before, or a question about what was already tried.

## Research basis

Based on the paper [*Self-Improvement Memory Enables Continual Recursive Self-Improvement*](https://arxiv.org/abs/2611.18856) (Yu et al., 2026). This skill is an independent adaptation for everyday agent maintenance, not affiliated with or endorsed by the authors or their employers.

## Where the memory lives

Use the folder the user or the agent's instructions name. Otherwise use `~/.openclaw/sim/` on OpenClaw, shared by every agent on the machine, and `.sim/` at the project root in other agents. Create the folder and its `index.md` on first use.

- `index.md`: one line per note with its status, what it covers and the date of its last attempt.
- `P-NNN-<slug>.md`: one note per recurring problem.

## Before a change

1. Read `index.md`, then search the notes for the symptom, component and error text, for example `grep -ril "<term>" <memory folder>`.
2. If a note explains the current failure, read its attempts. Check the agent, model and version behind each one before reusing it. Retry a direction that already failed only when new evidence justifies it.
3. If none fits, create the next `P-NNN-<slug>.md` from the template below.
4. Append the new attempt with **What**, **Why** and **Predicted** filled in. Write the prediction before testing.

## After validation

Fill **Observed** in the same attempt: what was fixed, what was missed, the evidence (test, run id, log line) and whether the change stayed or was reverted. Set `status` to `resolved` only when the evidence shows it. If the change is later replaced, add a new attempt; never edit or delete earlier ones.

Every time you create a note or add or complete an attempt, update that note's line in `index.md` in the same change. A note missing from the index is an incomplete change.

## Note template

```markdown
---
id: P-NNN
name: <one-line root-cause hypothesis>
status: open | resolved | parked
opened: YYYY-MM-DD
aliases: []
---

## Attempt YYYY-MM-DD <short title>
- **Who:** <agent, session or person>; model and version if known
- **What:** <change and files>
- **Why:** <rationale>
- **Predicted:** <what should be fixed, and how it will be checked>
- **Observed:** <filled after validation: fixed / missed / evidence>
- **Kept:** yes | reverted | replaced by <attempt>
- **Links:** <backup, report, commit, PR>
- **Backfilled:** no
```

Set **Backfilled** to `yes` for attempts reconstructed later from reports or logs.

## Index template

```markdown
# Self-Improvement Memory

| Note | Status | What it covers | Last attempt |
| --- | --- | --- | --- |
| [P-001](P-001-<slug>.md) | open | <one line> | YYYY-MM-DD |
```

## Rules

- Append only. To merge two problems, add the old id to `aliases` of the surviving note and keep both histories.
- Link evidence (backups, reports, commits); do not copy logs or other files' contents.
- Never write secrets, tokens or personal data.
- Read on demand with search; do not load the whole memory into context.
