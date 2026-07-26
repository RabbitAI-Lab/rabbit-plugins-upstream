## Description: <br>
Backtest dollar-cost averaging (DCA) against lump-sum investing on any coin's real historical price data, using the free CoinGecko market_chart API with no API key required and up to 365 days of daily history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to compare weekly crypto dollar-cost averaging with an equivalent lump-sum entry over a selected historical window before deciding how to allocate capital. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local Python script that sends public requests to CoinGecko. <br>
Mitigation: Install and run it only where outbound public API requests are acceptable; no API key, wallet credentials, trading account, or account modification is required. <br>
Risk: Backtest results are historical return comparisons and may be mistaken for investment advice or future performance predictions. <br>
Mitigation: Treat outputs as historical analysis only and review the limitations on risk-adjusted returns, fees, slippage, spread, and market timing before relying on results. <br>


## Reference(s): <br>
- [CoinGecko API](https://api.coingecko.com/api/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Plain text summary or JSON from a local Python command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports total invested, end value, percent return, and the better-performing strategy for the selected historical window.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
