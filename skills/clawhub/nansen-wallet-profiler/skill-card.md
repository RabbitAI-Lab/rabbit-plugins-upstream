## Description:

Guides wallet research with Nansen profiler commands for balances, PnL, labels, transactions, counterparties, tracing, and comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet researchers and developers use this skill to inspect wallet activity, identity, performance, and relationships or compare multiple wallets through Nansen CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, especially batch, trace, and looped calls, can consume credits or trigger x402 payments under existing wallet authorization.

Mitigation: Review the intended call volume and wallet spending limits before running multi-call workflows.

Risk: A configured API key or saved browser session can be used for Nansen CLI calls.

Mitigation: Select an intended credential and check authentication status before research; stop on authentication failure rather than switching to anonymous access.

## Reference(s):

- [Nansen Wallet Profiler on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-profiler)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers authentication, command flags, and paid-call precautions.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
