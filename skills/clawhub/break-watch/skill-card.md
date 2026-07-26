## Description: <br>
Break Watch scans real-time A-share market data from Tongdaxin via pytdx and returns stocks that simultaneously show volume expansion, price gains, and a bullish intraday candle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hunkguo](https://clawhub.ai/user/hunkguo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and market-analysis agents use this skill to run intraday A-share scans, identify stocks matching volume breakout, price rise, and bullish-candle criteria, and present structured results for monitoring and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Tongdaxin market-data servers during scans. <br>
Mitigation: Run it only where that network access is acceptable, and review or override the configured server list before use. <br>
Risk: The skill can write scan outputs and logs to local directories. <br>
Mitigation: Set explicit output directories and inspect generated CSV, HTML, TXT, and log files before sharing them. <br>
Risk: The security guidance notes dependency hygiene issues. <br>
Mitigation: Pin dependencies before installation and install pyinstaller only when packaging the tool is required. <br>
Risk: Screening results could be mistaken for investment advice. <br>
Mitigation: Use the output for market monitoring and review only, and keep the disclaimer that scores and signals are not investment advice. <br>


## Reference(s): <br>
- [Break Watch strategy reference](artifact/references/strategy.md) <br>
- [ClawHub skill page](https://clawhub.ai/hunkguo/skills/break-watch) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [JSON scan output with Markdown summaries and optional CSV, HTML, and TXT files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write scan results and logs under configured output directories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
