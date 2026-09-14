## Description:

Trades Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts through the Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure, dry-run, and optionally execute automated Polymarket weather-trading strategies based on forecast-to-market price differences. It is also used to inspect positions, tune trading thresholds, and test strategies in the Simmer paper venue before any live run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an SDK that receives API keys, optional wallet private keys, and live trading authority.

Mitigation: Review before installing, pin or verify the simmer-sdk version, and avoid exposing a primary wallet private key in the process environment.

Risk: Live mode can place real-money orders, and on-chain trades cannot be recalled.

Mitigation: Use dry-run mode or the SIM paper venue first, require explicit live-mode opt-in, and keep dashboard trade and daily limits low.

Risk: Weather temperature markets can gap at resolution, leaving no practical stop-loss exit even when monitoring is enabled.

Mitigation: Size positions conservatively and assume any position can go to zero.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/polymarket-weather-trader)
- [Simmer Wallet Setup](https://docs.simmer.markets/wallets)
- [Simmer API](https://api.simmer.markets)
- [Skill Documentation](SKILL.md)
- [Disclaimer](DISCLAIMER.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run opportunity analysis, position/status summaries, and live-trading commands when explicitly requested.]

## Skill Version(s):

1.23.10 (source: evidence release, SKILL.md frontmatter, CHANGELOG, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
