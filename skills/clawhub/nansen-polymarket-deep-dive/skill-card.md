## Description:

Guides a deep dive into a specific Polymarket market using Nansen market data, including prices, order books, holders, trades, and PnL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to examine a specific Polymarket market's price history, order book, holders, positions, trades, and PnL through Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nansen API keys or browser sessions can authorize account-level API access.

Mitigation: Use only a Nansen account and credentials you intend to authorize; check authentication status before research.

Risk: Research calls may spend wallet funds under existing payment authorization and spending limits.

Mitigation: Confirm wallet authorization and spending limits before running calls or loops.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-deep-dive)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Analysis]

**Output Format:** [Markdown with bash command examples and market analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a numeric market ID; covers OHLCV, order book, holders, positions, trades, and PnL.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
