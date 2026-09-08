## Description:

Trade Kalshi weather markets using NOAA forecasts via Simmer SDK and DFlow on Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure, dry-run, and optionally execute automated Kalshi weather-market trades based on NOAA forecasts, Simmer SDK market data, and DFlow execution. It also supports account status checks and trading-parameter tuning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode can place real on-chain trades using a raw Solana private key, and those trades may be irreversible.

Mitigation: Use dry-run mode first, keep funds in a dedicated low-balance wallet, and store SIMMER_API_KEY and SOLANA_PRIVATE_KEY only in secured environment storage.

Risk: Safety controls may be under-scoped or fail open, especially if safeguards are disabled or automation is scheduled before review.

Mitigation: Avoid --no-safeguards for live runs, review automatic market-import behavior, and delay scheduled automation until live-trading behavior is understood.

Risk: Weather-market stop-loss behavior may not cap losses when markets resolve quickly or gap at resolution.

Mitigation: Use conservative position sizing, set low per-trade limits, and assume a full position can go to zero.

## Reference(s):

- [Kalshi Weather Trader on ClawHub](https://clawhub.ai/simmer/skills/kalshi-weather-trader)
- [Skill Disclaimer](DISCLAIMER.md)
- [Simmer API](https://api.simmer.markets)
- [NOAA Weather API](https://api.weather.gov)
- [DFlow Proof KYC](https://dflow.net/proof)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce dry-run analysis, live-trading commands, account-status checks, and environment-variable configuration guidance.]

## Skill Version(s):

1.0.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
