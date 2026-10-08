## Description:

Guides agents through searching Resy availability and managing reservations, favorites, and Priority Notify from a shell without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Resy account holders can use this skill to find restaurant availability and manage their own reservations, favorites, and notifications through shell commands without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resy passwords and account tokens may be exposed through logs or shared files.

Mitigation: Treat RESY_PASSWORD and RESY_TOKEN as sensitive; use a trusted shell and avoid recording tokens in logs or shared files.

Risk: Booking or cancellation commands can change real reservations, including use of a saved payment method.

Mitigation: Manually confirm the venue, date, party size, payment method, and reservation token before booking or canceling; read back reservations afterward.

## Reference(s):

- [Resy API request examples](references/resy-api.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may access account data or change live reservations and notifications.]

## Skill Version(s):

1.3.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
