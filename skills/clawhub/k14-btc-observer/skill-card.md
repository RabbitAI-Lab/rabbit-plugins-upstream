## Description:

Observe Binance BTCUSDT K14 signals and public Polymarket feeds; test managed runtime and checkpoint persistence without trading.

This skill is for research and development only.

## Publisher:

[l337-krew-cs](https://clawhub.ai/user/l337-krew-cs)

### License/Terms of Use:

All rights reserved (custom terms)

## Use Case:

Developers and engineers use the observer to inspect BTC K14 signal candidates and public Polymarket feed health, and to assess managed-run and checkpoint behavior without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unused simmer-sdk dependency is unpinned.

Mitigation: Review the dependency and its source/version before installation.

Risk: Bundled thresholds apply only to October 2026; later runs are blocked until thresholds are separately validated.

Mitigation: Check the threshold month and supply a separately validated threshold file before running in a later month.

Risk: A directional signal candidate is not a complete entry decision, and the observer does not simulate fills or profits.

Mitigation: Treat the output as observation evidence only; assess fair value, liquidity, execution, position accounting, and exits separately.

Risk: Local checkpoints cannot prevent duplicate runs on isolated runner filesystems, and a declared schedule does not prove a cloud runner is active.

Mitigation: Use a dedicated persistent checkpoint directory when enabling recurring runs, and verify actual run reports and storage behavior.

## Reference(s):

- [Binance API: Server Time](https://api.binance.com/api/v3/time)
- [Binance API: Kline/Candlestick Data](https://api.binance.com/api/v3/klines)
- [Polymarket Gamma API: Markets](https://gamma-api.polymarket.com/markets)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON Lines with a final AUTOMATON_REPORT summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public market observations, a directional K14 candidate, feed health metrics, and run/checkpoint evidence; no orders, fills, or profits are produced.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
