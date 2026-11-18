## Description:

Check a Mac used as a work computer: memory pressure, CPU load, disk use, startup items, app leftovers, backup state. Read-only commands, cleanup only as proposals with a rollback, deletes only to the Trash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[korbenzhang](https://clawhub.ai/user/korbenzhang)

### License/Terms of Use:

MIT-0

## Use Case:

Mac owners and their agents use this skill to investigate performance, storage, startup, and backup concerns with read-only measurements. It helps turn current measurements into cleanup proposals with explicit risks, rollback steps, and owner approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial: some local references could not be resolved, so its evidence is incomplete.

Mitigation: Review the skill's requested checks and limits before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/korbenzhang/skills/macos-health-check)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with shell command blocks and numbered cleanup proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only measurements; changes require per-action approval and removals go to the Trash.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
