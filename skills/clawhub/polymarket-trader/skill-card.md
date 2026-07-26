## Description: <br>
Build and analyze a BTC 1h Up/Down trading strategy anchored to Binance BTCUSDT, with edge thresholds, regime filters, and trade validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drakec48](https://clawhub.ai/user/drakec48) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, traders, and trading-system operators use this skill to design, evaluate, tune, and troubleshoot Polymarket BTC 1h Up/Down strategies using Binance BTCUSDT as the resolution anchor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence financial decisions for Polymarket BTC 1h Up/Down markets. <br>
Mitigation: Treat outputs as analysis only and require explicit separate confirmation before any real trade or account action. <br>
Risk: The bundled scripts contact public Binance endpoints, so output quality depends on network access, endpoint availability, rate limits, and current market data. <br>
Mitigation: Review fetched data, keep script runs scoped, and avoid relying on a single script result without checking the market context. <br>
Risk: The fill-explanation script reads a local events.jsonl fill log that may contain sensitive trading history. <br>
Mitigation: Keep secrets out of logs, review the log path before running the script, and avoid sharing generated output that exposes private trading activity. <br>


## Reference(s): <br>
- [Strategy reference](references/strategy.md) <br>
- [Binance public API endpoint](https://api.binance.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code or shell commands; bundled scripts may emit JSON or tabular text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May contact public Binance endpoints and may read a local events.jsonl fill log when the bundled scripts are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
