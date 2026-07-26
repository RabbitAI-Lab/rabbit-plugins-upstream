## Description: <br>
AI agent for automated prediction market trading on Polymarket <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arubiku](https://clawhub.ai/user/arubiku) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to run a Polymarket trading workflow that analyzes markets, detects arbitrage opportunities, and prepares or executes trades with stated risk controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests wallet-level credentials and live trading authority without enough implementation provenance or credential-handling documentation. <br>
Mitigation: Use only a dedicated low-balance wallet, verify the actual mia-polymarket command from a trusted source, and do not provide a primary wallet private key unless the publisher supplies reviewed code, enforceable limits, and clear credential-handling documentation. <br>
Risk: Automated trading can execute unintended or financially harmful trades. <br>
Mitigation: Require dry-run mode or manual confirmation before any live trade and independently enforce portfolio limits, stop-loss behavior, and daily review. <br>


## Reference(s): <br>
- [Polymarket](https://polymarket.com) <br>
- [ClawHub skill page](https://clawhub.ai/arubiku/skills/mia-polymarket-trader) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include trading commands and credential setup guidance that should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
