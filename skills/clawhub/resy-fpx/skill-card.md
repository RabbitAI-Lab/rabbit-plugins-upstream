## Description:

Guides agents through searching Resy availability and managing reservations, favorites, and Priority Notify with shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Resy account holders use this skill to find restaurant openings and manage reservations, favorites, and Priority Notify from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resy credentials or account tokens could be exposed through shell history or logs.

Mitigation: Keep credentials and tokens secret, and avoid logging or sharing them.

Risk: Booking, cancellation, and notification commands make live changes to a Resy account.

Mitigation: Confirm the venue, date, party size, and reservation tokens before executing a write command.

## Reference(s):

- [Resy API request guide](references/resy-api.md)
- [Resy FPX on ClawHub](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can query Resy or change a signed-in account's reservations and notifications.]

## Skill Version(s):

1.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
