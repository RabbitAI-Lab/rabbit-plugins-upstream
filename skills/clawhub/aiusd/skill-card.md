## Description: <br>
Manage AIUSD trading, staking, withdrawals, gas top-ups, balance inquiries, and transaction history through authenticated backend calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users with OpenClaw or ClawdBot-compatible assistants use this skill to manage AIUSD accounts, execute crypto trades, stake or unstake AIUSD, withdraw funds, top up gas, and review account history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move funds or alter authentication state when it has access to a valid AIUSD account token. <br>
Mitigation: Require explicit user confirmation before every trade, withdrawal, stake, unstake, gas top-up, and reauthentication action. <br>
Risk: The bundled self-extracting installers overwrite an existing aiusd-skill directory during installation. <br>
Mitigation: Review the installer package before execution and avoid keeping important local data in an existing aiusd-skill directory. <br>
Risk: The security review verdict is suspicious because fund-moving authority has weak safeguards and installer behavior is under-disclosed. <br>
Mitigation: Install only if the publisher is trusted and scan the package before deployment. <br>


## Reference(s): <br>
- [ClawHub aiusd Skill Page](https://clawhub.ai/chaunceyliu/skills/aiusd) <br>
- [AIUSD Official Website](https://aiusd.ai) <br>
- [AIUSD OAuth Login](https://mcp.alpha.dev/oauth/login) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and user-facing account or transaction summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require live tool schema discovery and authenticated backend access before account, trade, staking, withdrawal, gas, or history operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
