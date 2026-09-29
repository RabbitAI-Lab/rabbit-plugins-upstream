## Description:

Profiles a Hyperliquid perpetual-futures trader's identity, open positions, recent trades, and overall PnL using the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and analysts use this skill to research a Hyperliquid trader's labels, current positions, recent trades, PnL, and leaderboard standing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, including repeated calls, may spend Nansen credits or trigger wallet payments.

Mitigation: Review credits, wallet payment policy, and spending limits before authorizing the workflow.

Risk: The agent can use the selected Nansen CLI authentication for account API research.

Mitigation: Use only an explicitly selected key or browser session and stop if authentication or renewal fails; do not fall back to anonymous paid access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-perp-trader-profile)
- [Nansen CLI browser-login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes trader labels, positions, recent trades, PnL, and leaderboard standing from Nansen CLI results.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
