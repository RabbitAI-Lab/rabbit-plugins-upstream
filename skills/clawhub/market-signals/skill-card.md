## Description: <br>
Market Signals is a local CSV technical-analysis skill that calculates indicators such as RSI, moving averages, volume anomalies, ATR, MACD, Bollinger Bands, VWAP, support and resistance levels, then returns an overall signal score and action label. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent workflows use this skill to run local technical-signal scans over CSV price data, compare multiple stocks, inspect signal history, and produce human-readable trading-signal summaries. The generated labels should be treated as technical-analysis outputs, not financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces buy, watch, wait, or avoid labels that could be mistaken for financial advice. <br>
Mitigation: Treat outputs as technical-analysis signals only and require human review before any investment or trading decision. <br>
Risk: The --output option writes results to a user-provided path. <br>
Mitigation: Review the output path before execution and avoid overwriting important files. <br>


## Reference(s): <br>
- [Market Signals ClawHub page](https://clawhub.ai/cqdev-ai/skills/market-signals) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown or terminal text with tables, optional ASCII charts, and optional JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on CSV input; optional --output writes analysis results to a user-provided path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
