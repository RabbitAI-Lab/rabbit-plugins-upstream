## Description:

Guides agents to search Resy restaurants, check availability, manage reservations and favorites, and set Priority Notify alerts from a shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders and developers use this skill to search restaurants, inspect available tables, and manage reservations, favorites, and Priority Notify alerts through an agent-assisted shell workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may expose Resy credentials or account tokens while following authentication instructions.

Mitigation: Keep credentials and tokens out of logs and shared shell history; review token access before installation.

Risk: Booking, cancellation, favorites, and notify commands change the user's live Resy account without a built-in dry run.

Mitigation: Read back the target account state and obtain explicit confirmation before booking, cancellation, or removal; verify the result afterward.

## Reference(s):

- [Resy API request guide](artifact/references/resy-api.md)
- [resy-fpx ClawHub listing](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes instructions for actions that can change a live Resy account.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
