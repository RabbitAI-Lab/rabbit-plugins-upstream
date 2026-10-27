## Description:

Helps agents review OKX account balances, positions, P&L, fees, and transaction history, and guide confirmed fund transfers or position-mode changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX account holders and their agents use this skill to check holdings, balances, open or closed positions, fees, and account activity, and to prepare user-approved transfers or account-setting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account balances and positions are sensitive financial data.

Mitigation: Grant OKX CLI account access only when needed, and never paste credentials into chat.

Risk: A live-mode transfer or position-mode change can affect real funds or account behavior.

Mitigation: Try demo mode first; confirm the mode and transfer details or new position mode before executing.

## Reference(s):

- [OKX CEX Portfolio on ClawHub](https://clawhub.ai/okx-retail/skills/okx-cex-portfolio)
- [OKX](https://www.okx.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with account summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies live or demo mode in command responses; requires confirmation before transfers or position-mode changes.]

## Skill Version(s):

1.4.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
