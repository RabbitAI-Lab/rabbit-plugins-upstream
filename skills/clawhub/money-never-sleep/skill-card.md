## Description: <br>
MNS (Money Never Sleeps) is an operations manual for agents using a local investment-ledger CLI to inspect holdings, record already-executed trades, refresh prices, generate rule-based rebalancing reports, adjust strategy parameters, and run backtests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sopaco](https://clawhub.ai/user/sopaco) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to guide an agent through MNS CLI workflows for local portfolio bookkeeping, price updates, market-sentiment checks, strategy reports, configuration review, and backtesting. It is intended to keep agent actions constrained to recorded user-executed trades and command outputs rather than brokerage execution or financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local ledger data can be changed, erased, or corrupted by initialization, removal, cash, configuration, buy, or sell commands. <br>
Mitigation: Confirm user intent before mutating commands, avoid forced initialization unless explicitly authorized, and only record trades the user says were already executed elsewhere. <br>
Risk: Rule-based rebalancing reports may be mistaken for brokerage execution or personalized investment advice. <br>
Mitigation: Present reports as mechanical calculations from MNS rules, state that MNS connects to no broker and executes no trades, and leave investment decisions to the user or a qualified advisor. <br>
Risk: Market sentiment and price workflows depend on network data sources that may fail or return unavailable data. <br>
Mitigation: Use only observed command output, report data-source failures plainly, and use manual price updates only with values supplied or confirmed by the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sopaco/skills/money-never-sleep) <br>
- [Publisher profile](https://clawhub.ai/user/sopaco) <br>
- [money-never-sleep project repository](https://github.com/sopaco/money-never-sleep) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text] <br>
**Output Format:** [Markdown guidance with inline shell commands and concise command-output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill should rely on current command output for portfolio numbers and should not fabricate prices, shares, returns, or strategy results.] <br>

## Skill Version(s): <br>
0.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
