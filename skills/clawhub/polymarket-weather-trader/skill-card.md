## Description:

Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scan Polymarket weather markets, compare market pricing against weather forecasts, simulate trades by default, and optionally execute bounded live weather-market trades after setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports that live trades may proceed when market-risk context cannot be checked.

Mitigation: Review before installing, start with dry-run or the sim venue, keep trade caps very low, and use an exact reviewed simmer-sdk version before enabling live trading.

Risk: Live mode can place real on-chain orders that cannot be recalled.

Mitigation: Require explicit --live use, keep SIMMER_WEATHER_MAX_POSITION_USD conservative, and confirm wallet, venue, and dashboard limits before running with real funds.

Risk: Weather temperature markets can resolve by gapping to near zero, so stop-loss monitoring may not cap losses.

Mitigation: Size positions for the full possible loss, use paper mode for an extended period first, and avoid relying on stop-loss behavior as the primary risk control.

Risk: The skill depends on sensitive SIMMER_API_KEY and optional WALLET_PRIVATE_KEY values.

Mitigation: Isolate credentials in a dedicated environment, avoid sharing logs or shells that expose them, and use managed-wallet or paper-mode paths where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-weather-trader)
- [Simmer wallet setup](https://docs.simmer.markets/wallets)
- [Simmer API](https://api.simmer.markets)
- [Simmer Polymarket V2 migration](https://docs.simmer.markets/v2-migration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default dry-run output; live trading requires explicit command-line opt-in and configured credentials.]

## Skill Version(s):

1.23.8 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
