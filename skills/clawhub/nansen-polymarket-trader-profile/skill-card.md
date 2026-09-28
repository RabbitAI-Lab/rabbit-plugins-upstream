## Description:

Analyzes a Polymarket wallet's trades, profit and loss, and market context using the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to review a Polymarket trader's activity, positions, and profit and loss across resolved and unresolved markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls may consume credits or trigger wallet-funded x402 payments, including repeated calls.

Mitigation: Review the wallet payment policy and spending limits before running research commands or loops.

Risk: The workflow requires access to a Nansen API key or saved browser session.

Mitigation: Use the skill only with a trusted Nansen CLI installation and an explicitly selected authenticated session or key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-trader-profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet trade history, market context, and profit-and-loss assessment]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
