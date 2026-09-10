## Description:

Trades Kalshi weather markets using NOAA forecasts through Simmer SDK and DFlow on Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External agents, developers, and trading operators use this skill to configure and run Kalshi weather-market scans, simulated trades, live trades, and position checks based on NOAA temperature forecasts.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill requires wallet-signing authority through SOLANA_PRIVATE_KEY.

Mitigation: Use a dedicated low-balance wallet, keep private keys out of chat, and inject secrets only through a secured environment or secret store.

Risk: Running with --live can place real automated trades.

Mitigation: Test in the default paper mode before using --live, keep position sizes conservative, and review all trading settings before scheduling runs.

Risk: Some safeguards can be bypassed or may fail open.

Mitigation: Keep safeguards enabled for live trading and do not combine --live with --no-safeguards.

Risk: The Simmer SDK dependency is part of the trusted computing base.

Mitigation: Review and pin the SDK dependency before deployment, and repeat review before dependency updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/kalshi-weather-trader)
- [Publisher profile](https://clawhub.ai/user/simmer)
- [Simmer API](https://api.simmer.markets)
- [NOAA Weather API](https://api.weather.gov)
- [DFlow Proof KYC](https://dflow.net/proof)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run Python commands that call external APIs; live trading requires explicit --live execution and credentials.]

## Skill Version(s):

1.0.12 (source: server release metadata, SKILL.md frontmatter, CHANGELOG released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
