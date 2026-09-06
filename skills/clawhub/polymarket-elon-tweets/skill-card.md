## Description:

Trade Polymarket "Elon Musk # tweets" markets using XTracker post count data, buying adjacent range buckets when combined cost is below the configured threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-tool operators use this skill to inspect XTracker tweet-count signals, configure Polymarket bucket-trading parameters, run dry-run scans, and optionally execute live trades through Simmer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place live trades with real funds.

Mitigation: Start in dry-run or paper mode, verify settings and market behavior, and use a small dedicated wallet before enabling live trading.

Risk: Wallet-key handling is sensitive when an external wallet private key is used.

Mitigation: Prefer managed-wallet flows when suitable; otherwise keep any private key in a dedicated secret store or environment, never paste it into prompts, and limit funds in the wallet.

Risk: Safeguards can be bypassed and managed defaults may allow larger exposure than local documentation examples.

Mitigation: Keep safeguards enabled, do not use --no-safeguards for live trading, and manually set conservative position, sizing, trade-count, exit, and slippage limits.

Risk: Fast market moves, signal lag, or resolution timing can prevent exits before losses occur.

Mitigation: Treat position sizing as the primary control, monitor open positions, and avoid scaling until performance is observed over an extended dry-run period.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-elon-tweets)
- [Simmer publisher profile](https://clawhub.ai/user/simmer)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Simmer V2 migration guide](https://docs.simmer.markets/v2-migration)
- [DISCLAIMER.md](DISCLAIMER.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose dry-run or live trading commands, environment variables, and risk-limit settings for the user's agent session.]

## Skill Version(s):

1.3.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
