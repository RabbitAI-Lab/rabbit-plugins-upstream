## Description:

Check a Mac used as a work computer: memory pressure, CPU load, disk use, startup items, app leftovers, backup state. Read-only commands, cleanup only as proposals with a rollback, deletes only to the Trash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holgergruenhagen](https://clawhub.ai/user/holgergruenhagen)

### License/Terms of Use:

MIT-0

## Use Case:

Mac owners and support agents use this skill to assess a work Mac's performance, storage, startup items, app leftovers, and backup state, then review measured cleanup proposals with risks and rollback steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The benign scan has medium confidence and partial coverage, with several local path-like references unresolved.

Mitigation: Review those references in the skill source and account for the scan's stated uncertainty before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/holgergruenhagen/skills/macos-health-check)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes measured findings, cleanup proposals with risks and rollback steps, and a short log format.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
