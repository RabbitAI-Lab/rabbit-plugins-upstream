## Description:

Helps agents search Resy restaurants, check availability, and manage reservations, favorites, and Priority Notify from a shell using direct API requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy users and developers can search restaurants, check available tables, and manage their own reservations and alerts through shell commands without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials or reservation tokens may be exposed through logs or shared terminals.

Mitigation: Keep credentials and RESY_TOKEN out of logs and avoid shared terminals.

Risk: Booking, cancellation, favorites, and notification commands change live account state.

Mitigation: Require explicit confirmation before each account-changing action and verify the result.

## Reference(s):

- [Resy API request examples](references/resy-api.md)
- [resy-fpx ClawHub release](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can query live availability or change the user's Resy account.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
