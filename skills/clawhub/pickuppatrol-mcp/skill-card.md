## Description:

Read and change children's school dismissal plans on PickUp Patrol from a shell with curl, including students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and parents with authorized PickUp Patrol accounts use this skill to script reads and carefully verified updates to student dismissal plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change live child dismissal plans.

Mitigation: Use only accounts you control, replace all example IDs and dates, inspect each write payload, and re-read PickUp Patrol fields after every update.

Risk: Session cookies and authentication artifacts may remain in local temporary files.

Mitigation: Avoid shared machines and delete /tmp/pup_* files and cookie jars after use.

Risk: Repeated rejected logins can count against the account and may trigger lockout.

Mitigation: Stop after one failed login attempt and correct credentials before trying again.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can read account data and write live dismissal plans; verify changes with follow-up reads.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
