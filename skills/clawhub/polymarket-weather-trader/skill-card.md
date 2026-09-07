## Description:

Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate and optionally automate weather-market trading strategies with dry-run, paper-trading, and live Polymarket execution modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move real funds when live trading is enabled.

Mitigation: Use dry-run or the $SIM venue first, then set strict dashboard trade limits before any live run.

Risk: Key live-trading safeguards can be disabled.

Mitigation: Keep safeguards enabled for live trading and avoid combining --no-safeguards with --live.

Risk: External-wallet mode may require a wallet private key in the runtime environment.

Mitigation: Run in an isolated environment, protect credentials from logs and shared shells, and prefer a pinned, reviewed simmer-sdk version.

Risk: Weather buckets can gap to zero at resolution, so a percentage stop-loss may not cap losses.

Mitigation: Size positions conservatively and assume the full position can be lost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-weather-trader)
- [Simmer wallet setup documentation](https://docs.simmer.markets/wallets)
- [Simmer API base URL](https://api.simmer.markets)
- [Polymarket V2 migration guide](https://docs.simmer.markets/v2-migration)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate API-backed dry-run, paper-trading, or live-trading actions depending on user configuration.]

## Skill Version(s):

1.23.6 (source: frontmatter, release evidence, changelog released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
