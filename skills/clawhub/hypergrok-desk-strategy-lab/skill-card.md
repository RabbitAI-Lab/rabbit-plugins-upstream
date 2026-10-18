## Description:

Helps users turn their trading ideas into explicit rules, test them against Hyperliquid market history, and paper-trade them on testnet without placing live orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and researchers use this skill to formalize their own trading ideas, inspect verified historical data, review backtests with costs and uncertainty, and evaluate proposals through testnet paper trading. It does not recommend trades or place orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete history or overly optimistic assumptions can make a backtest misleading.

Mitigation: Verify data coverage, keep an untouched holdout, and report costs, drawdown and trial counts; treat results as research, not investment advice.

Risk: Paper-trade proposals could be mistaken for permission to execute live trades.

Mitigation: Keep execution on testnet with user approval and risk review; do not place orders or run unattended execution.

## Reference(s):

- [HyperGrok Desk Strategy Lab on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-strategy-lab)

## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Markdown reports and Python backtest code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-defined rules, dataset notes, backtest results and testnet signal proposals; no live orders.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
