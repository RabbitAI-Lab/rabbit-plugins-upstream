## Description: <br>
Screen a watchlist of stock tickers for cash-secured put candidates suited to the options wheel strategy, using free Yahoo Finance data via yfinance with no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to generate wheel-strategy cash-secured put screening output for ticker watchlists. It helps compare candidate expirations, strikes, estimated premium yields, implied volatility, volume, and open interest before independent trade review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market data and option quotes may be delayed, stale, incomplete, or wide for illiquid contracts. <br>
Mitigation: Verify live quotes, bid/ask spread, open interest, volume, and tradability in an authoritative trading platform before acting. <br>
Risk: The screening output does not evaluate suitability, taxes, assignment risk, margin requirements, or portfolio concentration. <br>
Mitigation: Use the output only as an idea-generation input and perform independent financial, risk, and compliance review before any trade. <br>
Risk: The script estimates option premium yield with moneyness as a delta proxy instead of live greeks. <br>
Mitigation: Confirm delta, greeks, implied volatility, and scenario risk with a live options analytics source before relying on a candidate. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text terminal table with concise Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires yfinance market data; output is for idea generation only and does not execute trades.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
