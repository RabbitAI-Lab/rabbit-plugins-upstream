## Description:

Helps browse Polymarket prediction markets to find trending events, top markets by volume, and specific markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Prediction-market analysts and other users browse Polymarket events, search markets, and compare volume, liquidity, and open interest through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls may consume credits or trigger wallet-backed payments, especially when repeated in loops.

Mitigation: Review payment settings and spending limits before running calls; keep queries and loops bounded.

Risk: Research requires an API key or saved browser session with appropriate account permissions.

Mitigation: Confirm the selected authentication state before research and stop if authentication fails; do not retry anonymously.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-prediction-markets)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands and market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market screeners can include volume, liquidity, open interest, and trader activity.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
