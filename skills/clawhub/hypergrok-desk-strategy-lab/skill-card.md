## Description:

Helps users turn their own trading ideas into explicit rules, test them against Hyperliquid market history, and paper-trade them on testnet without recommending trades or promising returns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Traders and researchers use the skill to specify their own strategy rules, assess backtests with costs and holdout data, and review testnet paper-trading proposals before deciding whether an idea merits further testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backtest results may be mistaken for reliable trading signals or expected returns.

Mitigation: Treat results as tests of user-supplied ideas; document fees, slippage, trial counts, holdout results, and uncertainty before drawing conclusions.

Risk: Paper-trading workflows may be used with real credentials or connected to unattended execution.

Mitigation: Keep mainnet credentials and real orders outside this skill unless separately reviewed and explicitly controlled; require user approval and use testnet for paper trades.

## Reference(s):

- [HyperGrok Desk Strategy Lab on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-strategy-lab)

## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Markdown reports and rules, Python backtest code, and testnet trade proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents data requests, assumptions, costs, trial counts, and rejected ideas; does not place orders.]

## Skill Version(s):

1.5.0 (source: ClawHub release; bundled skill metadata says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
