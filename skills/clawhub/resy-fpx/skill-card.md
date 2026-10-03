## Description:

Guides agents through searching Resy availability and managing reservations, favorites, and Priority Notify from a shell using authenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders and developers use this skill to find restaurant availability and manage bookings, favorites, and Priority Notify without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resy credentials and tokens could be exposed in shared logs, shell history, commits, or screenshots.

Mitigation: Keep RESY_EMAIL, RESY_PASSWORD, and RESY_TOKEN out of shared outputs and stored history.

Risk: Booking, cancellation, favorite, and notification commands change a real Resy account.

Mitigation: Review each account-changing command before execution and verify the resulting account state.

## Reference(s):

- [Resy API request examples](references/resy-api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated actions can change live account state.]

## Skill Version(s):

1.3.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
