## Description:

Helps analyze a wallet's identity, holdings, trading performance, recent transactions, perpetual positions, and counterparties with Nansen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to investigate a wallet's labels, balances, profit and loss, recent activity, open perpetual positions, and counterparties through Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, especially in loops, can consume credits or trigger authorized x402 payments.

Mitigation: Review available credits, wallet authorization, payment policy, and spending limits before running calls or loops.

Risk: Cached authentication status may not prove that a selected credential is usable.

Mitigation: Check authentication status before research and stop on anonymous selection or authentication failures rather than retrying anonymously.

## Reference(s):

- [Nansen Wallet Deep Dive on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-deep-dive)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet analysis depends on a selected Nansen API key or saved browser session and available account entitlements.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
