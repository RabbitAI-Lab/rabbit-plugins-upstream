## Description:

Helps agents search Resy restaurants, check availability, and manage reservations, favorites, and Priority Notify using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders and developers can use this skill to find restaurants and available tables, book or cancel reservations, and manage favorites and Priority Notify without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, cancellation, favorite, and notify requests change a live Resy account without an enforced confirmation step.

Mitigation: Before each write, show and confirm the venue, date, time, party size, reservation or notify identifier, and payment method as applicable; check the account afterward.

Risk: Resy credentials and account tokens may be exposed through shared scripts or logs.

Mitigation: Treat RESY_PASSWORD and RESY_TOKEN as secrets; avoid including their values in shared logs or scripts.

## Reference(s):

- [Resy API request examples](references/resy-api.md)
- [resy-fpx on ClawHub](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-only lookups and commands that change a live Resy account.]

## Skill Version(s):

1.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
