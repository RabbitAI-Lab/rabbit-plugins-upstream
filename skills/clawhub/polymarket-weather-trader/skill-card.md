## Description:

Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scan Polymarket weather markets, compare forecast sources, configure trading thresholds, and optionally execute weather-market trades through Simmer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode can place real orders and move funds.

Mitigation: Run in dry-run mode or set TRADING_VENUE=sim until the strategy and account setup are understood; use --live only as an explicit opt-in.

Risk: Trading protections can be disabled or fail open.

Mitigation: Avoid --no-safeguards for live trading, keep conservative position limits, and review safeguard output before scaling beyond defaults.

Risk: Raw wallet private keys increase custody risk.

Mitigation: Prefer managed or delegated wallet handling where available; protect WALLET_PRIVATE_KEY if external-wallet self-custody is required.

Risk: Dependency behavior affects real-money execution.

Mitigation: Pin or review simmer-sdk before using real funds.

## Reference(s):

- [Simmer wallet setup documentation](https://docs.simmer.markets/wallets)
- [Simmer SDK API](https://api.simmer.markets)
- [Simmer V2 migration guide](https://docs.simmer.markets/v2-migration)
- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-weather-trader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe dry-run opportunities, live-trading actions, account status, positions, and safeguard decisions.]

## Skill Version(s):

1.23.8 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
