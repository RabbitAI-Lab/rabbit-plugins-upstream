## Description:

Profiles a Hyperliquid perpetual-futures trader's identity, open positions, recent trades, and overall PnL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and analysts use this skill to review a Hyperliquid perp trader's positions, recent trades, PnL, and leaderboard standing with Nansen.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls may consume credits or trigger configured x402 wallet payments, including repeated calls.

Mitigation: Review payment policies and wallet spending limits before running research commands or loops.

Risk: Research requires an authenticated Nansen API key or saved browser session; authentication failures can interrupt the workflow.

Mitigation: Check authentication before research and stop on failed or uncertain authentication rather than switching to anonymous access.

Risk: The skill requires installation of the nansen-cli package.

Mitigation: Review the package's trust before installing it.

## Reference(s):

- [Nansen Perp Trader Profile on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-perp-trader-profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cross-references positions, recent trades, and leaderboard standing.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
