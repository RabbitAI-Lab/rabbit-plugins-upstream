## Description:

Manages long-running goals across turns, sessions, and context compaction by maintaining a single persistent goal.md with sub-goals, checkpoints, decisions, and evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, operators, writers, planners, and troubleshooting teams use this skill to keep long-running work anchored to a durable goal.md instead of relying on chat memory or summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists project state in goal.md, which may retain sensitive or private details across sessions if users place them there.

Mitigation: Review the selected goal.md path and avoid storing secrets or sensitive private details unless that persistence is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzusp/skills/long-goal)
- [goal-template.md](assets/goal-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown updates to goal.md with optional shell commands for validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a persistent, user-visible goal.md and validates its structure with scripts/validate_long_goal.py.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
