## Description: <br>
Trade AIUSD tokens, manage balances, stake, withdraw, top up gas, view transaction history, and handle authentication via MCP backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External AI assistant users use this skill to manage AIUSD trading accounts through natural-language requests, including balance checks, trades, staking, withdrawals, gas top-ups, deposits, and transaction history. Agents should confirm every funds-moving action and use the live tool schema before making calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute trades, withdrawals, staking, unstaking, and gas top-ups that may move funds. <br>
Mitigation: Use a limited-balance account and require explicit confirmation before every trade, withdrawal, stake, unstake, or gas top-up. <br>
Risk: Authentication uses local tokens and browser login flows. <br>
Mitigation: Protect local token files and independently verify login domains before completing authentication. <br>
Risk: The self-extracting installers can make broad local changes while installing the skill. <br>
Mitigation: Run installers only in a clean directory without important local changes or secrets, and review the package before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chaunceyliu/skills/aiusd-trade-agent) <br>
- [AIUSD Official Website](https://aiusd.ai) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Agent Reference](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with concise status text, tool-call guidance, and shell commands when authentication or setup actions are needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live tool schemas for backend calls; funds-moving operations require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
