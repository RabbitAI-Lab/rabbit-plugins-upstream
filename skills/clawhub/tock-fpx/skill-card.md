## Description:

Queries Tock restaurant listings, availability, and signed-in reservation history from the shell through a paired browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Tock users can discover restaurants, inspect bookable dates, and view their own reservations without running a separate MCP server. The skill does not book or cancel reservations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paired browser extension can access exploretock.com through the user's browser session.

Mitigation: Install and pair it only if comfortable granting that site access, and review the extension before use.

Risk: Reservation and profile results, including temporary files, may expose names, email addresses, and reservation history.

Mitigation: Treat outputs as sensitive, limit sharing, and remove temporary files when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Tock request recipes](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Text or JSON with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; signed-in reservation and profile responses may contain personal information.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
