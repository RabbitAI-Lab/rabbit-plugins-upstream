## Description:

Near-expiry conviction trading on Polymarket. The skill scans markets in their final minutes, filters for strongly-skewed splits (60/40+), and places bounded trades against the under-priced side. Defaults — $10 max per trade, 5 trades/run, 8-minute expiry window, dry-run unless `--live`.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and traders use this skill to scan near-expiry Polymarket markets, configure bounded strategy parameters, inspect account status, and optionally execute live trades through the Simmer SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Managed defaults and strategy wording conflict in ways that could cause unintended real-money trades.

Mitigation: Keep dry-run enabled first, manually confirm the effective $10 max trade, 8-minute expiry, and 0.60 split settings, and enable live trading only after reviewing the resolved configuration.

Risk: Live mode can place irreversible on-chain Polymarket orders when wallet credentials are available.

Mitigation: Do not provide a wallet private key unless live trading is intended, keep position sizing conservative, and rely on preflight checks before order placement.

Risk: The default strategy is a template and has not been validated to produce profitable results.

Mitigation: Run paper or dry-run mode for an extended period, review market selection and fees, and treat the strategy as user-owned trading automation rather than financial advice.

## Reference(s):

- [Strategy attribution thread](https://x.com/mert/status/2020216613279060433)
- [Simmer API](https://api.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Simmer V2 migration guide](https://docs.simmer.markets/v2-migration)
- [Polymarket CLOB API](https://clob.polymarket.com)
- [Polymarket fee documentation](https://docs.polymarket.com/trading/fees)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration values, and trading-status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Simmer API key; live trading requires explicit `--live` use and may require wallet credentials.]

## Skill Version(s):

1.3.6 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
