## Description: <br>
Provides read-only OKX public market data commands for prices, order books, candles, funding and open-interest data, market screeners, instruments, and technical indicators without requiring API credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve public OKX market data, discover instruments, screen markets, and run technical indicator queries through the OKX CLI. It is intended for data lookup and analysis support, not account management, order placement, bot operation, or trading recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market data and technical indicators can be mistaken for trading advice. <br>
Mitigation: Treat outputs as raw data only; interpretation and trading decisions remain with the user. <br>
Risk: Large historical candle requests can consume excessive context. <br>
Mitigation: Estimate candle count first and ask for confirmation before fetching more than 500 candles. <br>
Risk: Derivative, option, stock token, metals, commodities, forex, and bond instruments require valid identifiers and may have trading-hour constraints. <br>
Mitigation: Verify instrument format, live state, and ticker data before relying on the returned market data. <br>


## Reference(s): <br>
- [OKX](https://www.okx.com) <br>
- [Price & Market Data Commands](artifact/references/price-data-commands.md) <br>
- [Derivatives & Contract Data Commands](artifact/references/derivatives-commands.md) <br>
- [Instrument Discovery Commands](artifact/references/instrument-commands.md) <br>
- [Technical Indicator Command Reference](artifact/references/indicator-commands.md) <br>
- [Cross-Skill Workflows & MCP Tool Reference](artifact/references/workflows.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/numpy0001/okx-cex-market) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON market data output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only public market data workflows; raw OKX API v5 responses are available when commands use --json.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
