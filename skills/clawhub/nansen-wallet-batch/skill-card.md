## Description:

Batch-profile wallet addresses with Nansen to identify smart-money and fund labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use the Nansen CLI to profile lists of wallet addresses and identify wallets labeled as smart money or funds, optionally checking balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch calls may consume credits or trigger authorized x402 payments, including within loops.

Mitigation: Confirm the selected API key or browser session and review wallet payment policy and spending limits before running a batch.

Risk: Invalid addresses can produce per-address errors rather than usable profiles.

Mitigation: Check each result for an error and skip invalid addresses.

## Reference(s):

- [Nansen Wallet Batch on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-batch)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports smart-money or fund-labeled addresses; optional balances and per-address errors are available.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
