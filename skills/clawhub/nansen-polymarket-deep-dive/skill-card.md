## Description:

Examines a specific Polymarket market using price history, order book, holder positions, trades, and PnL data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to investigate pricing, liquidity, holdings, trading activity, and profit or loss in a specific Polymarket market.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls may use credits or trigger wallet-authorized x402 payments, including once per call in a loop.

Mitigation: Review wallet spending limits and expected per-call costs before running commands or loops.

Risk: Research may fail or use the wrong access path if authentication is missing or expires.

Mitigation: Check the selected authentication state first; stop on failures rather than switching to anonymous paid access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-deep-dive)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with market analysis and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Nansen CLI and authenticated access; market identifiers are numeric.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
