## Description:

Enables an agent to operate TimeCamp through an OOMOL-connected account for reading users, tasks, timers, and time entries, and for creating or updating time-tracking records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect TimeCamp account data and manage time-tracking workflows such as starting timers, stopping timers, creating time entries, and updating existing entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run mutable remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing; prefer a signed or version-pinned oo CLI channel, or download and inspect the installer before running it.

Risk: Write actions can create, start, stop, or update TimeCamp records.

Mitigation: Confirm the exact write-action payload and expected effect with the user before execution.

## Reference(s):

- [TimeCamp homepage](https://www.timecamp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub TimeCamp skill page](https://clawhub.ai/oomol/skills/oo-timecamp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live TimeCamp connector schemas before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
