## Description: <br>
Trade Polymarket BTC 5-minute and 15-minute fast markets using Binance momentum signals, enhanced with TradingAgents pipeline, 50-persona swarm consensus, ACTA receipts, and Cedar governance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zombie760](https://clawhub.ai/user/zombie760) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to monitor BTC fast markets, generate momentum-based trade decisions, and submit trades through a Simmer-compatible trading API when configured. Because it can place trades, it should be used only with intentional paper or live-trading controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place trades through a configured trading API. <br>
Mitigation: Install and run it only when autonomous trading is intended, verify SIMMER_API_URL before use, and require explicit dry-run or live-trading controls. <br>
Risk: Documented paper-trading and governance safeguards are not fully implemented in the artifact. <br>
Mitigation: Add or require enforceable trade limits, authorization gates, and auditable governance checks before connecting the skill to funded accounts. <br>
Risk: Trading behavior depends on external market data and API responses. <br>
Mitigation: Monitor API failures and market-data quality, and review generated trade decisions before deployment in any live environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zombie760/skills/fast-loop-skill) <br>
- [Simmer API endpoint](https://api.simmer.markets) <br>
- [Binance klines API endpoint](https://api.binance.com/api/v3/klines) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration, guidance] <br>
**Output Format:** [Text logs, JSON-like trade results, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SIMMER_API_URL and may use SIMMER_API_KEY; the script can fetch Binance market data and call a Simmer trading API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
