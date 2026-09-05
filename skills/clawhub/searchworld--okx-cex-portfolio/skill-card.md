## Description:

Guides an agent in using the OKX CLI to inspect account balances, positions, P&L, bills, fees, withdrawal capacity, transfers, and position mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query OKX account balances, portfolio snapshots, open and closed positions, account bills, fees, account configuration, withdrawal limits, and account transfers through the OKX CLI after credential setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses persistent OKX exchange credentials.

Mitigation: Use a dedicated OKX sub-account or least-privilege API key, configure credentials through the OKX CLI instead of chat, and never paste credentials into the agent conversation.

Risk: The npm installation path may download helper executables.

Mitigation: Install only if the OKX CLI package is trusted and review the package before installation.

Risk: Live transfers and position-mode changes can affect real accounts.

Mitigation: Start in demo mode and require explicit confirmation before any live transfer or position-mode change.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-portfolio)
- [Publisher profile](https://clawhub.ai/user/searchworld)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command blocks and concise status notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-output flags for OKX CLI commands; command responses should state whether live or demo mode was used.]

## Skill Version(s):

1.4.5 (source: artifact frontmatter metadata.version and server release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
