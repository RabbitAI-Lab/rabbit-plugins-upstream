## Description:

This skill uses the OKX CLI to inspect account balances, positions, P&L, transaction history, fees, and account settings, and to transfer funds or change position mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX account holders use this skill to review balances, assets, positions, P&L, fees, and account activity, and to manage account transfers or position mode through the CLI. It requires configured OKX API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags no-confirmation command guidance and reports that its analysis is incomplete.

Mitigation: Review command behavior before installation. Confirm live or demo mode and the exact details before transfers or position-mode changes.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/okx-retail/skills/okx-cex-portfolio)
- [Publisher profile](https://clawhub.ai/user/okx-retail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with CLI command examples and account data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured OKX credentials; command results should identify live or demo mode.]

## Skill Version(s):

1.5.1 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
