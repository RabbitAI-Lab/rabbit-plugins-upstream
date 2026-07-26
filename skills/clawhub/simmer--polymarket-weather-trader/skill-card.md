## Description: <br>
Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simmer](https://clawhub.ai/user/simmer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and trading agents use this skill to inspect, configure, and optionally automate weather-market trading strategies on Polymarket through Simmer. It supports dry-run analysis, paper trading, position checks, and live execution when the user deliberately enables live mode and supplies required credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real-money Polymarket trades when live mode is enabled. <br>
Mitigation: Start in dry-run or TRADING_VENUE=sim, keep small per-trade and daily caps, and require deliberate review before passing --live. <br>
Risk: The --no-safeguards flag can bypass strategy-side checks for slippage, time decay, flip-flop warnings, and resolved-market status. <br>
Mitigation: Avoid combining --live with --no-safeguards; keep safeguards enabled unless a knowledgeable operator has reviewed the trade context. <br>
Risk: External-wallet use may require WALLET_PRIVATE_KEY and exposes signing risk. <br>
Mitigation: Avoid providing WALLET_PRIVATE_KEY unless external-wallet signing is intended and understood; prefer managed-wallet flows where appropriate. <br>
Risk: Weather bucket markets can gap to zero at resolution, so stop-loss monitoring may not cap losses. <br>
Mitigation: Size positions as though the full position can be lost and validate behavior in paper mode before scaling. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/polymarket-weather-trader) <br>
- [Simmer Wallet Setup](https://docs.simmer.markets/wallets) <br>
- [Simmer API](https://api.simmer.markets) <br>
- [Simmer Polymarket V2 Migration](https://docs.simmer.markets/v2-migration) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python commands, configuration values, and trading-status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports dry-run, paper, status, and live trading flows; live trading requires explicit user opt-in and credentials.] <br>

## Skill Version(s): <br>
1.23.4 (source: frontmatter, CHANGELOG, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
