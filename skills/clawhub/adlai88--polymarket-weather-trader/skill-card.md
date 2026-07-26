## Description: <br>
Trade Polymarket weather markets using NOAA (US) and Open-Meteo (international) forecasts via Simmer API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adlai88](https://clawhub.ai/user/adlai88) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and trading users use this skill to inspect, configure, and run automated weather-market strategies against Polymarket via the Simmer API. It supports dry-run analysis, paper trading, position checks, and live execution when the user explicitly opts in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live mode can place real-money Polymarket orders and expose the user to financial loss. <br>
Mitigation: Keep the default dry-run mode or set TRADING_VENUE=sim until wallet setup, dashboard limits, position caps, and loss behavior have been reviewed. <br>
Risk: The --no-safeguards option can disable strategy-side checks for flip-flop behavior, slippage, time decay, and resolved markets. <br>
Mitigation: Leave safeguards enabled for normal use and review any explicit request to disable them before running live. <br>
Risk: Stop-loss monitoring may not cap losses when weather buckets gap to resolution without intermediate liquidity. <br>
Mitigation: Size positions conservatively and assume each weather bucket position can go to zero. <br>
Risk: The skill uses API keys and may use a wallet private key for external-wallet trading. <br>
Mitigation: Provide only the required credentials, keep secrets out of prompts and logs, and prefer managed-wallet or paper-trading flows when appropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/adlai88/skills/polymarket-weather-trader) <br>
- [Simmer Wallet Setup](https://docs.simmer.markets/wallets) <br>
- [Simmer API](https://api.simmer.markets) <br>
- [Simmer V2 Migration](https://docs.simmer.markets/v2-migration) <br>
- [Disclaimer](DISCLAIMER.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python snippets, configuration tables, and status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can trigger API calls and, with explicit live-mode configuration, real-money trading actions through Simmer and Polymarket.] <br>

## Skill Version(s): <br>
1.23.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
