## Description:

Provides agent guidance for using the OKX CLI to inspect OKX account balances, asset snapshots, positions, P&L, bills, fees, account configuration, withdrawal capacity, fund transfers, and position mode changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer OKX portfolio and account-management questions, including total holdings, balances, positions, P&L, account activity, fees, and internal account transfers. It is intended for credentialed OKX CLI sessions with explicit live or demo mode handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive OKX account balances, positions, account configuration, and transaction data through authenticated CLI output.

Mitigation: Use demo mode first, avoid sharing raw configuration or account output unnecessarily, and never collect credentials in chat.

Risk: The skill includes account-affecting actions such as transfers and position mode changes, which can affect real funds when used in live mode.

Mitigation: Confirm live versus demo mode before execution, verify source balances and transfer details, and use least-privilege OKX API keys with withdrawals disabled and IP restrictions where possible.

Risk: The release depends on installing an external npm CLI package for OKX account access.

Mitigation: Verify the installed npm package and version match @okx_ai/okx-trade-cli@1.3.7 before use.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub release page](https://clawhub.ai/numpy0001/skills/okx-cex-portfolio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and occasional JSON output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OKX CLI credentials and live/demo mode confirmation for account-affecting commands.]

## Skill Version(s):

1.3.8 (source: ClawHub release metadata; artifact frontmatter and npm package reference 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
