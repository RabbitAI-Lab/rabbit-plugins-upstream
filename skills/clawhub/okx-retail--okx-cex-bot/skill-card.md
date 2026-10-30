## Description:

Manage OKX Grid, Spot and Contract DCA, and Smart Portfolio bots, including creation, monitoring, amendments, and stops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX account holders use this skill to create, monitor, amend, and stop Grid, DCA, and Smart Portfolio bots through the OKX CLI. It supports bot information requests and confirmed trading changes in live or demo mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account checks may expose saved API credentials to agent output.

Mitigation: Start in demo mode and ensure account-check output is redacted before using saved API-key profiles.

Risk: Live bot changes affect investments, leverage, or margin, and server-side bots continue running until stopped.

Mitigation: Review investment, leverage, margin, and stop behavior carefully; confirm write actions and verify their results.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/okx-retail/skills/okx-cex-bot)
- [Grid bot commands](references/grid-commands.md)
- [DCA bot commands](references/dca-commands.md)
- [Smart Portfolio bot commands](references/smart-portfolio-commands.md)
- [Bot workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated bot queries and trading changes; write actions require user confirmation.]

## Skill Version(s):

1.5.0 (source: skill frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
