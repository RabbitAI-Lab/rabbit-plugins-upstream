## Description: <br>
Binance Alpha new coin launch detector. Uses WebSocket to monitor !miniTicker@arr stream and detects new trading pairs immediately when they appear. Maintains known symbols set in memory and triggers alert for new symbols with valid opening price. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-tool operators use this skill to monitor Binance public market streams for newly appearing spot trading pairs and review recent listing alerts. It helps an agent set up, run, and inspect a local terminal-based listing monitor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The monitor connects to Binance public WebSocket and REST endpoints and depends on external market data availability. <br>
Mitigation: Run it only in environments where Binance network access is allowed, and review endpoint access before deployment. <br>
Risk: The script keeps known-symbol and alert-history files under ~/.config/alpha. <br>
Mitigation: Use a contained runtime or inspect and clear the state directory when local persistence is not desired. <br>
Risk: Listing alerts can be delayed, duplicated, or wrong if WebSocket delivery, reconnection, or baseline state is disrupted. <br>
Mitigation: Confirm important alerts against Binance directly and reset or rebuild local state when false positives appear. <br>


## Reference(s): <br>
- [Binance WebSocket API](https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams) <br>
- [Binance WebSocket API Reference](references/binance_ws.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and terminal output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces terminal monitoring output, alert history summaries, status text, and reset guidance for local state under ~/.config/alpha.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
