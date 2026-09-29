## Description:

Query Tock metros, restaurants, venue availability, and your reservations from a shell through a browser session without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find Tock restaurants and availability or read an authorized account's reservations through the fpx CLI. Booking and cancellation remain on Tock's website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI and browser extension can access the signed-in Tock session.

Mitigation: Install only if comfortable granting this access; use account-specific commands only for accounts you own or are authorized to access.

Risk: Saved reservation responses may contain names, email addresses, and booking details.

Mitigation: Avoid retaining or sharing response files; delete temporary files after use.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock queries; reservations and account identity require an authorized signed-in browser session.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
