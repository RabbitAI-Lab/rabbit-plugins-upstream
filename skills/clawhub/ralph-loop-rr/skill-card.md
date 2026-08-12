## Description:

Ralph Loop is an autonomous task execution discipline that has an agent create a persistent plan, execute multi-step tasks to completion, update progress, and send Telegram status messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[roboticresults](https://clawhub.ai/user/roboticresults)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators can use this skill to make an agent run a planned multi-step task autonomously, track progress in a temporary markdown memory file, and provide concise progress notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives the agent broad self-directed authority for multi-step work with limited pause points.

Mitigation: Use it only when autonomous execution is intentional, scope the task clearly, and keep approval checkpoints for commands, network access, credential handling, and destructive changes.

Risk: The skill sends Telegram progress details without clear opt-in, recipient scope, or task boundaries.

Mitigation: Confirm the Telegram destination before use and avoid sensitive tasks, filenames, credentials, or private content in progress messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/roboticresults/skills/ralph-loop-rr)
- [Publisher profile](https://clawhub.ai/user/roboticresults)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Text]

**Output Format:** [Markdown guidance, temporary markdown progress files, command execution, and short Telegram status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to delete its temporary progress file on completion.]

## Skill Version(s):

1.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
