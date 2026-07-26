## Description: <br>
Manage AIUSD accounts and trades: check balances, execute buy/sell/swap orders, stake or unstake, withdraw funds, top up gas, and view transaction history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an assistant manage AIUSD account workflows, including balance checks, trading, staking, withdrawals, gas top-ups, transaction history, deposits, and reauthentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Assistant-mediated trading, staking, withdrawals, and gas top-ups can move funds. <br>
Mitigation: Require explicit user confirmation before each financial action and verify the asset, amount, chain, destination address, and fees. <br>
Risk: Self-extracting installers and reauthentication flows can modify local state. <br>
Mitigation: Install only if the publisher is trusted, inspect the extracted package before running installers, and understand that reauthentication can delete local auth/session files and may install or invoke mcporter. <br>
Risk: The server security verdict is Review because safeguards are not strong enough for a fund-moving skill. <br>
Mitigation: Review and scan the skill before deployment, and limit use to environments where financial actions can be supervised. <br>


## Reference(s): <br>
- [Aiusd Skills on ClawHub](https://clawhub.ai/chaunceyliu/skills/aiusd-skills) <br>
- [AIUSD official website](https://aiusd.ai) <br>
- [AIUSD OAuth login](https://mcp.alpha.dev/oauth/login) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Natural-language or Markdown responses with tool JSON/text results and inline shell commands when setup or reauthentication is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce account balances, trading account addresses, transaction status, deposit guidance, authentication guidance, or trade and account-management responses.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
