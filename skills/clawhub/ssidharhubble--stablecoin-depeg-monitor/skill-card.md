## Description: <br>
Real-time stablecoin peg monitoring that checks major stablecoins across simulated CEX and DEX venues, classifies peg status, summarizes historical stability, and surfaces cross-venue arbitrage windows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, DeFi operators, treasury teams, traders, and risk managers use this skill to check stablecoin peg status, review simulated stability history, and inspect potential arbitrage windows before replacing mock data with verified market integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake simulated stablecoin, liquidity, and arbitrage outputs for live market data. <br>
Mitigation: Clearly label generated outputs as simulated and replace the mock data source with verified live market integrations before using the skill for monitoring, trading, treasury, or compliance decisions. <br>
Risk: Financial decisions based on unverified or simulated depeg signals could be misleading. <br>
Mitigation: Treat results as operational guidance only until reviewed by a qualified operator and cross-checked against authoritative market data sources. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ssidharhubble/skills/stablecoin-depeg-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI output includes stablecoin price status, venue prices, liquidity estimates, deviation basis points, thresholds, timestamps, historical summaries, and arbitrage windows. Bundled outputs use deterministic simulated market data unless live integrations are added.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
