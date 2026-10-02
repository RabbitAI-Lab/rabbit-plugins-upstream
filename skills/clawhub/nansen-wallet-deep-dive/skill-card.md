## Description:

Guides an agent through Nansen wallet research covering identity labels, balances, trading performance, recent transactions, perpetual positions, and counterparties.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet researchers and developers use this skill to review a wallet's identity, holdings, trading activity, open perpetual positions, and counterparties through Nansen.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated research calls can incur x402 payments under existing wallet authorization.

Mitigation: Review wallet authorization, payment policy, and spending limits before running calls or loops.

Risk: Research requires a selected Nansen API key or saved browser session.

Mitigation: Check authentication status first and stop if the selected credential is absent, invalid, or fails renewal; do not fall back to anonymous access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-deep-dive)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands]

**Output Format:** [Markdown with shell commands and wallet research findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Perpetual-position results cover Hyperliquid and may be empty when no positions are open.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
