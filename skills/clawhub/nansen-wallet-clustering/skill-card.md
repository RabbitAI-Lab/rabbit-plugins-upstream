## Description:

Helps agents cluster and attribute related blockchain wallets using funding chains, shared signers, and counterparty patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to trace wallet relationships and assess possible common ownership across supported chains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls, loops, and traces can consume credits or trigger permitted wallet payments.

Mitigation: Confirm authentication and payment limits before calls; bound loops and trace width, and ask before expanding to new wallets.

Risk: Weak wallet-link signals can lead to incorrect ownership attribution.

Mitigation: Use multiple independent signals, report confidence, and exclude ENS-only, single-withdrawal, or single-deployer matches.

## Reference(s):

- [Nansen Wallet Clustering release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-clustering)
- [Wallet Attribution Reference](artifact/REFERENCE.md)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with wallet attribution tables and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet addresses, proposed owners, confidence levels, supporting signals, and roles]

## Skill Version(s):

0.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
