## Description: <br>
Monitors Polymarket prediction markets for arbitrage opportunities and provides scripts and guidance for market fetching, opportunity detection, continuous monitoring, risk scoring, and alerting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johny0920](https://clawhub.ai/user/johny0920) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technically sophisticated traders use this skill to monitor Polymarket markets, inspect possible arbitrage signals, and generate command-line workflows for paper trading or manually verified trades. It is best treated as a monitoring and analysis helper rather than an automated trading system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill overstates trading capabilities and should not be treated as an automated trading system. <br>
Mitigation: Use it only for monitoring, paper trading, and manually verified opportunities unless the trading, logging, and secret-handling behavior has been reviewed and fixed. <br>
Risk: The security evidence flags unsafe command and webhook-token handling. <br>
Mitigation: Run the scripts in a virtual environment with trusted paths and avoid passing real webhook tokens until logging and secret handling are corrected. <br>
Risk: Artifact documentation notes that displayed Polymarket prices can be stale or not executable, and low-liquidity opportunities may be misleading. <br>
Mitigation: Manually verify each opportunity on Polymarket, prefer high-volume markets, start with paper trading, and apply strict position and loss limits before risking funds. <br>


## Reference(s): <br>
- [Getting Started with Polymarket Arbitrage](artifact/references/getting_started.md) <br>
- [Arbitrage Types on Polymarket](artifact/references/arbitrage_types.md) <br>
- [Polymarket](https://polymarket.com) <br>
- [Polymarket Documentation](https://docs.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python script references, and JSON output file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update local JSON files containing market snapshots, detected arbitrage opportunities, and alert state when its scripts are run.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
