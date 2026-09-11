## Description:

A dependency-free Python tool that tracks a numeric goal and a date-based budget guard, printing a one-line reminder with an exit code an agent or script can branch on.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulscode](https://clawhub.ai/user/paulscode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create and check a local reminder state file for numeric milestones, deadline proximity, and daily spend-cap triggers. It is useful when an agent workflow needs a simple branchable signal without network calls, credentials, or background services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The command can create, overwrite, or update a local JSON state file, including when --force or update flags are used.

Mitigation: Run it with an explicit --state path in an intended project location and review before using --force or mutating check flags.

Risk: The reminder is not an accounting integration or scheduled monitor.

Mitigation: Use it as a local reminder signal and have the calling agent or scheduler invoke check at the desired cadence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulscode/skills/founder-ledger-tracker)
- [Publisher profile](https://clawhub.ai/user/paulscode)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON]

**Output Format:** [Plain text reminders, process exit codes, and local JSON state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a caller-selected local JSON state file; check exits 0, 1, or 2 for branchable automation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
