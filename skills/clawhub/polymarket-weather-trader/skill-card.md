## Description:

Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure, test, and run agent-assisted temperature-market trading workflows on Polymarket through Simmer. It supports dry-run, paper trading, status checks, replay/backtest gating, and explicit live execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode can place real-money trades.

Mitigation: Start with dry-run or TRADING_VENUE=sim, and do not use --live until wallet limits, daily caps, and position caps are configured.

Risk: The release trusts an unpinned trading SDK and any ambient trade journal module.

Mitigation: Pin and review the Simmer SDK version, and verify that no unexpected tradejournal module is present before running with trading credentials.

Risk: Weather temperature buckets can resolve by gapping, so stop-loss monitors may not cap losses.

Mitigation: Size positions conservatively, assume the full position can go to zero, and keep per-trade and daily caps low.

Risk: Default strategy parameters are a framework and are not validated as profitable.

Mitigation: Run paper mode and replay/backtest gates with an honest forecast archive before scaling beyond default position sizes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-weather-trader)
- [Simmer wallet setup](https://docs.simmer.markets/wallets)
- [Simmer API](https://api.simmer.markets)
- [Polymarket V2 migration](https://docs.simmer.markets/v2-migration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute local Python scripts and API-backed trading/status workflows when invoked by the agent; live trading requires explicit flags and credentials.]

## Skill Version(s):

1.23.17 (source: evidence release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
