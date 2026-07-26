## Description: <br>
Binance Dollar-Cost Averaging (DCA) tool for automated and manual recurring crypto purchases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fpsjago](https://clawhub.ai/user/fpsjago) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to plan DCA strategies, check Binance prices and balances, view trade history, and execute manual or scheduled spot buy orders through Binance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place live Binance spot buy orders. <br>
Mitigation: Use Binance testnet first and require explicit user confirmation before any live buy. <br>
Risk: Agent-accessible API credentials could enable unintended trading if over-permissioned. <br>
Mitigation: Use restricted Binance API keys with withdrawals disabled and IP limits where possible. <br>
Risk: Recurring jobs can continue buying without strong built-in caps. <br>
Mitigation: Keep order sizes small and place external limits on scheduled runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fpsjago/skills/binance-dca-tool) <br>
- [Binance API endpoint](https://api.binance.com) <br>
- [Binance testnet endpoint](https://testnet.binance.vision) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash commands and command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Binance public and signed REST endpoints through the provided shell script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
