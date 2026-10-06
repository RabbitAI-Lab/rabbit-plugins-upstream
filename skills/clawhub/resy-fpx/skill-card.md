## Description:

Guides agents in searching Resy venues, checking availability, and managing reservations, favorites, and Priority Notify from a shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy users and developers can search restaurants, inspect reservation availability, and manage their own bookings, favorites, and notifications through shell commands without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, cancellation, favorite, and notification commands can change a live Resy account without a built-in confirmation step.

Mitigation: Require manual confirmation of the account, venue, date, and intended action before running any account-changing command.

Risk: Credentials, authentication tokens, and access to a signed-in browser session can expose private reservation data or enable unauthorized actions.

Mitigation: Treat credentials, tokens, and browser-session access as secrets; avoid sharing or logging them and restrict access to the account owner.

## Reference(s):

- [Resy API request examples](references/resy-api.md)
- [resy-fpx on ClawHub](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve reservation details or change a live Resy account.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
